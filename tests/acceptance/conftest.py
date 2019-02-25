import pytest

from tests.acceptance.twitter_console_testing_dsl import TwitterConsoleTestingDSL


@pytest.fixture
def twitter_console():
    return TwitterConsoleTestingDSL()
