Feature: Home Page Functionality
  Scenario: User goes to fill out PTO form
    Given a user is logged in
    And they are on the home page
    When the user clicks on the absence request button
    Then the user is redirected to the absence request form

  Scenario: User goes to fill out travel authorization form
    Given a user is logged in
    And they are on the home page
    When the user clicks on the travel authorization button
    Then the user is redirected to the travel authorization form
