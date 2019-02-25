Feature: User's wall

	Scenario: User sees messages from friends on her own wall

		Given Bob posts a few messages
		And Charlie posts a few messages
		And Charlie follows Bob
		When Charlie checks his wall
		Then messages from Bob and Charlie are displayed in reverse chronological order
