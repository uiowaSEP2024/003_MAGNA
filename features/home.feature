Feature: Home Page Functionality
  Scenario: User tries to navigate to home page before logging in on Chrome
    Given the user is using chrome
    And the user is on the login page
    And the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario:Kiosk user can see travel authorization form on Chrome
    Given the user is using chrome
    And a kiosk user is logged in
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form

  # Still need user variants for the different types of users, and to check if they can see
  # Specific pages on the home page or not

  Scenario: Kiosk user can see travel authorization form on Chrome
    Given the user is using chrome
    And a kiosk user is logged in
    When the user clicks on the travel authorization button
    Then the user is redirected to the travel authorization form


  # Edge tests past this point
  Scenario: User tries to navigate to home page before logging in on Edge
    Given the user is using edge
    And the user is on the login page
    And the user tries to navigate to the home page
    Then the user is redirected to the login page

  Scenario:Kiosk user can see travel authorization form on Chrome
    Given the user is using edge
    And a kiosk user is logged in
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form

  # Still need user variants for the different types of users, and to check if they can see
  # Specific pages on the home page or not

  Scenario: Kiosk user can see travel authorization form on Edge
    Given the user is using edge
    And a kiosk user is logged in
    When the user clicks on the travel authorization button
    Then the user is redirected to the travel authorization form





