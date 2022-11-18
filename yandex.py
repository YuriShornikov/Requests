import requests

from settings import TOKEN

class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def get_files_list(self):
        uri = 'v1/disk/resources/files/'
        request_uri = self.base_host + uri
        params = {'limit': '2'}
        response = requests.get(request_uri, headers=self.get_headers(), params=params)
        print(response.json())

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_uri = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_uri, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка успешна')


if __name__ == '__main__':
    ya = Yandex(TOKEN)
    # ya.get_files_list()
    ya.upload_to_disk('hello.txt', '/hello.txt')