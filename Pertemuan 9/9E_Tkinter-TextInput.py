from tkinter import *
import tkinter

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
L1 =Label(top, text='Username')
E1 = Entry(top, bd = 5)
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
    onvalue = 1, offvalue = 0, height = 5, \
    width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
    onvalue = 1, offvalue = 0, height = 5, \
    width = 20)
button = Button(top, text="Checkbox")



L1.pack(side = LEFT)
E1.pack(side = RIGHT)
C1.pack()
C2.pack()
button.pack()

top.mainloop()