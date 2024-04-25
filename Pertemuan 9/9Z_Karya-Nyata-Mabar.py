import tkinter as tk

def greet():
    print("Hello, World!")

root = tk.Tk()
button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
