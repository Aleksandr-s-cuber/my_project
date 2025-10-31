import factory
import uuid
from faker import Faker

fake = Faker()

class NoteFactory(factory.Factory):
    class Meta:
        model = dict

    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker('text', max_nb_chars=200)

    @staticmethod
    def with_empty_title():
        return {"title": "", "content": fake.text()}

    @staticmethod
    def with_empty_content():
        return {"title": fake.sentence(), "content": ""}

    @staticmethod
    def with_invalid_data():
        return {"title": None, "content": None}
