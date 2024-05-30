#CREATING GUI USING TKINTER (2)

from tkinter import *

#Jalankan code untuk lihat topik berjalan. Beri tanda # untuk topik yang tidak dijalankan.
#untuk topik yang #Exercise1#

print("====================")
print("==Mencetak data dari Entry Widget dengan Button==")
print("====================")
root = Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width=20)
entry1.pack()

button1 = Button(root, text="Cetak Data", command=CetakData).pack()

root.mainloop()

print('=================================================')
print('==Exercise1: Menginput Data dan Menampilkan Data (Part1)==')
print('=================================================')
from tkinter import *
from tkinter import messagebox

class DataInOut:

    def __init__(self, root):
        self.root = root
        self.root.title('Penjualan')
        self.root.geometry('300x150+0+0')

        frame1 = Frame(self.root)
        frame1.grid(row=0)

        frame2 = Frame(frame1) #frame2,3,4 diletakkan pada frame1
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        frame4 = Frame(frame1)
        frame4.grid(row=2, column=1)

        FirstNum = StringVar()
        SecondNum = StringVar()
        
        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2)
        self.txtSecondNum.grid(row=1, column=1)

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
    
    
print('===============Exercise#2================')
print('Mengambil Data dan Menampilkan Data Part 2')
print('=========================================')

from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        frame1 = Frame(self.root)
        frame1.grid()
        frame2 = Frame(frame1)
        frame2.grid(row = 0, column= 0)
        frame2 = Frame(frame1)
        frame2.grid(row=1,column=0)
        frame3 = Frame(frame1)
        frame.grid(row=2, column=0)
        
        FirstNum = StringVar()
        SecondNum = StringVar()
        Hasil = StringVar()
        
        self.lblFirstNum = Label(frame2, text='Masukan Bilangan Pertama')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)
        
        self.lblSecondNum = Label(frame2, text='Masukan Bilangan Kedua')
        self.lblSecondNum.grid(row=0, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=0, column=1)
        
        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=3, column=0)
        self.txtHasil = Entry(frame2,textvariable=Hasil)
        self.txtHasil.grid(row=3,column=1)
        
        def JUMLAHKAN():
            pertama = float(FirstNum.get())
            kedua = float(SecondNum.get())
            hasil = pertama + kedua
            Hasil.set(hasil)
            
        self.btnJumlahkan = Button(frame3,text='Jumlahkan').grid(row=2,column=0)
        self.btnReset = Button(frame3, text = 'Reset').grid(row = 2, column = 1)
        self.btnKeluar = Button(frame3, text = 'Keluar').grid(row = 2, column = 2)
        
if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()