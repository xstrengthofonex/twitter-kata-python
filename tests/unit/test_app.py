from unittest.mock import Mock

import pytest

from twitter.app import TwitterConsole
from twitter.infrastructure import Console


@pytest.fixture
def console():
    return Mock(Console)


@pytest.fixture
def twitter(console):
    return TwitterConsole(console)


def test_should_terminate_when_an_exit_command_is_received(twitter, console):
    console.input.side_effect = ["a command", "exit"]

    twitter.start()

    console.print.assert_called_with("bye!")
