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
    When the kiosk user correctly enters the username
    When the kiosk user correctly enters the password
    When the user presses the login button
    Then the user should be on the home page

  Scenario: Floor employee tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the floor employee user correctly enters the username
    When the floor employee user correctly enters the password
    When the user presses the login button
    Then the user should be on the home page

  Scenario: HR tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the HR user correctly enters the username
    When the HR user correctly enters the password
    When the user presses the login button
    Then the user should be on the home page

  Scenario: Manager tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the manager user correctly enters the username
    When the manager user correctly enters the password
    When the user presses the login button
    Then the user should be on the home page

  Scenario: Admin tries to login on chrome with correct credentials
    Given the user is using chrome
    And the user has navigated to the login page
    When the admin user correctly enters the username
    When the admin user correctly enters the password
    When the user presses the login button
    Then the user should be on the home page

    # tests incorrect login where there is a missing username
    # Using chrome for webdriver in these tests, with different user variants

  Scenario: Kiosk user tries to login on chrome with missing username
    Given the user is using chrome
    And the user has navigated to the login page
    When the kiosk user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Floor employee tries to login on chrome with missing username
    Given the user is using chrome
    And the user has navigated to the login page
    When the floor employee user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  Scenario: HR tries to login on chrome with missing username
    Given the user is using chrome
    And the user has navigated to the login page
    When the HR user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Manager tries to login on chrome with missing username
    Given the user is using chrome
    And the user has navigated to the login page
    When the manager user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Admin tries to login on chrome with missing username
    Given the user is using chrome
    And the user has navigated to the login page
    When the admin user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  # tests incorrect login where there is a missing password
  # Using chrome for webdriver in these tests, with different user variants


  Scenario: Kiosk user tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the kiosk user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Floor employee tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the floor employee user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: HR tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the HR user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Manager tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the manager user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Admin tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the admin user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  # tests incorrect login with mistyped username
  # Chrome webdriver, all user variants
  Scenario: Kiosk user tries to login on chrome with mistyped username
    Given the user is using chrome
    And the user has navigated to the login page
    When the kiosk user incorrectly enters the username
    When the kiosk user correctly enters the password
    When the user presses the login button
    Then the user should be on the login page

  # tests incorrect login with mistyped password
  # chrome webdriver, all user variants

  # tests incorrect login with no fields
  # chrome webdriver, no user variants needed

  Scenario: user tries to login with no fields on Chrome
    Given the user is using chrome
    And the user has navigated to the login page
    When the user presses the login button
    Then the user should be on the login page


  # EDGE TESTS START HERE

  # tests on edge for correct login, user variants

  Scenario: Kiosk user tries to login on chrome with missing password
    Given the user is using edge
    And the user has navigated to the login page
    When the kiosk user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Floor employee tries to login on chrome with missing password
    Given the user is using chrome
    And the user has navigated to the login page
    When the floor employee user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: HR tries to login on chrome with missing password
    Given the user is using edge
    And the user has navigated to the login page
    When the HR user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Manager tries to login on chrome with missing password
    Given the user is using edge
    And the user has navigated to the login page
    When the manager user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  Scenario: Admin tries to login on edge with missing password
    Given the user is using edge
    And the user has navigated to the login page
    When the admin user correctly enters the username
    When the user presses the login button
    Then the user should be on the login page

  # tests incorrect login where there is a missing username
  # Using edge for webdriver in these tests, with different user variants

  # tests incorrect login where there is a missing password
  # Using edge for webdriver in these tests, with different user variants

  # tests incorrect login with mistyped username
  # Using edge, all user variants

  # tests incorrect login with mistyped password
  # Using edge, all user variants

  # tests incorrect login with no fields
  # using edge, no user variants needed

  Scenario: user tries to login with no fields on edge
    Given the user is using edge
    And the user has navigated to the login page
    When the user presses the login button
    Then the user should be on the login page

  # tests on firefox for correct login, user variants

  # tests incorrect login where there is a missing username
  # Using firefox for webdriver in these tests, with different user variants

  # tests incorrect login where there is a missing password
  # Using firefox for webdriver in these tests, with different user variants

  # tests incorrect login with mistyped username
  # Using firefox, all user variants

  # tests incorrect login with mistyped password
  # Using firefox, all user variants

  # tests incorrect login with no fields
  # using firefox, no user variants needed

  # tests on internet explorer for correct login, user variants

  # tests incorrect login where there is a missing username
  # Using internet explorer for webdriver in these tests, with different user variants

  # tests incorrect login where there is a missing password
  # Using internet explorer for webdriver in these tests, with different user variants

  # tests incorrect login with mistyped username
  # Using internet explorer, all user variants

  # tests incorrect login with mistyped password
  # Using internet explorer, all user variants

  # tests incorrect login with no fields
  # using internet explorer, no user variants needed



