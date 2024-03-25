# Created by spenc at 3/24/2024
Feature: Travel Authorization form feature
  # Enter feature description here

  #Chrome tests
  Scenario Outline: Correct form on Chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the home page
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |




  Scenario Outline: Missing clock number on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      |test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |

  Scenario Outline: Missing department on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name  | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test          | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |


  Scenario Outline: Missing departure date on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
    | clock_number | name | department | destination | return_date | travel_type | nights | manager | email | signature |
    | 0001         | test | HR         | place       | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
    |0001          |test  |Floor Staff |place        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
    |0001          |test  |HR |place        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |

  # Personal car, and all of those are skipped as the default is false

  Scenario Outline: Missing nights lodging on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | manager | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |manager2 |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |manager5 |test@test.com |test |

  Scenario Outline: Missing department manager on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |test@test.com |test |

  Scenario Outline: Missing email on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test |

  Scenario Outline: Missing signature on chrome
    Given the user is using chrome
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email |
            | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com           |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |



  #Edge Tests
Scenario Outline: Correct form on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the home page
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |




  Scenario Outline: Missing clock number on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      |test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |

  Scenario Outline: Missing department on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name  | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test          | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |


  Scenario Outline: Missing departure date on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
    | clock_number | name | department | destination | return_date | travel_type | nights | manager | email | signature |
    | 0001         | test | HR         | place       | 2025-1-6    | personal_car| 1      | manager1| test@test.com| test|
    |0001          |test  |Floor Staff |place        |2025-1-6     |company_car  |1       |manager2 |test@test.com |test |
    |0001          |test  |HR |place        |2025-1-6     |car_rental  |1       |manager3 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-1-6     |airfare  |1       |manager4 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |

  # Personal car, and all of those are skipped as the default is false

  Scenario Outline: Missing nights lodging on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | manager | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |manager2 |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |manager5 |test@test.com |test |

  Scenario Outline: Missing department manager on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | email | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |test@test.com |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |test@test.com |test |

  Scenario Outline: Missing email on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | signature |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test |

  Scenario Outline: Missing signature on edge
    Given the user is using edge
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email |
      | 0001         | test | HR         | place       |2025-1-5        | 2025-1-6    | personal_car| 1      | manager1| test@test.com|
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager2 |test@test.com |
      |0001          |test  |HR |place        |2025-1-5        |2025-1-6     |car_rental  |1       |manager3 |test@test.com           |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |airfare  |1       |manager4 |test@test.com |
      |0001          |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |


  #Firefox tests

Scenario Outline: Correct form on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the home page
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test | HR         | place       |2025-01-05       | 2025-01-06    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |HR          |place        |2025-01-05        |2025-01-06     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager5 |test@test.com |test |




  Scenario Outline: Missing clock number on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | name | department | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      |test | HR         | place       |2025-01-5        | 2025-01-6    | personal_car| 1      | manager1| test@test.com| test|
      |test  |Floor Staff |place        |2025-01-5        |2025-01-6     |company_car  |1       |manager2 |test@test.com |test |
      |test  |HR |place        |2025-01-5        |2025-01-6     |car_rental  |1       |manager3 |test@test.com |test |
      |test  |Floor Staff |place        |2025-01-5        |2025-01-6     |airfare  |1       |manager4 |test@test.com |test |
      |test  |Floor Staff |place        |2025-1-5        |2025-1-6     |company_car  |1       |manager5 |test@test.com |test |

  Scenario Outline: Missing department on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name  | destination | departure_date | return_date | travel_type | nights | manager | email | signature |
      | 0001         | test          | place       |2025-01-05        | 2025-01-06    | personal_car| 1      | manager1| test@test.com| test|
      |0001          |test  |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager2 |test@test.com |test |
      |0001          |test  |place        |2025-01-05        |2025-01-06     |car_rental  |1       |manager3 |test@test.com |test |
      |0001          |test  |place        |2025-01-05        |2025-01-06     |airfare  |1       |manager4 |test@test.com |test |
      |0001          |test  |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager5 |test@test.com |test |


  Scenario Outline: Missing departure date on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
    | clock_number | name | department | destination | return_date | travel_type | nights | manager | email | signature |
    | 0001         | test | HR         | place       | 2025-01-06    | personal_car| 1      | manager1| test@test.com| test|
    |0001          |test  |Floor Staff |place        |2025-01-06     |company_car  |1       |manager2 |test@test.com |test |
    |0001          |test  |HR |place        |2025-01-06     |car_rental  |1       |manager3 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-01-06     |airfare  |1       |manager4 |test@test.com |test |
    |0001          |test  |Floor Staff |place        |2025-01-06     |company_car  |1       |manager5 |test@test.com |test |

  # Personal car, and all of those are skipped as the default is false

  Scenario Outline: Missing nights lodging on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | manager | email | signature |
      | 0001         | test | HR         | place       |2025-01-05        | 2025-01-06    | personal_car| manager1| test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |manager2 |test@test.com |test |
      |0001          |test  |HR |place        |2025-01-05        |2025-1-6     |car_rental  |manager3 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |airfare |manager4 |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |manager5 |test@test.com |test |

  Scenario Outline: Missing department manager on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <email> as their email
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | email | signature |
      | 0001         | test | HR         | place       |2025-01-05        | 20250-1-06    | personal_car| 1      | test@test.com| test|
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |test@test.com |test |
      |0001          |test  |HR |place        |2025-01-5        |2025-01-06     |car_rental  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |airfare  |1       |test@test.com |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |test@test.com |test |

  Scenario Outline: Missing email on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <signature> as their signature
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | signature |
      | 0001         | test | HR         | place       |2025-01-05        | 2025-01-06    | personal_car| 1      | manager1| test|
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager2 |test |
      |0001          |test  |HR |place        |2025-01-05        |2025-01-06     |car_rental  |1       |manager3 |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |airfare  |1       |manager4 |test |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager5 |test |

  Scenario Outline: Missing signature on firefox
    Given the user is using firefox
    And a kiosk user is logged in
    And the user clicks on the travel authorization button
    And the user enters <clock_number> as their clock number
    And the user enters <name> as their name
    And the user selects <department> from the dropdown menu
    And the user enters <destination> as their destination
    And the users enters <departure_date> as their departure date
    And the user enters <return_date> as their return date
    And the user selects <travel_type> as their mode of transportation
    And the user enters <nights> as their amount of nights of lodging
    And the user enters <manager> as their manager
    And the user enters <email> as their email
    When the user submits the form
    Then the user should be on the travel authorization form
    Examples:
      | clock_number | name | department | destination | departure_date | return_date | travel_type | nights | manager | email |
      | 0001         | test | HR         | place       |2025-01-05        | 2025-01-06    | personal_car| 1      | manager1| test@test.com|
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager2 |test@test.com |
      |0001          |test  |HR |place        |2025-01-05        |2025-01-06     |car_rental  |1       |manager3 |test@test.com           |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |airfare  |1       |manager4 |test@test.com |
      |0001          |test  |Floor Staff |place        |2025-01-05        |2025-01-06     |company_car  |1       |manager5 |test@test.com |
