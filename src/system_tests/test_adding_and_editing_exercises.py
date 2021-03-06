"""Selenium tests."""
from .conftest import assert_regex, wait_for, wait_for_true

from selenium.common.exceptions import NoSuchElementException

from um.exercises.factories import ExerciseFactory

import pytest

import time


def test_florian_adds_a_new_exercise(browser, live_server):
    # Florian wants to add a new exercise.
    # He starts by opening the home page,
    browser.get(live_server.url)

    # and sees that it's there.
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))

    # He finds the "Plus" navbar menu and clicks it.
    browser.find_element_by_id('navbarDropdownPlusMenu').click()
    time.sleep(0.5)
    # There is the the "Add new exercise" button.
    browser.find_element_by_id('id_add_exercise').click()

    # Next, he is presented a form to create a new exercise
    wait_for(lambda: browser.find_element_by_tag_name('form'))
    assert_regex(browser.current_url, '.+/new')

    # He enters a simple exercise into the text area,
    browser.find_element_by_id('id_text').send_keys('What is 5 + 4?')

    # and clicks the submit button.
    browser.find_element_by_id('submit-id-submit').click()

    # Then, he gets back to the home page,
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))
    assert_regex(browser.current_url, '.+/')

    # and the new exercise is displayed there.
    assert 'What is 5 + 4?' in browser.page_source


def test_user_edits_an_exercise(browser, live_server, user):
    # GIVEN an existing exercise
    ex = ExerciseFactory.create(author=user)

    # Florian goes to the home page and wants to edit this exercise
    browser.get(live_server.url)

    # and sees that it's there.
    wait_for(lambda: browser.find_element_by_id(f'id_edit_{ex.id}'))

    # He clicks the Edit button,
    browser.find_element_by_id(f'id_edit_{ex.id}').click()

    # and gets to the update form.
    wait_for(lambda: browser.find_element_by_tag_name('form'))
    assert_regex(browser.current_url, f'.+/{ex.id}/edit')

    # He replaces the exercise text,
    textarea = browser.find_element_by_id('id_text')
    textarea.clear()
    textarea.send_keys('This exercise isn\'t good enough. \( 5 + 4 = 9 \).')

    # and clicks submit.
    browser.find_element_by_id('submit-id-submit').click()

    # Then, he gets back to the home page,
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))
    assert_regex(browser.current_url, '.+/')

    # and the new text is displayed.
    assert 'This exercise ' in browser.page_source


def test_anonymous_user_views_an_exercise(anon_browser, live_server):
    browser = anon_browser

    # GIVEN an existing exercise
    ex = ExerciseFactory.create()

    # Florian goes to the home page and wants to inspect the exercise,
    browser.get(live_server.url)

    # sees that it's there.
    wait_for(lambda: browser.find_element_by_id(f'id_detail_{ex.id}'))

    # He clicks the Details button,
    browser.find_element_by_id(f'id_detail_{ex.id}').click()

    # and gets to the detail view.
    wait_for(lambda: browser.find_element_by_id('id_text'))
    assert_regex(browser.current_url, f'.+/{ex.id}/')

    # He clicks the `back` button.
    browser.find_element_by_id('back-id-back').click()

    # Then, he gets back to the home page,
    assert_regex(browser.current_url, '.+/')


def test_florian_deletes_an_exercise(browser, live_server, user):
    # GIVEN an existing exercise
    ex = ExerciseFactory.create(author=user)

    # Florian goes to the home page and wants to delete this exercise
    browser.get(live_server.url)

    # and sees that it's there.
    wait_for(lambda: browser.find_element_by_id(f'id_detail_{ex.id}'))

    # He clicks the View button,
    browser.find_element_by_id(f'id_detail_{ex.id}').click()

    # and gets to the detail view
    wait_for(lambda: browser.find_element_by_id(f'id_delete_{ex.id}'))
    assert_regex(browser.current_url, f'.+/{ex.id}/')

    # He clicks the "Delete" button
    browser.find_element_by_id(f'id_delete_{ex.id}').click()
    # let the modal pop up
    time.sleep(0.5)

    # And confirms the deletion
    browser.find_element_by_id('submit-id-submit').click()


    # Then, he gets back to the home page,
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))
    assert_regex(browser.current_url, '.+/')

    # and the exercise is gone.
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_id(f'id_detail_{ex.id}')
