import requests
from behave import given, when, then


@given('the API endpoint is "{url}"')
def step_impl(context, url):
    context.url = url
    print(url)


@when('I make a GET request to the API')
def step_impl(context):
    response = requests.get(context.url)
    context.response = response
    print(context)


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code
    print(status_code)


@then('the response body should contain users details')
def step_impl(context):
    response_body = context.response.json()
    assert 'data' in response_body
    user_data = response_body['data']
    assert user_data['id'] == 2
    assert user_data['email'] == 'janet.weaver@reqres.in'
    assert user_data['first_name'] == 'Janet'
    assert user_data['last_name'] == 'Weaver'
