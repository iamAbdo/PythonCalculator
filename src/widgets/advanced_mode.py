import tkinter as tk
from config import style as cfg

class AdvancedModeFrame(tk.Frame):
    def __init__(self, master, button_command, calculate_command, clear_command):
        super().__init__(master, bg=cfg.COLORS['background'])
        self.button_command = button_command
        self.calculate_command = calculate_command
        self.clear_command = clear_command
        self.create_buttons()
        self.configure_layout()

    def configure_layout(self):
        # Configure grid columns for 5-column layout
        for i in range(5):
            self.columnconfigure(i, weight=1, uniform='col')
        self.rowconfigure(5, weight=1)  # Add spacing at bottom

    def create_buttons(self):
        buttons = [
            ('(', 0, 0), (')', 0, 1), ('C', 0, 2), ('/', 0, 3), ('sin', 0, 4),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3), ('cos', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('tan', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3), ('log', 3, 4),
            ('0', 4, 0), ('.', 4, 2), ('=', 4, 3), ('ln', 4, 4),
            ('π', 5, 0), ('e', 5, 1), ('√', 5, 2), ('x²', 5, 3), ('^', 5, 4)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        if text == '0':
            btn = tk.Button(
                self,
                text=text,
                width=cfg.DIMENSIONS['num_pad_button_width'],
                height=cfg.DIMENSIONS['button_height'],
                bg=cfg.COLORS['button_bg'],
                fg=cfg.COLORS['button_fg'],
                command=lambda t=text: self.button_command(t),
                **cfg.BUTTON_STYLE
            )
            btn.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=1, pady=1)
        else:
            if text == 'C':
                cmd = self.clear_command
                bg_color = cfg.COLORS['special_button_bg']
            elif text == '=':
                cmd = self.calculate_command
                bg_color = cfg.COLORS['special_button_bg']
            else:
                cmd = lambda t=text: self.button_command(t)
                bg_color = cfg.COLORS['button_bg']
            
            btn = tk.Button(
                self,
                text=text,
                width=cfg.DIMENSIONS['button_width'],
                height=cfg.DIMENSIONS['button_height'],
                bg=bg_color,
                fg=cfg.COLORS['button_fg'],
                command=cmd,
                **cfg.BUTTON_STYLE
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)
        return btn