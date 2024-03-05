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
  Scenario Outline: Correct login on chrome
    Given the user is using chrome
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the home page
    Examples:
      | username | password |
      | kiosk1 | kioskpass1 |
      | floor1 | floorpass1 |
      | manager1 | managerpass1 |
      | hr1      | hrpass1      |
      | admin    | adminpass123   |

    # tests incorrect login where there is a missing username
    # Using chrome for webdriver in these tests, with different user variants
  Scenario Outline: Missing username on chrome
    Given the user is using chrome
    And the user has navigated to the login page
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | password |
      | kioskpass1 |
      | floorpass1 |
      | managerpass1 |
      | hrpass1      |
      | adminpass123 |

  Scenario Outline: Missing password on chrome
    Given the user is using chrome
    And the user has navigated to the login page
    And the user enters <username> as the username
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username |
      | kiosk1   |
      | floor1   |
      | manager1 |
      | hr1      |
      | admin    |


  # tests incorrect login with mistyped username
  # Chrome webdriver, all user variants

  Scenario Outline: Mistyped username on chrome
    Given the user is using chrome
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username | password |
      | kiosk11 | kioskpass1 |
      | flooor1 | floorpass1 |
      | managerr1 | managerpass1 |
      | he1      | hrpass1      |
      | admin1    | adminpass123   |

  # tests incorrect login with mistyped password
  # Chrome webdriver, all user variants

  Scenario Outline: Mistyped password on chrome
    Given the user is using chrome
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username | password |
      | kiosk1 | kioskpass |
      | floor1 | floorpass |
      | manager1 | managerpass |
      | hr1      | hrpass      |
      | admin    | adminpass1   |


  # tests incorrect login with no fields
  # chrome webdriver, no user variants needed

  Scenario: user tries to login with no fields on Chrome
    Given the user is using chrome
    And the user has navigated to the login page
    When the user presses the login button
    Then the user should be on the login page


  # EDGE TESTS START HERE

  # tests on edge for correct login, user variants

  Scenario Outline: Correct login on edge
    Given the user is using edge
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the home page
    Examples:
      | username | password |
      | kiosk1 | kioskpass1 |
      | floor1 | floorpass1 |
      | manager1 | managerpass1 |
      | hr1      | hrpass1      |
      | admin    | adminpass123   |



  # tests incorrect login where there is a missing username
  # Using edge for webdriver in these tests, with different user variants

  Scenario Outline: Missing username on edge
    Given the user is using edge
    And the user has navigated to the login page
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | password |
      | kioskpass1 |
      | floorpass1 |
      | managerpass1 |
      | hrpass1      |
      | adminpass123 |


  # tests incorrect login where there is a missing password
  # Using edge for webdriver in these tests, with different user variants

  Scenario Outline: Missing password on edge
    Given the user is using edge
    And the user has navigated to the login page
    And the user enters <username> as the username
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username |
      | kiosk1   |
      | floor1   |
      | manager1 |
      | hr1      |
      | admin    |


  # tests incorrect login with mistyped username
  # Using edge, all user variants

  Scenario Outline: Mistyped username on edge
    Given the user is using edge
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username | password |
      | kiosk11 | kioskpass1 |
      | flooor1 | floorpass1 |
      | managerr1 | managerpass1 |
      | he1      | hrpass1      |
      | admin1    | adminpass123   |

  # tests incorrect login with mistyped password
  # Using edge, all user variants

  Scenario Outline: Mistyped password on edge
    Given the user is using edge
    And the user has navigated to the login page
    And the user enters <username> as the username
    And the user enters <password> as the password
    When the user presses the login button
    Then the user should be on the login page
    Examples:
      | username | password |
      | kiosk1 | kioskpass |
      | floor1 | floorpass |
      | manager1 | managerpass |
      | hr1      | hrpass      |
      | admin    | adminpass1   |

  # tests incorrect login with no fields
  # using edge, no user variants needed

  Scenario: user tries to login with no fields on edge
    Given the user is using edge
    And the user has navigated to the login page
    When the user presses the login button
    Then the user should be on the login page



  ## Firefox starts here

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

  Scenario: user tries to login with no fields on firefox
    Given the user is using firefox
    And the user has navigated to the login page
    When the user presses the login button
    Then the user should be on the login page

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



