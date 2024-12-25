import tkinter


class Input:
    def __init__(self, root):
        self._input = tkinter.Entry(root, width=50)

    def bind(self, action):
        self._input.bind('<Return>', action)
        self._input.pack(padx=10, pady=5)

    def get(self):
        return self._input.get()

    def delete(self):
        self._input.delete(0, tkinter.END)
