from habr import get_result
import time
import pytest
import requests
from uuid import uuid4


URL = 'https://habr.com/ru/search/?q='

for query in ['new', 'Photoshop', 'switches']:
    params = {
        'q': query,
        }

@pytest.fixture
def things(params):
    return {
        query
    }

# @pytest.fixture
# def temp_folder():
#     """Генерирует уникальное имя папки"""
#     return f"test-folder-{uuid4()}"
#
# @pytest.fixture
# def create_and_cleanup_folder(things, temp_folder):
#     """Создаёт папку и удаляет её после теста"""
#     folder_path = f"disk:/{temp_folder}"
#     # Создание
#     res = requests.get(URL, headers=things, params={'path': folder_path})
#     time.sleep(0.3)
#     assert res.status_code in [201, 409], f"Ошибка при создании: {res.text}"
#
#     yield temp_folder  # передаём управление в тест
#
#     # Удаление после теста
#     requests.delete(URL, headers=things, params={'path': folder_path, 'permanently': 'true'})
#
# def test_create_folder_success(things, temp_folder):
#     res = requests.put(URL, headers=things, params={'path': f'disk:/{temp_folder}'})
#     assert res.status_code in [201, 409]
#
#
# def test_create_existing_folder(create_and_cleanup_folder):
#     folder = create_and_cleanup_folder
#     res = requests.put(URL, params={'path': {folder}})
#     assert res.status_code == 409
#
#
# def test_create_folder_invalid_path(folder_path):
#     res = requests.put(URL, params={'path': {folder_path}})
#     assert res.status_code == 404
#     requests.delete(URL, params={'path': folder_path, 'permanently': 'true'})