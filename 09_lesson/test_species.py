from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
import pytest

# Подключение к БД
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
        assert len(names) > 0, "В БД нет таблиц"

        print(f"Найдено таблиц: {len(names)}")

    except SQLAlchemyError as e:
        pytest.fail(f"Ошибка подключения к БД: {e}")


def test_add_species():
    """Тест на добавление вида (CREATE)"""
    test_species_name = "Test Species - Must Delete"
    test_species_type_id = 1
    test_species_id = 999999

    with db.connect() as connection:
        connection.execute(
            text("DELETE FROM species WHERE species_name = :name"),
            {"name": test_species_name}
        )
        connection.commit()

        connection.execute(
            text("INSERT INTO species (species_id, species_name, type_id) VALUES (:id, :name, :type_id)"),
            {"id": test_species_id, "name": test_species_name, "type_id": test_species_type_id}
        )
        connection.commit()

        result = connection.execute(
            text("SELECT species_name, type_id FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        row = result.first()

        assert row is not None, "Вид не был добавлен"
        assert row.species_name == test_species_name, "Название вида не совпадает"
        assert row.type_id == test_species_type_id, "type_id не совпадает"

        connection.execute(
            text("DELETE FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        connection.commit()


def test_update_species():
    """Тест на изменение вида (UPDATE)"""
    test_species_name = "Test Species Original"
    new_species_name = "Test Species Updated"
    test_species_type_id = 1
    test_species_id = 999998

    with db.connect() as connection:
        connection.execute(
            text("DELETE FROM species WHERE species_id IN (:id1, :id2)"),
            {"id1": test_species_id, "id2": test_species_id + 1}
        )
        connection.commit()

        connection.execute(
            text("INSERT INTO species (species_id, species_name, type_id) VALUES (:id, :name, :type_id)"),
            {"id": test_species_id, "name": test_species_name, "type_id": test_species_type_id}
        )
        connection.commit()

        connection.execute(
            text("UPDATE species SET species_name = :new_name WHERE species_id = :id"),
            {"new_name": new_species_name, "id": test_species_id}
        )
        connection.commit()

        result_old = connection.execute(
            text("SELECT species_name FROM species WHERE species_name = :name"),
            {"name": test_species_name}
        )
        rows_old = result_old.all()
        assert len(rows_old) == 0, "Старое название все еще существует"

        result_new = connection.execute(
            text("SELECT species_name FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        row_new = result_new.first()
        assert row_new is not None, "Вид с новым названием не найден"
        assert row_new.species_name == new_species_name, "Новое название не совпадает"

        connection.execute(
            text("DELETE FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        connection.commit()


def test_delete_species():
    """Тест на удаление вида (DELETE)"""
    test_species_name = "Test Species To Delete"
    test_species_type_id = 1
    test_species_id = 999997

    with db.connect() as connection:
        connection.execute(
            text("DELETE FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        connection.commit()

        connection.execute(
            text("INSERT INTO species (species_id, species_name, type_id) VALUES (:id, :name, :type_id)"),
            {"id": test_species_id, "name": test_species_name, "type_id": test_species_type_id}
        )
        connection.commit()

        result_before = connection.execute(
            text("SELECT species_id FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        rows_before = result_before.all()
        assert len(rows_before) == 1, "Вид не был создан перед удалением"

        connection.execute(
            text("DELETE FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        connection.commit()

        result_after = connection.execute(
            text("SELECT species_id FROM species WHERE species_id = :id"),
            {"id": test_species_id}
        )
        rows_after = result_after.all()
        assert len(rows_after) == 0, "Вид не был удален"


def test_add_place():
    """Тест на добавление места (CREATE)"""
    test_place_name = "Test Place - Must Delete"
    test_coordinates = "55.7558, 37.6173"
    test_place_id = 999999  # Вручную задаем ID, так как автоинкремента нет

    with db.connect() as connection:
        connection.execute(
            text("DELETE FROM places WHERE place_name = :name"),
            {"name": test_place_name}
        )
        connection.commit()

        # Теперь передаем place_id вручную!
        connection.execute(
            text("INSERT INTO places (place_id, place_name, coordinates) VALUES (:id, :name, :coords)"),
            {"id": test_place_id, "name": test_place_name, "coords": test_coordinates}
        )
        connection.commit()

        result = connection.execute(
            text("SELECT place_name, coordinates FROM places WHERE place_id = :id"),
            {"id": test_place_id}
        )
        row = result.first()

        assert row is not None, "Место не было добавлено"
        assert row.place_name == test_place_name, "Название места не совпадает"
        assert row.coordinates == test_coordinates, "Координаты не совпадают"

        connection.execute(
            text("DELETE FROM places WHERE place_id = :id"),
            {"id": test_place_id}
        )
        connection.commit()


