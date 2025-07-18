import pytest
import json
import os
from playwright.sync_api import sync_playwright

# Load configuration from JSON
@pytest.fixture(scope="session")
def config():
    with open("config.json") as f:
        return json.load(f)

# Launch browser for the test session
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        headless = os.getenv("HEADLESS", "true").lower() == "true"
        browser = p.webkit.launch(headless=headless)
        yield browser
        browser.close()

# Create a new page for each test
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
