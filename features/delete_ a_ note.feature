Feature: Delete a note by ID

  Scenario: Delete an existing note by valid ID
    Given a note exists with ID "123"
    When I send a request to delete the note with ID "123"
    Then the response status code should be 204
    And the note with ID "123" should be deleted

  Scenario: Delete a non-existing note by invalid ID
    When I send a request to delete the note with ID "invalid_id"
    Then the response status code should be 404
    And the response should contain an error message