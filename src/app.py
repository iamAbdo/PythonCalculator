import tkinter as tk
from widgets.simple_mode import SimpleModeFrame
from widgets.advanced_mode import AdvancedModeFrame
from utils.calculator import evaluate_expression
from config import style as cfg

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.configure(bg=cfg.COLORS['background'])
        self.master.resizable(False, False)
        
        # Configure grid layout
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(2, weight=1)
        
        self.create_display()
        self.create_mode_selector()
        self.create_frames()

    def create_display(self):
        self.display = tk.Entry(
            self.master,
            width=28,  # Adjusted to match button grid width
            font=cfg.DIMENSIONS['display_font'],
            justify='right',
            bd=5,
            bg=cfg.COLORS['display_bg'],
            fg=cfg.COLORS['display_fg']
        )
        self.display.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

    def create_mode_selector(self):
        mode_frame = tk.Frame(self.master, bg=cfg.COLORS['background'])
        mode_frame.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')
        
        self.simple_btn = tk.Button(
            mode_frame,
            text="Simple",
            command=self.show_simple,
            width=8,
            bg=cfg.COLORS['mode_button_bg'],
            fg=cfg.COLORS['mode_button_fg'],
            **cfg.BUTTON_STYLE
        )
        self.simple_btn.pack(side=tk.LEFT, padx=2)
        
        self.advanced_btn = tk.Button(
            mode_frame,
            text="Advanced",
            command=self.show_advanced,
            width=8,
            bg=cfg.COLORS['mode_button_bg'],
            fg=cfg.COLORS['mode_button_fg'],
            **cfg.BUTTON_STYLE
        )
        self.advanced_btn.pack(side=tk.LEFT, padx=2)

    def create_frames(self):
        self.simple_frame = SimpleModeFrame(self.master, self.button_click, self.calculate, self.clear)
        self.advanced_frame = AdvancedModeFrame(self.master, self.button_click, self.calculate, self.clear)
        self.show_simple()

    def show_simple(self):
        self.advanced_frame.grid_forget()
        self.simple_frame.grid(row=2, column=0, columnspan=4, pady=(0, 10), sticky='nsew')
        self.update_mode_buttons(True)

    def show_advanced(self):
        self.simple_frame.grid_forget()
        self.advanced_frame.grid(row=2, column=0, columnspan=5, pady=(0, 10), sticky='nsew')
        self.update_mode_buttons(False)

    def update_mode_buttons(self, simple_active):
        active_bg = cfg.COLORS['active_mode_bg']
        inactive_bg = cfg.COLORS['mode_button_bg']
        
        self.simple_btn.config(bg=active_bg if simple_active else inactive_bg)
        self.advanced_btn.config(bg=active_bg if not simple_active else inactive_bg)

    def button_click(self, char):
        current = self.display.get()
        self.display.delete(0, tk.END)
        
        special_mappings = {
            'x²': '**2', '√': 'sqrt(', '^': '**',
            'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan(',
            'log': 'log(', 'ln': 'ln('
        }
        
        self.display.insert(0, current + special_mappings.get(char, str(char)))

    def calculate(self):
        expression = self.display.get()
        result = evaluate_expression(expression)
        self.display.delete(0, tk.END)
        self.display.insert(0, result)
        
    def clear(self):
        self.display.delete(0, tk.END)