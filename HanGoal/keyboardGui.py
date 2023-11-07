#Dependencies

import tkinter as tk

class InputDialog(tk.Toplevel):
    def __init__(self, parent, title="Input"):
        super().__init__(parent)
        self.title(title)
        self.result = None
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter text:")
        self.label.pack(padx=10, pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=5)

        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=5)

    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

def show_keyboard_and_input():
    root = tk.Tk()
    root.title("Korean On-Screen Keyboard")

    input_dialog = InputDialog(root)
    root.wait_window(input_dialog)

    user_input = input_dialog.result
    if user_input is not None:
        print("User input:", user_input)
        return user_input

