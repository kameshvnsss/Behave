import pandas as pd
import os
import glob
import csv
import mysql.connector as mysql
from mysql.connector import Error

inputdir = 'C:\\Users\\ThoughtSphere\\PycharmProjects\\Behave\\Test1'
outdir = 'C:\\Users\\ThoughtSphere\\PycharmProjects\\Behave\\Test1'

csv_files = glob.glob(os.path.join(inputdir, "*.csv"))
print(csv_files)
for f in csv_files:
    if f.split("\\")[-1] == 'File1.csv':
        df1 = pd.read_csv(f, index_col=False)
        print(df1.columns)
    elif f.split("\\")[-1] == 'File2.csv':
        df2 = pd.read_csv(f, index_col=False)
        df2.rename(columns={'ID': 'PositionID'}, inplace=True)
        print(df2.columns)

df = df1.merge(df2, how='inner', left_on='ID', right_on='InstrumentID')
df = df.drop(['ID', 'Name'], axis=1)
df['Total Price'] = df['Quantity'] * df['Unit Price']
# df  = df.set_index('Index Title')
print(df.columns)
print(df.iterrows())
df.to_csv(outdir + '\\' + 'File3.csv', encoding='utf-8', sep=',', index_label=False)

posdata = pd.read_csv(outdir + '\\' + 'File3.csv', sep=',')
print(posdata.head())

# try:
#     conn = mysql.connect(host='localhost', user='root', port='3306', password='admin')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("CREATE DATABASE Test")
#         print("Database is created")
# except Error as e:
#     print("Error while connecting to MySQL", e)
try:
    conn = mysql.connect(host='localhost', database='test', user='root', port='3306', password='admin')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE test_data(ISIN varchar(255),Unit_Price varchar(255),PositionID varchar(255),\
            InstrumentID varchar(255),Quantity varchar(255),Total_Price varchar(255))")

        for i, row in posdata.iterrows():
            sql = "INSERT INTO test.test_data VALUES (%s,%s,%s,%s,%s,%s)"
            print(sql)
            cursor.execute(sql, tuple(row))
            print("Record inserted")
    conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
