Feature: Buy small teams plan

  @wip
  Scenario: Buy small teams plan when not signed in on site
    Given CloudAcademy page is accessed
    When The pricing button menu is clicked
    And The Start Now button is clicked on Small Teams plan
    Then The Checkout page is opened
    And A form to sign up to CloudAcademy is present

  @wip
  Scenario: Buy small teams plan when already signed in on site
    Given CloudAcademy page is accessed
    And A user is logged in CloudAcademy
    When The pricing button menu is clicked
    And The Start Now button is clicked on Small Teams plan
    Then The Checkout page is opened
    And A form to buy Small Teams plan is present