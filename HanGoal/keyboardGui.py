#Dependencies

import tkinter as tk
from tkinter.simpledialog import Dialog

class InputDialog(Dialog):
    def body(self, master):
        self.result = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result)
        self.entry.pack()
        return self.entry

def show_keyboard_and_input():
    root = tk.Tk()
    root.title("Korean On-Screen Keyboard")

    input_dialog = InputDialog(root)
    input_dialog.show()

    user_input = input_dialog.result.get()
    print("User input:", user_input)
