import pytest

@pytest.fixture
def invalid_body():
    return {
        "name": "Tomek",
        "surname": "M",
        "amount": 0,
    }


@pytest.fixture
def valid_body(invalid_body):
    valid_body = invalid_body.copy()
    valid_body["login"] = "TM"
    valid_body["password"] = "haslo"
    return valid_body
