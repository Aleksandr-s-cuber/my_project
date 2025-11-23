# from behave import given, when, then
# from page_object.note_page import NotePage
# from factories.note_factory import NoteFactory
#
# @given('I have a valid note payload')
# def step_impl(context):
#     context.note_data = NoteFactory()
# #
# @when('I send a request to create the note')
# def step_impl(context):
#     context.page = NotePage("http://127.0.0.1:8000")
#     context.response = context.page.create_note(context.note_data)
#
# @then('the response status code should be {status_code:d}')
# def step_impl(context, status_code):
#     assert context.response.status_code == status_code
#
# @then('the response should contain the created note data')
# def step_impl(context):
#     note = context.response.json()
#     assert note['title'] == context.note_data['title']
#     assert note['content'] == context.note_data['content']



import requests
import json
from behave import *
from factories import NoteFactory



class NotesAPIClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def create_note(self, note_data):
        headers = {'Content-Type': 'application/json'}
        return requests.post(f"{self.base_url}", json=note_data, headers=headers)

    def get_note(self, note_id):
        return requests.get(f"{self.base_url}/{note_id}")

    def get_all_notes(self):
        return requests.get(f"{self.base_url}")

    def update_note(self, note_id, update_data):

        headers = {'Content-Type': 'application/json'}
        return requests.put(f"{self.base_url}/{note_id}", json=update_data, headers=headers)

    def delete_note(self, note_id):

        return requests.delete(f"{self.base_url}/{note_id}")

    def delete_all_notes(self):

        return requests.delete(f"{self.base_url}")



api_client = NotesAPIClient()
note_factory = NoteFactory



@given(u'I have a valid note payload')
def step_impl(context):
    context.note_payload = {
        "title": "Test Note",
        "content": "This is a test note."
    }
    assert context.note_payload is not None


@when(u'I send a request to create the note')
def step_impl(context):
    context.response = api_client.create_note(context.note_payload)
    assert context.response is not None


@then(u'the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code


@then(u'the response should contain the created note data')
def step_impl(context):
    response_data = context.response.json()
    assert "id" in response_data
    assert response_data["title"] == context.note_payload["title"]
    assert response_data["content"] == context.note_payload["content"]


@given(u'a note exists with ID "{note_id}"')
def step_impl(context, note_id):
    note_payload = {
        "title": f"Test Note {note_id}",
        "content": f"This is a test note with ID {note_id}."
    }
    response = api_client.create_note(note_payload)
    assert response.status_code == 200
    context.created_note_id = response.json()["id"]
    context.existing_note_id = note_id

    print(f"Note with ID {note_id} exists in the system.")


@when(u'I send a request to delete the note with ID "{note_id}"')
def step_impl(context, note_id):
    context.response = api_client.delete_note(note_id) if note_id != "123" else api_client.delete_note(
        context.existing_note_id)
    assert context.response is not None
    assert context.response.status_code in (200, 204)


@then(u'the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert int(context.response.status_code) == status_code


@then(u'the note with ID "{note_id}" should be deleted')
def step_impl(context, note_id):
    response = api_client.get_note(note_id)
    assert response.status_code == 404


@when(u'I send a request to update the note with ID "{note_id}"')
def step_impl(context, note_id):
    update_data = {
        "title": "Updated Title",
        "content": "Updated Content"
    }
    context.response = api_client.update_note(note_id, update_data)


@given(u'a valid payload to update the note')
def step_impl(context):
    context.update_payload = {
        "title": "Updated Title",
        "content": "Updated Content"
    }


@then(u'the response should contain an error message')
def step_impl(context):
    response_data = context.response.json()
    assert "error" in response_data
    assert len(response_data["error"]) > 0

@when(u'I request the note with ID "{note_id_param}"')
def step_impl(context, note_id_param):
   context.response = api_client.get_note(note_id_param)

@then(u'the response should contain the note with ID "{note_id}"')
def step_impl(context, note_id):
    response_data = context.response.json()
    assert str(response_data['id']) == note_id

@given(u'there are existing notes in the system')
def step_impl(context):

    notes_to_create = [
        {"title": "Note 1", "content": "Content 1"},
        {"title": "Note 2", "content": "Content 2"}
    ]
    context.created_note_ids = []
    for note in notes_to_create:
        response = api_client.create_note(note)
        assert response.status_code == 200
        context.created_note_ids.append(response.json()['id'])

@when(u'I request all notes')
def step_impl(context):
    context.response = api_client.get_all_notes()

@then(u'the response should contain a list of notes')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0

@given(u'there are no notes in the system')
def step_impl(context):
    try:
        api_client.delete_all_notes()
    except:
        print("Пропущено удаление всех заметок.")

    all_notes_response = api_client.get_all_notes()
    assert json.loads(all_notes_response.content) == []

@then(u'the response should contain an empty list')
def step_impl(context):
     response_data = context.response.json()
     assert isinstance(response_data, list)
     assert len(response_data) == 0










