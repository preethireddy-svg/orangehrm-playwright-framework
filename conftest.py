import pytest
import os
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader
from datetime import datetime


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as p:
        browser_type = config.get("browser")

        if browser_type == "chromium":
            browser = p.chromium.launch(headless=config.get("headless"))
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=config.get("headless"))
        else:
            browser = p.webkit.launch(headless=config.get("headless"))

        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()

        # code for auto screen shot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name

            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            page.screenshot(path=screenshot_path)

            print(f"\n📸 Screenshot saved: {screenshot_path}")