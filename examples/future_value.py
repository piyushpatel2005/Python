import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Future value Calculator")
root.geometry("300x200")
root.mainloop()

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=ttk.BOTH, expand=True)
button1 = ttk.Button(frame, text="Click Me")
button2 = ttk.Button(frame, text="No, Me")
button1.pack()
button2.pack()
