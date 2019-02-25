Feature: Posting and Reading

	Scenario: Reading posts from a user

		Given Alice posts a few messages
		When Bob reads Alice's messages
		Then Alice's messages are displayed in reverse chronological order