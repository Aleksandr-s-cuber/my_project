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


import factory
import uuid
from faker import Faker




class NoteFactory(factory.DictFactory):
    class Meta:
        model = dict

    title = factory.Faker('sentence', nb_words=4)  # Faker создаст случайные заголовки
    content = factory.Faker('paragraph', nb_sentences=3)  # Faker создаст случайное содержимое

    @classmethod
    def build(cls, **kwargs):



        return factory.build(dict, FACTORY_CLASS=cls, **kwargs)
    @classmethod
    def with_empty_title(cls):
        return cls.build(title="")

    @classmethod
    def with_empty_content(cls):
        return cls.build(content="")

    @classmethod
    def with_long_title(cls, length=100):
         return cls.build(title=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))


    @classmethod
    def with_long_content(cls, length=500):
        return cls.build(content=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)))


    @classmethod
    def with_invalid_data(cls):
        return cls.build(title=None, content=123)  # Invalid types


    @classmethod
    def valid_update_data(cls):
        return {"title": "Updated Title", "content": "Updated content"}

    @classmethod
    def invalid_update_data(cls):
        return {"title": "", "content": "Valid content"}

    @classmethod
    def generate_invalid_id(cls):
        return 99999  # Should be an ID that doesn't exist in your database


    @classmethod
    def build_note_dict(cls, **kwargs):
        note_dict = cls.build(**kwargs)
        return note_dict



if __name__ == '__main__':
    valid_note = NoteFactory.build()
    print("Valid Note:", valid_note)

    empty_title_note = NoteFactory.with_empty_title()
    print("Empty Title Note:", empty_title_note)

    long_title_note = NoteFactory.with_long_title(length=200)
    print("Long Title Note:", len(long_title_note['title']))

    invalid_note = NoteFactory.with_invalid_data()
    print("Invalid Note:", invalid_note)

    update_data = NoteFactory.valid_update_data()
    print("Update Data:", update_data)














