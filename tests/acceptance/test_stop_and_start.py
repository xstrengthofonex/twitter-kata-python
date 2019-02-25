from pytest_bdd import scenario, given, then


@scenario("features/stop_and_start.feature", "Terminate on exit command")
def test_terminate_on_exit_command():
    pass


@given("the application receives an 'exit' command")
def application_receives_an_exit_command(twitter_console):
    twitter_console.receives("Some user command")
    twitter_console.receives("exit")


@then("the application should terminate")
def the_application_should_terminate(twitter_console):
    output = twitter_console.output()
    expected = "bye!"
    assert output == expected

