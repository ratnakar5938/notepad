from tkinter.filedialog import *
import tkinter as tk

def save_file():
    new_file =asksaveasfile(mode="w", filetype=[('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get('1.0', tk.END))
    new_file.write(text)
    new_file.close()

def open_file():
    file = askopenfile(mode="r", filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(tk.INSERT, content)

def clear_file():
    entry.delete('1.0', tk.END)


canvas  = tk.Tk()
canvas.geometry("800x600")
canvas.title("Notepad by ravi")
canvas.config(bg ="white")
top = tk.Frame(canvas)
top.pack(padx=10, pady=5, anchor="nw")

b1 = tk.Button(canvas, text="Open", bg="white", command=open_file)
b1.pack(in_=top, side="left")

b2 = tk.Button(canvas, text="Save", bg="white", command=save_file)
b2.pack(in_=top, side="left")

b3 = tk.Button(canvas, text="Clear", bg="white", command=clear_file)
b3.pack(in_=top, side="left")

b4 = tk.Button(canvas, text="Exit", bg="white", command=exit)
b4.pack(in_=top, side="left")

entry = tk.Text(canvas,wrap="word", bg="#F9DDA4", font=("cursive", 14))
entry.pack(padx=10, pady=5, expand=True, fill="both")

canvas.mainloop()