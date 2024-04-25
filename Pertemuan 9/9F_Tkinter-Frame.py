from tkinter import *

# root frame
root = Tk()

#frame for colored button
frame = Frame(root)
frame.pack(side = BOTTOM)

#black button frame
buttonframe = Frame(root)
buttonframe.pack(side = BOTTOM)

#frame for username
entryframe = Frame(root)
entryframe.pack(side = TOP)

labelframe = Frame(buttonframe)


var = StringVar()
label = Label(root, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")


CheckVar1 = IntVar()
CheckVar2 = IntVar()
L1 =Label(entryframe, text='Username')
E1 = Entry(entryframe, bd = 5)
C1 = Checkbutton(root, text = "Music", variable = CheckVar1, \
    onvalue = 1, offvalue = 0, height = 5, \
    width = 20)
C2 = Checkbutton(root, text = "Video", variable = CheckVar2, \
    onvalue = 1, offvalue = 0, height = 5, \
    width = 20)

L1.pack(side = LEFT)
E1.pack(side = RIGHT)
C1.pack()
C2.pack()

redbutton = Button(frame, text = 'Red', fg = 'red')
redbutton.pack(side = LEFT)

brownbutton = Button(frame, text = 'Brown', fg = 'brown')
brownbutton.pack(side = LEFT)

bluebutton = Button(frame, text = 'Blue', fg = 'blue')
bluebutton.pack(side = LEFT)

blackbutton = Button(buttonframe, text = 'Black', fg = 'black')
blackbutton.pack(side = BOTTOM)

label.pack()

root.mainloop()