import requests
import json
print('Задание 1')
url = 'https://akabab.github.io/superhero-api/api/all.json'
res = requests.get(url)
heroes = res.json()
coolest_heroes = {}
for hero in heroes:
    if hero['name'] in ['Hulk','Captain America', 'Thanos']:
        coolest_heroes = {hero['name']:hero['powerstats']['intelligence']}
        print(coolest_heroes)


print(max(coolest_heroes, key=coolest_heroes.get))

print('Задание 2')

My_token = 'y0_AgAAAABe-gmCAADLWwAAAADSa_7eCtVzTHroQjCmXjGX-gvwepPsGGQ'
class YaUploader:
    def __init__(self, token):
        self.token = token
        self.host = 'https://cloud-api.yandex.net:443'

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files'
        headers = self.get_headers()
        response= requests.get(url, headers=headers)
        print(response.json())

    def upload(self, path, file_name):
        upload_link = 'D:\кодики\jajaj' #путь до файла на моем ПК
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    yauploader = YaUploader(My_token)
    yauploader.upload('test.txt')


