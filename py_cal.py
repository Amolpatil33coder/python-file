 import tkinter as tk
from tkinter import ttk

class ColorfulCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Calculator")
        self.root.geometry("380x550")
        self.root.resizable(False, False)

        self.expression = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.root.configure(bg="#f0f4f8")

        # Display styling
        self.style.configure("TEntry", fieldbackground="white", foreground="#333", font=("Segoe UI", 28))

        # Button styles (increased font size)
        self.style.configure("Num.TButton", background="#4a90e2", foreground="white", font=("Segoe UI", 18), padding=10)
        self.style.map("Num.TButton", background=[("active", "#357ABD")])

        self.style.configure("Op.TButton", background="#f5a623", foreground="white", font=("Segoe UI", 18), padding=10)
        self.style.map("Op.TButton", background=[("active", "#d48806")])

        self.style.configure("Func.TButton", background="#50e3c2", foreground="white", font=("Segoe UI", 18), padding=10)
        self.style.map("Func.TButton", background=[("active", "#3ac7a5")])

        # Display
        self.display_var = tk.StringVar()
        display = ttk.Entry(self.root, textvariable=self.display_var, justify="right")
        display.pack(fill="x", padx=20, pady=20, ipady=14)

        # Buttons
        grid_frame = ttk.Frame(self.root)
        grid_frame.pack(padx=10, pady=5, fill="both", expand=True)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "⌫", "+"],
            ["C", "=", "History"]
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                style = (
                    "Op.TButton" if char in "+-*/=" else
                    "Func.TButton" if char in ["C", "⌫", "History"] else
                    "Num.TButton"
                )
                ttk.Button(
                    grid_frame,
                    text=char,
                    style=style,
                    command=lambda b=char: self.on_click(b)
                ).grid(row=r, column=c, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1)

    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.display_var.set(result)
                self.expression = result
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.display_var.set("")
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)
        elif char == "History":
            self.show_history()
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def show_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("Calculation History")
        history_win.geometry("300x400")
        history_win.configure(bg="#eaf0f6")

        tk.Label(
            history_win,
            text="History",
            font=("Segoe UI", 16, "bold"),
            bg="#eaf0f6",
            fg="#333"
        ).pack(pady=10)

        listbox = tk.Listbox(history_win, font=("Segoe UI", 16), bg="white", fg="#333")
        listbox.pack(fill="both", expand=True, padx=10, pady=10)

        for item in self.history:
            listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorfulCalculator(root)
    root.mainloop()
