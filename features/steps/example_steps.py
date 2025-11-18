from behave import given, when, then
from page_object.note_page import NotePage
from factories.note_factory import NoteFactory

@given('I have a valid note payload')
def step_impl(context):
    context.note_data = NoteFactory()
#
@when('I send a request to create the note')
def step_impl(context):
    context.page = NotePage("http://127.0.0.1:8000")
    context.response = context.page.create_note(context.note_data)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain the created note data')
def step_impl(context):
    note = context.response.json()
    assert note['title'] == context.note_data['title']
    assert note['content'] == context.note_data['content']













