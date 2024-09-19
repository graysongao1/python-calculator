import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40,"bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24,"bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = "0"
        self.current_expression = "0"

    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, full="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=25, font=SMALL_FONT_STYLE)

    def run(self):
        self.window.mainloop()

calc=Calculator()
calc.run()