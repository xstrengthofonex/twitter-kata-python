from pytest_bdd import scenario, when, given, then


@scenario("features/wall.feature", "User sees messages from friends on her own wall")
def test_user_sees_messages_from_friends_on_her_own_wall():
    pass


@given("Bob posts a few messages")
def bob_posts_a_few_messages():
    pass


@given("Charlie posts a few messages")
def charlie_posts_a_few_messages():
    pass


@given("Charlie follows Bob")
def charlie_follows_bob():
    pass


@when("Charlie checks his wall")
def charlie_checks_his_wall():
    pass


@then("messages from Bob and Charlie are displayed in reverse chronological order")
def messages_from_bob_and_charlie_are_displayed_in_reverse_chronological_order():
    pass
