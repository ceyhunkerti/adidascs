from datetime import datetime
from pytest import fixture
from adidascs import __version__
from adidascs.arguments import get_arguments


def pytest_addoption(parser):
    parser.addoption("--page_types", action="store")


def test_version():
    assert __version__ == "0.1.0"


def test_page_types(page_types):
    assert len(page_types) > 0


def test_metric_types(metric_types):
    assert len(metric_types) > 0
    for m in metric_types:
        assert m in ["fe", "dur"]


def test_time_windows(time_windows):
    assert len(time_windows) > 0


def test_ref_date(ref_date):
    assert datetime.strptime(ref_date, "%Y.%m.%d")