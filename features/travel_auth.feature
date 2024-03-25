# Created by spenc at 3/24/2024
Feature: Travel Authorization form feature
  # Enter feature description here

  #Chrome tests
  Scenario Outline: Correct form on Chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button

  Scenario Outline: Missing clock number on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  Scenario Outline: Missing department on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  Scenario Outline: Missing departure date on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  # Personal car, and all of those are skipped as the default is false

  Scenario Outline: Missing nights lodging on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  Scenario Outline: Missing department manager on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  Scenario Outline: Missing email on chrome
    Given the user is using chrome
    And a kiosk user is logged in

  Scenario Outline: Missing signature on chrome
    Given the user is using chrome
    And a kiosk user is logged in



  #Edge Tests
  Scenario Outline: Correct form on Edge


  #Firefox tests

  Scenario Outline: Correct form on Firefox