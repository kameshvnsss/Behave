Feature: Testing the User Creation in API
  Scenario: Post the user
    Given the API endpoint for users "https://reqres.in/api/users/"
    When I make a Post request to the API
    Then the response status code should be 201
    And user post successful