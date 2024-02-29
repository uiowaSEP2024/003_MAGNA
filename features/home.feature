Feature: Home Page Functionality
  Scenario: User tries to navigate to home page before logging in
    Given the user is not logged in
    When the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario: User goes to fill out PTO form
    Given the user has logged in
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form
