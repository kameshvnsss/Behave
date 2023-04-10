import requests
from behave import given, when, then


@given('the API endpoint for users "{url}"')
def step_impl(context, url):
    context.url = url
    print(url)


@when('I make a Post request to the API')
def step_impl(context):
    # response = requests.get(context.url)
    # headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"name": "morpheus", "job": "leader"}
    response = requests.post(context.url, json=data)
    context.response = response


@then('the response status code should be like  {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code
    print(status_code)


@then('user post successful')
def step_impl(context):
    response_body = context.response.json()
    print(response_body)
