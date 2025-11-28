Feature: Get a note by ID

  Scenario: Get a note by valid ID
    Given a note exists with ID "123"
    When I request the note with ID "123"
    Then the response status code should be 200
    And the response should contain the note with ID "123"

  Scenario: Get a note by invalid ID
    When I request the note with ID "invalid_id"
    Then the response status code should be 400
    And the response should contain an error message

