import pytest
from selene import browser

@pytest.fixture(autouse=True)
def init_browser():
    browser.config.window_width = 720
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()