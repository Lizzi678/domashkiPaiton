import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture
def base_url():
  return BASE_URL


@pytest.fixture
def auth_token():
  # Наставнику: замените 'YOUR_TOKEN' на ваш актуальный токен Yougile перед запуском
  return "YOUR_TOKEN"


@pytest.fixture
def company_id():
  # Наставнику: замените 'YOUR_COMPANY_ID' на ваш ID компании перед запуском
  return "YOUR_COMPANY_ID"


@pytest.fixture
def headers(auth_token):
  return {
      "Authorization": f"Bearer {auth_token}",
      "Content-Type": "application/json",
  }


@pytest.fixture
def created_project(base_url, headers):
  #Фикстура создает тестовый проект для GET и PUT запросов
  data = {"title": "Temporary Project for Test"}
  response = requests.post(f"{base_url}/projects", json=data, headers=headers)
  project_id = response.json().get("id")
  yield project_id