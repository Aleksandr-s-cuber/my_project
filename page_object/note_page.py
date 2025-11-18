# import requests
#
# class NotePage:
#     def __init__(self, base_url):
#         self.base_url = base_url
#
#     def create_note(self, note_data):
#         response = requests.post(f"{self.base_url}/notes", json=note_data)
#         return response
#
#     def get_all_notes(self):
#         response = requests.get(f"{self.base_url}/notes")
#         return response
#
#     def get_note_by_id(self, note_id):
#         response = requests.get(f"{self.base_url}/notes/{note_id}")
#         return response
#
#     def update_note(self, note_id, update_data):
#         response = requests.put(f"{self.base_url}/notes/{note_id}", json=update_data)
#         return response
#
#     def delete_note(self, note_id):
#         response = requests.delete(f"{self.base_url}/notes/{note_id}")
#         return response




import requests
class NotePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_note(self, note_data):
        response = requests.post(f"{self.base_url}/notes", json=note_data)
        return response

    def get_all_notes(self):
        response = requests.get(f"{self.base_url}/notes")
        return response

    def get_note_by_id(self, note_id):
        response = requests.get(f"{self.base_url}/notes/{note_id}")
        return response

    def update_note(self, note_id, update_data):
        response = requests.put(f"{self.base_url}/notes/{note_id}", json=update_data)
        return response

    def delete_note(self, note_id):
        response = requests.delete(f"{self.base_url}/notes/{note_id}")
        return response














# from behave import *
# from page_object.note_page import NotesPage  # Correct import path
# from factories.note_factory import NoteFactory  # Correct import path
# import json
#
# @given('the note payload with a valid title and content')
# def step_impl(context):
#     context.note_payload = NoteFactory.create_note()
#
# @given('the note payload with invalid data')
# def step_impl(context):
#     context.note_payload = NoteFactory.create_invalid_note()
#
# @when('I send a request to create the note')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.create_note(context.note_payload)
#
# @then('the response status code should be {status_code:d}')
# def step_impl(context, status_code):
#     assert context.response.status_code == status_code
#
# @then('the response should contain the correct title')
# def step_impl(context):
#     response_data = context.response.json()
#     assert response_data['title'] == context.note_payload['title']
#
# @when('I request all notes')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.get_notes()
#
# @then('the response should be an empty list')
# def step_impl(context):
#     assert context.response.status_code == 200
#     assert context.response.json() == []
#
# @given('at least one existing note')
# def step_impl(context):
#     # Создаем заметку через API
#     context.notes_page = NotesPage()
#     context.note_payload = NoteFactory.create_note()
#     context.response = context.notes_page.create_note(context.note_payload)
#     assert context.response.status_code == 201
#     context.created_note_id = context.response.json()['id']
#
# @then('the response should contain the existing note')
# def step_impl(context):
#     assert context.response.status_code == 200
#     notes = context.response.json()
#     assert len(notes) > 0
#
# @given('an existing note')
# def step_impl(context):
#     # Создаем заметку и сохраняем ее ID
#     context.notes_page = NotesPage()
#     context.note_payload = NoteFactory.create_note()
#     context.response = context.notes_page.create_note(context.note_payload)
#     assert context.response.status_code == 201
#     context.note_id = context.response.json()['id']
#
# @when('I request the note by its id')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.get_note_by_id(context.note_id)
#
# @then('the response should contain the correct title')
# def step_impl(context):
#     assert context.response.status_code == 200
#     response_data = context.response.json()
#     assert response_data['title'] == context.note_payload['title']
#
# @when('I request the note by an invalid id')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.get_note_by_id("invalid_id")  # Или любой невалидный ID
#
# @then('the response status code should be 404')
# def step_impl(context):
#     assert context.response.status_code == 404
#
# @when('I update the note with a new title and content')
# def step_impl(context):
#     context.new_note_payload = NoteFactory.create_note(title="Updated Title", content="Updated Content")
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.update_note(context.note_id, context.new_note_payload)
#
# @then('the response should contain the updated title')
# def step_impl(context):
#     assert context.response.status_code == 200
#     response_data = context.response.json()
#     assert response_data['title'] == context.new_note_payload['title']
#
# @when('I attempt to update a note with an invalid id')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.new_note_payload = NoteFactory.create_note(title="Updated Title", content="Updated Content")
#     context.response = context.notes_page.update_note("invalid_id", context.new_note_payload)
#
# @when('I delete the note by its id')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.delete_note(context.note_id)
#
# @then('the response status code should be 204')
# def step_impl(context):
#     assert context.response.status_code == 204
#
# @when('I attempt to delete a note with an invalid id')
# def step_impl(context):
#     context.notes_page = NotesPage()
#     context.response = context.notes_page.delete_note("invalid_id")
