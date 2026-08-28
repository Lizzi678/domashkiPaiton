import pytest
import requests


#ТЕСТЫ ДЛЯ МЕТОДА [POST] /api-v2/projects


def test_create_project_positive(base_url, headers):
  #Позитивный тест: успешное создание проекта.
  data = {"title": "My New Project"}
  response = requests.post(f"{base_url}/projects", json=data, headers=headers)

  assert response.status_code == 201
  assert "id" in response.json()


def test_create_project_negative(base_url, headers):
  #Негативный тест: создание проекта без обязательных данных.
  data = {"title": ""}
  response = requests.post(f"{base_url}/projects", json=data, headers=headers)

  assert response.status_code in [400, 422]


#ТЕСТЫ ДЛЯ МЕТОДА [GET] /api-v2/projects/{id}


def test_get_project_positive(base_url, headers, created_project):
  #Позитивный тест: получение существующего проекта по ID.
  project_id = created_project
  response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)

  assert response.status_code == 200
  assert response.json().get("id") == project_id


def test_get_project_negative(base_url, headers):
  #Негативный тест: получение проекта с несуществующим ID.
  fake_id = "00000000-0000-0000-0000-000000000000"
  response = requests.get(f"{base_url}/projects/{fake_id}", headers=headers)

  assert response.status_code == 404


#ТЕСТЫ ДЛЯ МЕТОДА [PUT] /api-v2/projects/{id}


def test_update_project_positive(base_url, headers, created_project):
  #Позитивный тест: обновление существующего проекта.
  project_id = created_project
  data = {"title": "Updated Project Title"}
  response = requests.put(
      f"{base_url}/projects/{project_id}", json=data, headers=headers
  )

  assert response.status_code == 200
  assert response.json().get("id") == project_id


def test_update_project_negative(base_url, headers):
  #Негативный тест: обновление несуществующего проекта.
  fake_id = "00000000-0000-0000-0000-000000000000"
  data = {"title": "Hacker Project"}
  response = requests.put(
      f"{base_url}/projects/{fake_id}", json=data, headers=headers
  )

  assert response.status_code in [400, 404]

if __name__ == "__main__":
  pytest.main(["-v", __file__])