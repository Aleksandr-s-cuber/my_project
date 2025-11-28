# import behave
# from page_object.note_page import NotePage
# from factories.note_factory import NoteFactory
#
# @behave.given('I have a valid note payload')
# def step_impl(context):
#     context.note_data = NoteFactory()
# #
# @behave.when('I send a request to create the note')
# def step_impl(context):
#     context.page = NotePage("http://127.0.0.1:8000")
#     context.response = context.page.create_note(context.note_data)
#
# @behave.then('the response status code should be {status_code:d}')
# def step_impl(context, status_code):
#     assert context.response.status_code == status_code
#
# @behave.then('the response should contain the created note data')
# def step_impl(context):
#     note = context.response.json()
#     assert note['title'] == context.note_data['title']
#     assert note['content'] == context.note_data['content']





# from behave import given, when, then
# from page_object.note_page import NotePage
# from factories.note_factory import NoteFactory
#
#
# @given('I have a valid note payload')
# def step_impl(context):
#     context.note_data = NoteFactory.create_valid()
#
#
# @given('a note payload with title "{title}" and content "{content}"')
# def step_impl(context, title, content):
#     context.note_data = {"title": title, "content": content}
#
# @given('a note payload with only content "{content}"')
# def step_impl(context, content):
#     context.note_data = {"content": content}
#
# @when('I send a request to create the note')
# def step_impl(context):
#     context.page = NotePage(context.base_url)
#     context.response = context.page.create_note(context.note_data)
#
# @then('the response status code should be {status_code:d}')
# def step_impl(context, status_code):
#     expected_status = int(status_code)
#     actual_status = context.response.status_code
#     assert actual_status == expected_status, \
#         f"Expected status code {expected_status}, but got {actual_status}. " \
#         f"Response body: {context.response.text}"
#
# @then('the response should contain the created note data')
# def step_impl(context):
#     response_json = context.response.json()
#     assert response_json['title'] == context.note_data['title'], \
#         f"Expected title '{context.note_data['title']}', but got '{response_json['title']}'"
#     assert response_json['content'] == context.note_data['content'], \
#         f"Expected content '{context.note_data['content']}', but got '{response_json['content']}'"
#
# @then('the response should contain the correct title')
# def step_impl(context):
#     response_json = context.response.json()
#     assert response_json['title'] == context.note_data['title'], \
#         f"Expected title '{context.note_data['title']}', but got '{response_json['title']}'"
#
# @then('the response should contain the correct content')
# def step_impl(context):
#     response_json = context.response.json()
#     assert response_json['content'] == context.note_data['content'], \
#         f"Expected content '{context.note_data['content']}', but got '{response_json['content']}'"
#
# @then('the response should contain an error message')
# def step_impl(context):
#     response_json = context.response.json()
#     assert 'message' in response_json or 'error' in response_json, \
#         f"Response did not contain an error message. Response: {response_json}"



from behave import *
import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

@given('a note payload with title "{title}" and content "{content}"')
def step_impl(context, title, content):
    context.payload = {"title": title, "content": content}

@given('a note payload with only content "{content}"')
def step_impl(context, content):
    context.payload = {"content": content}


@when('I send a request to create the note')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/notes/", json=context.payload)

    try:
        context.response_json = context.response.json()  #
    except json.decoder.JSONDecodeError:
        context.response_json = None


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code


@then('the response should contain the correct title "{title}"')
def step_impl(context, title):
    assert context.response_json["title"] == title


@then('the response should contain the correct content "{content}"')
def step_impl(context, content):
    assert context.response_json["content"] == content


@then('the response should contain an id')
def step_impl(context):
    assert "id" in context.response_json


@then('the response should contain an error message')
def step_impl(context):
    assert "detail" in context.response_json # FastAPI default











