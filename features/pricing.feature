Feature: Check pricing for various plans

  Scenario: See prices for business plans
    Given CloudAcademy page is accessed
    When The pricing button menu is clicked
    Then The pricing page for "business" is opened
    And Buttons for business and individuals are present
    And Plans for "business" are visible
    And The pricing for each "business" plan is visible

  Scenario: See prices for individuals plans
    Given CloudAcademy page is accessed
    When The pricing button menu is clicked
    And The "For Individuals" button is clicked
    Then The pricing page for "individual" is opened
    And Buttons for business and individuals are present
    And Plans for "individual" are visible
    And The pricing for each "individual" plan is visible