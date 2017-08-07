"""Selenium tests."""
from .conftest import assert_regex, wait_for


def test_florian_adds_a_new_exercise(browser, live_server):
    # Florian wants to add a new exercise.
    # He starts by opening the home page,
    browser.get(live_server.url)

    # and sees that it's there.
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))

    # He finds the "Add new exercise" button and clicks it.
    browser.find_element_by_id('id_add_exercise').click()

    # Next, he is presented a form to create a new exercise
    wait_for(lambda: browser.find_element_by_tag_name('form'))
    assert_regex(browser.current_url, '.+/new')

    # He enters a simple exercise into the text area,
    browser.find_element_by_id('id_text').send_keys('What is 5 + 4?')

    # and clicks the submit button.
    browser.find_element_by_id('id_submit').click()

    # Then, he gets back to the home page,
    wait_for(lambda: browser.find_element_by_id('id_add_exercise'))
    assert_regex(browser.current_url, '.+/')

    # and the new exercise is displayed there.
    assert 'What is 5 + 4?' in browser.page_source
