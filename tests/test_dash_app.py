import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app():
    app = import_app("dash_app")
    return app

def test_header_is_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Analysis"

def test_visualisation_is_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_is_present(dash_duo, app):
    dash_duo.start_server(app)
    dropdown = dash_duo.find_element("#region-dropdown")
    assert dropdown is not None
