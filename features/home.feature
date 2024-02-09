Feature: Home Page Functionality
  Scenario: User goes to fill out PTO form
    Given the user has navigated to the home page
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form
