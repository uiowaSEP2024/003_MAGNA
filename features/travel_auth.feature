Feature: Travel Authorization form functionality
  Scenario: A user logs in and fills out the form correctly, with one traveler
    Given a user is logged in
    And a user is on the travel authorization page
    When the user correctly fills out the date
    When the user correctly selects a reason for travel
    When the user correctly types in their clock number
    When the user correctly enters their name
    When the user correctly selects their department
    When the user correctly fills out their destination


