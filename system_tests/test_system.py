"""Selenium tests."""
from .conftest import wait_for

import pytest


def test_florian_adds_a_new_exercise(browser, live_server):
    # Florian wants to add a new exercise.
    # He starts by opening the home page,
    browser.get(live_server.url)

    # and sees that it's there.
    wait_for(lambda: browser.find_element_by_tag_name('h1'))

    # He finds the "Add new exercise" button and clicks it.
    browser.find_element_by_id('id_add_exercise').click()

    # Next, he is presented a form to create a new exercise
    wait_for(lambda: browser.find_element_by_tag_name('form'))

    # Fail the test.
    pytest.fail('Finish the test!')
