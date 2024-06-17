Feature: Search courses on Cloudacademy

  Scenario: Search aws courses
    Given Cloudacademy page is accessed
    When Search toolbar is clicked
    And The search box is filled with the value "aws"
    And Enter key is pressed
    Then The search page is opened
    And A list of "aws" courses is shown

  Scenario: Search gcp courses
    Given Cloudacademy page is accessed
    When Search toolbar is clicked
    And The search box is filled with the value "gcp"
    And Enter key is pressed
    Then The search page is opened
    And A list of "gcp" courses is shown

  Scenario: Search azure courses
    Given Cloudacademy page is accessed
    When Search toolbar is clicked
    And The search box is filled with the value "azure"
    And Enter key is pressed
    Then The search page is opened
    And A list of "azure" courses is shown
