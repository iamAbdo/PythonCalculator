import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.resizable(False, False)
       
        # Mode selection buttons
        mode_frame = tk.Frame(master)
        mode_frame.grid(row=0, column=0, columnspan=5, pady=5)
       
        self.simple_btn = tk.Button(mode_frame, text="Simple", command=self.show_simple)
        self.simple_btn.pack(side=tk.LEFT, padx=2)
       
        self.advanced_btn = tk.Button(mode_frame, text="Advanced", command=self.show_advanced)
        self.advanced_btn.pack(side=tk.LEFT, padx=2)

        # Create display
        self.display = tk.Entry(master, width=30, font=('Arial', 16), justify='left', bd=5)
        self.display.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        # Create frames for different modes
        self.simple_frame = tk.Frame(master)
        self.advanced_frame = tk.Frame(master)
       
        # Initialize with simple mode
        self.show_simple()

    def create_simple_buttons(self):
        # Clear previous buttons
        for widget in self.simple_frame.winfo_children():
            widget.destroy()

        buttons = [
            ('(', 0, 0), (')', 0, 1), ('C', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            if text == '0':
                btn = tk.Button(self.simple_frame, text=text, width=9, height=2,
                               command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew')
            else:
                btn = tk.Button(self.simple_frame, text=text, width=4, height=2,
                              command=lambda t=text: self.button_click(t) if t != '=' else self.calculate())
                btn.grid(row=row, column=col, sticky='nsew')

        # Equal button
        equal_btn = tk.Button(self.simple_frame, text='=', width=4, height=2, command=self.calculate)
        equal_btn.grid(row=4, column=3, sticky='nsew')

    def create_advanced_buttons(self):
        # Clear previous buttons
        for widget in self.advanced_frame.winfo_children():
            widget.destroy()

        buttons = [
            ('(', 0, 0), (')', 0, 1), ('C', 0, 2), ('/', 0, 3), ('sin', 0, 4),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3), ('cos', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('tan', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3), ('log', 3, 4),
            ('0', 4, 0), ('.', 4, 2), ('=', 4, 3), ('ln', 4, 4),
            ('π', 5, 0), ('e', 5, 1), ('√', 5, 2), ('x²', 5, 3), ('^', 5, 4)
        ]

        for (text, row, col) in buttons:
            if text == '0':
                btn = tk.Button(self.advanced_frame, text=text, width=9, height=2,
                               command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew')
            else:
                btn = tk.Button(self.advanced_frame, text=text, width=4, height=2,
                              command=lambda t=text: self.button_click(t) if t != '=' else self.calculate())
                btn.grid(row=row, column=col, sticky='nsew')

        # Equal button
        equal_btn = tk.Button(self.advanced_frame, text='=', width=4, height=2, command=self.calculate)
        equal_btn.grid(row=4, column=3, sticky='nsew')

    def show_simple(self):
        self.advanced_frame.grid_forget()
        self.simple_frame.grid(row=2, column=0, columnspan=5)
        self.create_simple_buttons()

    def show_advanced(self):
        self.simple_frame.grid_forget()
        self.advanced_frame.grid(row=2, column=0, columnspan=5)
        self.create_advanced_buttons()

    def button_click(self, char):
        current = self.display.get()
        self.display.delete(0, tk.END)
       
        # Handle special characters
        if char in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt']:
            self.display.insert(0, current + f"{char}(")
        elif char == 'x²':
            self.display.insert(0, current + "**2")
        elif char == '√':
            self.display.insert(0, current + "sqrt(")
        elif char == '^':
            self.display.insert(0, current + "**")
        else:
            self.display.insert(0, current + str(char))

    def clear(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression, {'__builtins__': None}, {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log10,
                'ln': math.log,
                'sqrt': math.sqrt,
                'π': math.pi,
                'e': math.e
            })
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()