import os

import pytest
from starlette.testclient import TestClient

from api import main
from api.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, environment="dev")


@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
