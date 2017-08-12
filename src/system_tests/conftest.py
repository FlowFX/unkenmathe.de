"""Fixtures for Selenium tests."""
import re
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import pytest


MAX_WAIT = 10


def assert_regex(text: str, regex: str):
    """Assert regular expression match."""
    text = str(text)
    p = re.compile(regex)
    m = p.match(text)

    assert m is not None, text + " does not match " + regex


def wait_for(fn):
    """Explicit wait helper function for Selenium functional tests."""
    start_time = time.time()
    while True:
        try:
            return fn()
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)


@pytest.fixture(scope="session")
def browser():
    """Provide a selenium webdriver instance.

    Use headless Chrome browser.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    browser_ = webdriver.Chrome(chrome_options=options)

    yield browser_

    browser_.quit()
