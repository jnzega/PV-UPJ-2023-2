import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
    ["Zega", 20, 130000],
    ["UPJ", 99, 666000],
    ["Letris", 666, 99999],
    ["Anjay", 23, 123456],
]

index = 0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("age", "salary")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Name')
tree.heading('age', text='Age')
tree.heading('salary', text='Salary')

read_data()
root.mainloop()