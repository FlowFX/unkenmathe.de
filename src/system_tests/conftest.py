"""Fixtures for Selenium tests."""
import re
import time

from django.contrib.auth.hashers import make_password

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from um.core.factories import UserFactory

import pytest


MAX_WAIT = 10

TESTUSER = 'Test User'
TESTEMAIL = 'test@example.com'
TESTPASSWORD = 'password'


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
def anon_browser():
    """Provide a selenium webdriver instance.

    Use headless Chrome browser.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')

    browser_ = webdriver.Chrome(chrome_options=options)

    yield browser_

    browser_.quit()


@pytest.fixture()
def user(db):
    """Add a test user to the database."""
    user_ = UserFactory.create(
        name=TESTUSER,
        email=TESTEMAIL,
        password=make_password(TESTPASSWORD),
    )

    return user_


@pytest.fixture()
def browser(anon_browser, client, live_server, user):  # pylint: disable=redefined-outer-name
    """Return a browser instance with logged-in user session."""
    browser = anon_browser
    client.login(email=TESTEMAIL, password=TESTPASSWORD)
    cookie = client.cookies['sessionid']

    browser.get(live_server.url)  # selenium will set cookie domain based on current page domain
    browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    browser.refresh()  # need to update page for logged in user

    return browser
