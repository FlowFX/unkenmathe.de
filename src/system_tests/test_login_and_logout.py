"""Functional test for login and logout pages."""
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

import pytest

from .conftest import assert_regex, wait_for, wait_for_true


def test_login_of_anonymous_user(live_server, anon_browser, user):
    browser = anon_browser

    # Open the home page
    browser.get(live_server.url)

    # There is a login link
    wait_for(lambda: browser.find_element_by_id('id_link_to_login'))

    # but no logout
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_id('id_link_to_logout')

    # open the LOGIN modal
    browser.find_element_by_id('id_link_to_login').click()
    time.sleep(0.5)

    # enter credentials
    browser.find_element_by_id('id_login').send_keys('test@example.com')
    browser.find_element_by_id('id_password').send_keys('password')

    # click "Go!"
    browser.find_element_by_id('submit-id-login').click()

    # and wait for the home page with the logout link
    wait_for(lambda: browser.find_element_by_id('id_link_to_logout'))

    # but no login
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_id('id_link_to_login')
    assert_regex(browser.current_url, '.+/')


def test_logout_of_authenticated_user(browser, live_server):
    # WHEN getting the home page
    browser.get(live_server.url)

    # THEN there is a logout link
    wait_for(lambda: browser.find_element_by_id('id_link_to_logout'))

    # On mobile, the menu is hidden
    if not browser.find_element_by_id('id_link_to_logout').is_displayed():
        try:
            browser.find_element_by_class_name('navbar-toggler').click()
            time.sleep(0.5)
        except ElementNotVisibleException:
            pass

    # Open the Account dropdown.
    browser.find_element_by_id('navbarDropdownAccountMenu').click()
    time.sleep(0.5)

    # Open the LOGOUT modal,
    browser.find_element_by_id('id_link_to_logout').click()
    time.sleep(0.5)

    # confirm the logout,
    browser.find_element_by_id('submit-id-confirm-logout').click()

    # and wait for the login page
    wait_for(lambda: browser.find_element_by_id('id_link_to_login'))
