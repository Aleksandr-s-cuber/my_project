Feature: Edit a note by ID

  Scenario: Edit a note by valid ID
    Given a note exists with ID "123"
    And a valid payload to update the note
    When I send a request to update the note with ID "123"
    Then the response status code should be 200
    And the note with ID "123" should be updated

  Scenario: Edit a note by invalid ID
    Given a valid payload to update the note
    When I send a request to update the note with ID "invalid_id"
    Then the response status code should be 400
    And the response should contain an error message