import pytest
import json
import os
from playwright.sync_api import sync_playwright

# Fixture to load config.json (works in local + GitHub Actions)
@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        return json.load(f)

# Fixture to launch Playwright browser
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# Fixture to create a new page for each test
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
