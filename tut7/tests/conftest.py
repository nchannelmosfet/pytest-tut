"""
conftest.py store fixtures shared among all test suites.
Try to use conftest.py as local as possible, i.e. not in the root to avoid slowing down performance.
"""

from datetime import datetime

import pytest

from tut7.myapp.student import Student


@pytest.fixture
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe", 20)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student
