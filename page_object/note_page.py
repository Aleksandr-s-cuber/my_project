
# import requests
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
import json

class NotePage:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/notes" # Предполагаем, что endpoint для заметок - /notes

    def _request(self, method, url_suffix="", data=None, json_data=None):
        url = f"{self.base_url}{url_suffix}"
        headers = {'Content-Type': 'application/json'}
        try:
            if method == 'GET':
                return requests.get(url, headers=headers)
            elif method == 'POST':
                return requests.post(url, headers=headers, json=json_data if json_data else data)
            elif method == 'PUT':
                return requests.put(url, headers=headers, json=json_data if json_data else data)
            elif method == 'DELETE':
                return requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
        except requests.exceptions.ConnectionError as e:
            # Улучшенное сообщение об ошибке для ConnectionError
            raise ConnectionError(f"Failed to connect to API at {url}. "
                                  f"Is the Flask/Other API running on {self.base_url.split('/notes')[0]}? Error: {e}")
        except requests.exceptions.HTTPError as e:
            # Обработка HTTP ошибок (4xx, 5xx)
            print(f"HTTP Error for {method} {url}: {e.response.status_code} - {e.response.text}")
            return e.response # Возвращаем объект response для дальнейшей проверки в then-шагах
        except Exception as e:
            print(f"An unexpected error occurred during request to {url}: {e}")
            raise


    def create_note(self, note_data_factory_instance):
        return self._request('POST', json_data=note_data_factory_instance.to_dict())

    def get_note(self, note_id):
        return self._request('GET', url_suffix=f"/{note_id}")

    def get_all_notes(self):
        return self._request('GET')

    def update_note(self, note_id, update_data_factory_instance):
        return self._request('PUT', url_suffix=f"/{note_id}", json_data=update_data_factory_instance.to_dict())

    def delete_note(self, note_id):
        return self._request('DELETE', url_suffix=f"/{note_id}")













