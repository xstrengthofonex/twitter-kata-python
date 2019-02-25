from twitter.infrastructure import Console


class TwitterConsole:
    def __init__(self, console):
        self.console = console

    def start(self):
        while True:
            user_command = self.console.input()
            if user_command == "exit":
                self.console.print("bye!", end="")
                break


if __name__ == '__main__':
    twitter = TwitterConsole(Console())
    twitter.start()
