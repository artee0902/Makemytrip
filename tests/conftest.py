import pytest
import json
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def config():
    with open("../config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
