Feature: Create a note
  Scenario: Successfully create a note with valid data
    Given I have a valid note payload
    When I send a request to create the note
    Then the response status code should be 200
    And the response should contain the created note data