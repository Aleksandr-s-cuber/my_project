# import factory
# import uuid
# from faker import Faker

# fake = Faker()
#
# class NoteFactory(factory.Factory):
#     class Meta:
#         model = dict
#
#     title = factory.Faker('sentence', nb_words=4)
#     content = factory.Faker('text', max_nb_chars=200)
#
#     @staticmethod
#     def with_empty_title():
#         return {"title": "", "content": fake.text()}
#
#     @staticmethod
#     def with_empty_content():
#         return {"title": fake.sentence(), "content": ""}
#
#     @staticmethod
#     def with_invalid_data():
#         return {"title": None, "content": None}
#
#
#
#     @classmethod
#     def create_notes(cls, count):
#         return [cls.build() for _ in range(count)]
#
#
#
#     @classmethod
#     def valid_update_data(cls):
#         return {"title": fake.sentence(nb_words=5), "content": fake.text(max_nb_chars=150)}
#
#     @classmethod
#     def invalid_update_data(cls):
#         return {"title": "", "content": fake.text(max_nb_chars=100)}
#
#
#
#     @staticmethod
#     def generate_valid_id():
#         return str(uuid.uuid4())
#
#     @staticmethod
#     def generate_invalid_id():
#         return "invalid-id"

#
# import factory
# import uuid
# from faker import Faker
#
#
#
#
# class NoteFactory(factory.DictFactory):
#     class Meta:
#         model = dict
#
#     title = factory.Faker('sentence', nb_words=4)
#     content = factory.Faker('paragraph', nb_sentences=3)
#
#     @classmethod
#     def build(cls, **kwargs):
#
#
#
#         return factory.build(dict, FACTORY_CLASS=cls, **kwargs)
#     @classmethod
#     def with_empty_title(cls):
#         return cls.build(title="")
#
#     @classmethod
#     def with_empty_content(cls):
#         return cls.build(content="")
#
#     @classmethod
#     def with_long_title(cls, length=100):
#          return cls.build(title=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))
#
#
#     @classmethod
#     def with_long_content(cls, length=500):
#         return cls.build(content=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))
#
#
#     @classmethod
#     def with_invalid_data(cls):
#         return cls.build(title=None, content=123)  # Invalid types
#
#
#     @classmethod
#     def valid_update_data(cls):
#         return {"title": "Updated Title", "content": "Updated content"}
#
#     @classmethod
#     def invalid_update_data(cls):
#         return {"title": "", "content": "Valid content"}
#
#     @classmethod
#     def generate_invalid_id(cls):
#         return 99999
#
#
#     @classmethod
#     def build_note_dict(cls, **kwargs):
#         note_dict = cls.build(**kwargs)
#         return note_dict
#
#
#
# if __name__ == '__main__':
#     valid_note = NoteFactory.build()
#     print("Valid Note:", valid_note)
#
#     empty_title_note = NoteFactory.with_empty_title()
#     print("Empty Title Note:", empty_title_note)
#
#     long_title_note = NoteFactory.with_long_title(length=200)
#     print("Long Title Note:", len(long_title_note['title']))
#
#     invalid_note = NoteFactory.with_invalid_data()
#     print("Invalid Note:", invalid_note)
#
#     update_data = NoteFactory.valid_update_data()
#     print("Update Data:", update_data)





# import factory
# import uuid
# from faker import Faker
# import secrets
# import string
#
# fake = Faker()
#
# class NoteFactory(factory.DictFactory):
#     class Meta:
#         model = dict
#
#
#     title = factory.LazyFunction(lambda: fake.sentence(nb_words=4))
#     content = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
#
#
#     @classmethod
#     def create_valid(cls):
#         """Создает и возвращает словарь с валидными данными заметки."""
#         return cls.build()
#
#     @classmethod
#     def with_empty_title(cls):
#         return cls.build(title="")
#
#     @classmethod
#     def with_empty_content(cls):
#         return cls.build(content="")
#
#     @classmethod
#     def with_long_title(cls, length=100):
#         return cls.build(title=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))
#
#     @classmethod
#     def with_long_content(cls, length=500):
#         return cls.build(content=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))
#
#     @classmethod
#     def with_invalid_data(cls):
#         # В DictFactory вы можете напрямую указать значения различных типов
#         # Flask API может вернуть 400 при таком виде данных
#         return cls.build(title=None, content=123)
#
#     @classmethod
#     def valid_update_data(cls):
#         return {"title": "Updated Title", "content": "Updated content"}
#
#     @classmethod
#     def invalid_update_data(cls):
#         return {"title": "", "content": "Valid content"} # Пример невалидного обновления
#
#     @classmethod
#     def generate_invalid_id(cls):
#         return str(uuid.uuid4()) # Лучше использовать строку, если ID в API - UUID
#
#
# if __name__ == '__main__':
#     valid_note = NoteFactory.create_valid()
#     print("Valid Note:", valid_note)



from behave import *
import requests
import json

BASE_URL = "http://localhost:8000"


def create_note(title, content):
    payload = {"title": title, "content": content}
    response = requests.post(f"{BASE_URL}/notes/", json=payload)
    return response.json()["id"]  # Return the created note ID


def delete_note(note_id):
    requests.delete(f"{BASE_URL}/notes/{note_id}")


@given('a note exists with ID "{note_id}"')
def step_impl(context, note_id):
  context.note_id = create_note(title="Test Note", content="Test Content")

  assert context.note_id is not None, "Failed to create a test note"

  context.add_cleanup(delete_note, context.note_id)


@when('I send a request to delete the note with ID "{note_id}"')
def step_impl(context, note_id):
    context.response = requests.delete(f"{BASE_URL}/notes/{note_id}")


@then('the note with ID "{note_id}" should be deleted')
def step_impl(context,note_id):
    response = requests.get(f"{BASE_URL}/notes/{note_id}")
    assert response.status_code == 404, "Note was not deleted"








