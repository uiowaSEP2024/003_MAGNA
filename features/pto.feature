Feature: PTO form functionality
  Scenario: A user correctly fills out the PTO form
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should be submitted

  Scenario: A user incorrectly fills out the clock number box
    Given a user is logged in and on the PTO form
    When the user incorrectly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user incorrectly fills out the name box
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user incorrectly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user incorrectly fills out the start date box
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user incorrectly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user incorrectly fills out the return date box
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user incorrectly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user incorrectly fills out the approving supervisor box
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user incorrectly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user incorrectly fills out the email box
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user incorrectly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the clock number box blank
    Given a user is logged in and on the PTO form
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the name box blank
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the start date box blank
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the return date box blank
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the supervisor blank
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When The user correctly enters their email
    When the user submits the PTO form
    Then the form should not be submitted

  Scenario: A user leaves the email box blank
    Given a user is logged in and on the PTO form
    When the user correctly fills out clock number
    When the user correctly selects a shift
    When the user correctly fills out their name
    When the user correctly selects a start date
    When the user correctly selects a return date
    When the user correctly selects the reason for time off
    When the user correctly selects their approving supervisor
    When the user submits the PTO form
    Then the form should not be submitted
