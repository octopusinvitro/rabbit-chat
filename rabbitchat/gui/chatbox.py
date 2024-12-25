import tkinter


class Chatbox:
    def __init__(self, root):
        self._chatbox = tkinter.Text(root, width=50, height=20, wrap=tkinter.WORD)
        self._chatbox.pack(padx=10, pady=10)
        self._chatbox.config(state=tkinter.DISABLED)

    def display(self, message):
        self._chatbox.config(state=tkinter.NORMAL)
        self._chatbox.insert(tkinter.END, f'{message}\n')
        self._chatbox.config(state=tkinter.DISABLED)
        self._chatbox.yview(tkinter.END)
