Feature: Login functionality
  Scenario: User tries to login with correct credentials
    Given the user has navigated to the login page
    When the user submits the login form with valid credentials
    Then the user should be redirected to the home page
