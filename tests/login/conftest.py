import pytest


@pytest.fixture(scope='function')
def user_login_fixture(page_manager):
    yield page_manager
