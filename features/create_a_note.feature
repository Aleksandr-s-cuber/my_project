Feature: Create a note
  As a user
  I want to be able to create a note
  So that I can save important information

  Scenario: Successfully create a note with valid data
    Given a note payload with title "My Note" and content "This is the content of my note"
    When I send a request to create the note
    Then the response status code should be 201
    And the response should contain the correct title "My Note"
    And the response should contain the correct content "This is the content of my note"
    And the response should contain an id

  Scenario: Unsuccessfully create a note with invalid data (missing title)
    Given a note payload with only content "This is the content"
    When I send a request to create the note
    Then the response status code should be 422  # ValidationError в FastAPI
    And the response should contain an error message # Вам нужно будет проверить структуру ответа













