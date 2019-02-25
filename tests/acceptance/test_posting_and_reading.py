from pytest_bdd import scenario, given, when, then


@scenario("features/posting_and_reading.feature", "Reading posts from a user")
def test_reading_posts_from_a_user():
    pass


@given("Alice posts a few messages")
def alice_posts_a_few_messages():
    pass


@when("Bob reads Alice's messages")
def bob_reads_alice_s_messages():
    pass


@then("Alice's messages are displayed in reverse chronological order")
def alice_s_messages_are_displayed_in_reverse_chronological_order():
    pass

