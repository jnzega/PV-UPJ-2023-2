from tkinter import *
def donothing():
    var = StringVar()
    label = Message(root, textvariable=var, relief=RAISED)
    var.set("Hey!? How are you doing?")
    return label.pack()

root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

root.config(menu=menubar)

Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Javascript")
Lb1.insert(3, "CSS")
Lb1.insert(4, "PHP")
Lb1.insert(5, "Java")
Lb1.insert(6, "HTML")

Lb1.pack(side = LEFT)

root.mainloop()