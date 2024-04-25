from tkinter import *

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Javascript")
Lb1.insert(3, "CSS")
Lb1.insert(4, "PHP")
Lb1.insert(5, "Java")
Lb1.insert(6, "HTML")

Lb1.pack()
top.mainloop()