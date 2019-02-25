import pytest
from pytest_bdd import scenario, when, given, then


@scenario("features/wall.feature", "User sees messages from friends on her own wall")
def test_user_sees_messages_from_friends_on_her_own_wall():
    pytest.fail("Not implemented")


@given("Bob posts a few messages")
def bob_posts_a_few_messages():
    pytest.fail("Not implemented")


@given("Charlie posts a few messages")
def charlie_posts_a_few_messages():
    pytest.fail("Not implemented")


@given("Charlie follows Bob")
def charlie_follows_bob():
    pytest.fail("Not implemented")


@when("Charlie checks his wall")
def charlie_checks_his_wall():
    pytest.fail("Not implemented")


@then("messages from Bob and Charlie are displayed in reverse chronological order")
def messages_from_bob_and_charlie_are_displayed_in_reverse_chronological_order():
    pytest.fail("Not implemented")
