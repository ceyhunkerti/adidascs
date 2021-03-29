import pytest


def pytest_addoption(parser):
    parser.addoption("--page_types", action="store")
    parser.addoption("--metric_types", action="store")
    parser.addoption("--time_windows", action="store")
    parser.addoption("--ref_date", action="store")


@pytest.fixture(scope="session")
def page_types(request):
    value = request.config.option.page_types
    if value is None:
        pytest.skip()
    return value


@pytest.fixture(scope="session")
def ref_date(request):
    value = request.config.option.ref_date
    if value is None:
        pytest.skip()
    return value