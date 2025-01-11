Feature: Simple Calculator Functionality

  Scenario: Verify if the calculator performs addition correctly
    Given the calculator is open
    When I enter "5"
    And I press "+"
    And I enter "3"
    And I press "="
    Then the result should be "8"

  Scenario: Verify if the calculator performs subtraction correctly
    Given the calculator is open
    When I enter "10"
    And I press "-"
    And I enter "4"
    And I press "="
    Then the result should be "6"

  Scenario: Verify if the calculator performs multiplication correctly
    Given the calculator is open
    When I enter "6"
    And I press "x"
    And I enter "3"
    And I press "="
    Then the result should be "18"

  Scenario: Verify if the calculator performs division correctly
    Given the calculator is open
    When I enter "9"
    And I press "/"
    And I enter "3"
    And I press "="
    Then the result should be "3.0"

  Scenario: Verify the calculator shows "Error" for division by zero
    Given the calculator is open
    When I enter "10"
    And I press "/"
    And I enter "0"
    And I press "="
    Then the result should be "Error"

  Scenario: Verify the calculator handles clearing the input
    Given the calculator is open
    When I enter "15"
    And I press "C"
    Then the input should be empty

  Scenario: Verify the calculator handles multiple operations
    Given the calculator is open
    When I enter "5"
    And I press "+"
    And I enter "5"
    And I press "x"
    And I enter "2"
    And I press "="
    Then the result should be "15"
