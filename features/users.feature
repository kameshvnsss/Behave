Feature: Testing the User API
  Scenario: Retrieve user with ID 2
    Given the API endpoint is "https://reqres.in/api/users/2"
    When I make a GET request to the API
    Then the response status code should be 200
    And the response body should contain users details