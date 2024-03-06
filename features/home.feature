Feature: Home Page Functionality
  Scenario: User tries to navigate to home page before logging in on Chrome
    Given the user is using chrome
    And the user is not logged in
    And the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario: User tries to navigate to home page before logging in on Firefox
    Given the user is using firefox
    And the user is not logged in
    And the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario: User tries to navigate to home page before logging in on edge
    Given the user is using edge
    And the user is not logged in
    And the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario: User goes to fill out PTO form
    Given the user has logged in
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form

  Scenario: User goes to fill out travel authorization form
    Given the user has logged in
    And is on the home page
    When the user clicks on the travel authorization button
    Then the user is redirected to the travel authorization form


