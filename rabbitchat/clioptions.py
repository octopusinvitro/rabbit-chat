import argparse


class CLIOptions:
    DEFAULT_HOSTNAME = 'localhost'

    def __init__(self, arguments):
        parser = self._setup()
        self._options = parser.parse_args(arguments)

    @property
    def hostname(self):
        return self._options.hostname

    @property
    def username(self):
        return self._options.username

    def _setup(self):
        parser = argparse.ArgumentParser(
            prog='Rabbit Chat',
            description='A chat made with RabbitMQ and a GUI made with tkinter.',
            usage='%(prog)s [OPTIONS]...'
        )
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            help='User name to display in the chat.',
            required=True
        )
        parser.add_argument(
            '-o',
            '--hostname',
            type=str,
            help='Host to connect to.',
            required=False,
            default=self.DEFAULT_HOSTNAME
        )

        return parser
