Feature: Get all notes

  Scenario: Get all notes when notes exist
    Given there are existing notes in the system
    When I request all notes
    Then the response status code should be 200
    And the response should contain a list of notes

  Scenario: Get all notes when no notes exist
    Given there are no notes in the system
    When I request all notes
    Then the response status code should be 200
    And the response should contain an empty list