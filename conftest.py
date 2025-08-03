import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "channel": "chrome",
        "timeout": 5000
    }

@pytest.fixture
def base_url():
    return "https://reqres.in"