from pytest_bdd import scenario, given, when, then


@scenario("features/posting_and_reading.feature", "Reading posts from a user")
def test_reading_posts_from_a_user():
    pass


@given("Alice posts a few messages")
def alice_posts_a_few_messages(twitter_console):
    twitter_console.receives("Alice -> Hello, my name is Alice")
    twitter_console.receives("Alice -> It's a lovely day today")


@when("Bob reads Alice's messages")
def bob_reads_alice_s_messages(twitter_console):
    twitter_console.receives("Alice")


@then("Alice's messages are displayed in reverse chronological order")
def alice_s_messages_are_displayed_in_reverse_chronological_order(twitter_console):
    output = twitter_console.output()
    expected = "Alice - It's a lovely day today \n" \
               "Alice - Hello, my name is Alice \n" \
               "bye!"
    assert output == expected

