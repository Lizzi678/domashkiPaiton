from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
import pytest

db_connection_string = "postgresql://postgres:1234@localhost:5432/ecology_project"
db = create_engine(db_connection_string)


def test_db_connection():
    """Тест подключения к БД и получения списка таблиц"""
    try:
        inspector = inspect(db)
        names = inspector.get_table_names()
        print(f"Таблицы в БД: {names}")

        assert names is not None, "Не удалось получить список таблиц"
        assert isinstance(names, list), "Список таблиц должен быть списком"

        print(f"Найдено таблиц: {len(names)}")

    except SQLAlchemyError as e:
        pytest.fail(f"Ошибка подключения к БД: {e}")
def test_add_user():
    """Тест на добавление пользователя без mappings()."""
    test_email = "testuser@example.com"
    test_subject_id = 1

    with db.connect() as connection:
        # Добавляем тестового пользователя
        connection.execute(
            text("INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"),
            {"email": test_email, "subject_id": test_subject_id}
        )
        connection.commit()

        # Проверяем, что пользователь добавился
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email}
        )
        rows = result.all()  # без mappings()

        # Доступ по индексам (нужно знать порядок колонок в таблице)
        # Предположим: 0 - user_id, 1 - user_email, 2 - subject_id
        assert len(rows) == 1, "Пользователь не был добавлен"
        assert rows[0][1] == test_email, "Email не совпадает"
        assert rows[0][2] == test_subject_id, "subject_id не совпадает"

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": test_email}
        )
        connection.commit()

if __name__ == "__main__":
    test_db_connection()

