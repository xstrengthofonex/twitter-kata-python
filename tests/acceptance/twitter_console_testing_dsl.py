import subprocess


class TwitterConsoleTestingDSL:
    EXIT_COMMAND = "exit\n"
    TWITTER_CONSOLE_ON_COMMAND_LINE = ("python", "-m", "twitter.app")

    def __init__(self):
        self.user_commands = []

    def receives(self, command):
        self.user_commands.append(command + "\n")

    def output(self):
        if self.EXIT_COMMAND not in self.user_commands:
            self.user_commands.append(self.EXIT_COMMAND)
        return self.run_twitter_console_with(self.user_commands)

    def run_twitter_console_with(self, user_commands):
        with subprocess.Popen(
                self.TWITTER_CONSOLE_ON_COMMAND_LINE,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                universal_newlines=True) as process:
            output = process.communicate("".join(user_commands), 3)[0]
        return output
