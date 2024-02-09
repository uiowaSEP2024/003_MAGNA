Feature: Home Page functionality
  Scenario: User clicks on a form
    Given the user is on the home page
    When the user clicks on the PTO button
    Then the user should be directed to the PTO page

  Scenario: Kiosk is logged in
    Given the kiosk is logged in
    When on the home page
    Then the kiosk should see all user forms

  Scenario: Manager is logged in
    Given a manager is logged in
    When on the home page
    Then The manager should see all forms
Feature: Home Page Functionality
  Scenario: User goes to fill out PTO form
    Given the user has navigated to the home page
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form
