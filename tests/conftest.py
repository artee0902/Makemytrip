import pytest
import json
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def config():
    with open("config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # HEADLESS is set to "true" in GitHub Actions environment
        headless = os.getenv("HEADLESS", "true").lower() == "true"
        browser = p.webkit.launch(
            headless=headless,
            args=[
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-web-security"
            ]
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(user_agent=(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ))
    page = context.new_page()
    yield page
    context.close()
