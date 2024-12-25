import tkinter

from .chatbox import Chatbox
from .input import Input


class MainGUI:
    @classmethod
    def create(cls, title, root=tkinter.Tk()):
        root.title(title)
        return cls(root, Chatbox(root), Input(root))

    def __init__(self, root, chatbox, input):
        self._root = root
        self._chatbox = chatbox
        self._input = input

    def start(self, user):
        self._user = user
        self._input.bind(self._send)
        self._root.mainloop()

    def display(self, message):
        self._chatbox.display(message)

    def _send(self, event):
        message = self._input.get()
        self._user.send(message)
        self._input.delete()
