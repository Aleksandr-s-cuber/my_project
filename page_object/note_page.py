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
