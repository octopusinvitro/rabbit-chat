import sys
from threading import Thread

from .clioptions import CLIOptions
from .queues.connection import Connection
from .queues.channel_factory import ChannelFactory
from .gui.main_gui import MainGUI
from .parser import Parser


def main():
    options = CLIOptions(sys.argv[1:])

    gui = MainGUI.create(options.username)
    parser = Parser(options.username)

    user = Connection(ChannelFactory.create(options.hostname), parser, None)
    server = Connection(ChannelFactory.create(options.hostname), parser, gui.display)
    [connection.setup() for connection in (user, server)]

    listener_thread = Thread(target=server.wait_for_messages, daemon=True)
    listener_thread.start()

    gui.start(user)
