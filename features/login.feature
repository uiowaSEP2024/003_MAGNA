Feature: Login functionality

  #Old, less modular tests are deprecated
#  Scenario: User tries to login with correct credentials
#    Given the user has navigated to the login page
#    When the user submits the login form with valid credentials
#    Then the user should be redirected to the home page
#
#  Scenario: User tries to login with incorrect credentials
#    Given the user has navigated to the login page
#    When the user submits the login form with incorrect credentials
#    Then the user should not be redirected to the home page

  #Newer tests designed to be more modular

  # tests on chrome for correct login, user variants
  Scenario: Kiosk user tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the kiosk user correctly logs in
    Then the user should be on the home page

  Scenario: Floor employee tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the floor employee user correctly logs in
    Then the user should be on the home page

    Scenario: HR tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the HR user correctly logs in
    Then the user should be on the home page

    Scenario: Manager tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the manager user correctly logs in
    Then the user should be on the home page

    Scenario: Admin tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the admin user correctly logs in
    Then the user should be on the home page


