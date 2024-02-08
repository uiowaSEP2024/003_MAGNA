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