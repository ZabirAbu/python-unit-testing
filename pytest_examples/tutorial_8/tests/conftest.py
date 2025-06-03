from datetime import datetime

import pytest

from tutorial_8.myapp.student import Student


@pytest.fixture
def dummy_student(request):
    return Student("Mike", datetime(2010, 1, 1), "coe", request.param)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2010, 1, 1), "coe", credits)

    return _make_dummy_student
