import pytest

from tut2.myapp.sample import validate_age


def test_validate_age_valid_age():
    validate_age(10)


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)


def test_validate_age_invalid_age_verbose():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    assert str(exc_info.value) == 'Age cannot be less than 0'
