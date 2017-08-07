"""Selenium tests."""
from .conftest import wait_for


def test_home_page(live_server, browser):
    # GIVEN any state
    # WHEN calling the home page
    browser.get(live_server.url)

    # THEN it's there
    wait_for(lambda: browser.find_element_by_tag_name('h1'))
