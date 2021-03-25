import csv
from pathlib import Path
from helpers.csv import reset_file_from_path

from domain.ports.user import User
from adapters.csv_user_repository import CsvUserRepository

csv_path = Path("tests/integration/data") / "user_repo.csv"
user_example = User(name="patrice", status="contact", uuid="pat_uuid")


def test_can_add_user():
    reset_file_from_path(csv_path)
    csv_user_repository = CsvUserRepository(csv_path=csv_path)
    csv_user_repository.add(user_example)
    with csv_path.open("r") as f:
        reader = csv.DictReader(f)
        assert list(reader)[0] == {
            "uuid": "pat_uuid",
            "name": "patrice",
            "status": "contact",
        }


def test_can_get_user_if_exists():
    reset_file_from_path(csv_path)
    csv_user_repository = CsvUserRepository(csv_path=csv_path)
    csv_user_repository.add(user_example)
    assert csv_user_repository.get(uuid="pat_uuid") == user_example