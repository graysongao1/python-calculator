from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(height=500, width=500)
root.wm_resizable(False, False)
root.title("feet to meters")

style = ttk.Style()
style.configure("custom.TFrame", background="#eb4034")

mainframe = ttk.Frame(root, style="custom.TFrame", padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.mainloop()
