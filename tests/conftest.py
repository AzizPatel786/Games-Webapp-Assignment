import pytest
from games import create_app
from games.adapters import memory_repository
from games.adapters.memory_repository import MemoryRepository, populate
from games.adapters import repository
from pathlib import Path
from games.adapters.repository import AbstractRepository

TEST_DATA_PATH = Path('tests')/ 'test_data'


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    populate(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,
        'TEST_DATA_PATH': TEST_DATA_PATH,
        'WTF_CSRF_ENABLED': False
    })

    return my_app.test_client()