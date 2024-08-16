# conftest.py

import pytest
import requests
from config import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def session():
    return requests.Session()
