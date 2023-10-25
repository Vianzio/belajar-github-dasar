from tkinter import *
root = Tk()
root.title('Kalkulator')

layar = Entry(root, width = 27, borderwidth = 5)
layar.grid(column=0,row=0,columnspan =3,padx=10, pady= 10 )
def tambahAngka(angka):
    angkaPertama = layar.get()
    layar.delete(0, END)
    layar.insert(0, str(angkaPertama + str (angka)))
def hapus():
    layar.delete(0, END)
def tambah():
    angka_pertama = layar.get()
    global angkaFirst
    global math 
    math ="tambah"
    angkaFirst = int(angka_pertama)
    layar.delete(0,END)
def bagi():
    angka_pertama = layar.get()
    global angkaFirst
    global math 
    math ="tambah"
    angkaFirst = int(angka_pertama)
    layar.delete(0,END)
def kurang():
    angka_pertama = layar.get()
    global angkaFirst
    global math 
    math ="kurang"
    angkaFirst = int(angka_pertama)
    layar.delete(0,END)
  
def kali():
    angka_pertama = layar.get()
    global angkaFirst
    global math 
    math ="kali"
    angkaFirst = int(angka_pertama)
    layar.delete(0,END)
def hasil():
    angka_kedua = int(layar.get())
    layar.delete(0,END)
    if math == "tambah":
      layar.insert(0,angkaFirst + int(angka_kedua))
    if math == "kurang":
     layar.insert(0,angkaFirst - int(angka_kedua))
    if math == "kali":
      layar.insert(0,angkaFirst  * int(angka_kedua))
    if math == "bagi":
      layar.insert(0,angkaFirst / int(angka_kedua))
angka0 = Button(root, text='0', padx = 40, pady = 20, command = lambda: tambahAngka(0))
angka1 = Button(root, text='1', padx = 40, pady = 20, command = lambda: tambahAngka(1))
angka2 = Button(root, text='2', padx = 40, pady = 20, command = lambda: tambahAngka(2))
angka3 = Button(root, text='3', padx = 40, pady = 20, command = lambda: tambahAngka(3))
angka4 = Button(root, text='4', padx = 40, pady = 20, command = lambda: tambahAngka(4))
angka5 = Button(root, text='5', padx = 40, pady = 20, command = lambda: tambahAngka(5))
angka6= Button(root, text= '6', padx = 40, pady = 20, command = lambda: tambahAngka(6))
angka7 = Button(root, text='7', padx = 40, pady = 20, command = lambda: tambahAngka(7))
angka8 = Button(root, text='8', padx = 40, pady = 20, command = lambda: tambahAngka(8))
angka9 = Button(root, text='9', padx = 40, pady = 20, command = lambda: tambahAngka(9))

hapus = Button(root, text = 'hapus', padx = 73, pady = 20,command=hapus)
tambah = Button(root, text ='+', padx =40, pady = 20, command = tambah)
samaDengan = Button(root, text= '=', padx =40, pady=20, command =hasil)
kurang = Button(root, text= '-',padx = 40,pady=20, command = kurang)
kali = Button(root, text= '*',padx = 40,pady=20, command = kali)
bagi = Button(root, text= '/',padx = 40,pady=20, command = bagi)
angka1.grid(column=0,row=1)
angka2.grid(column=1,row=1)
angka3.grid(column=2,row=1)
angka4.grid(column=0,row=2)
angka5.grid(column=1,row=2)
angka6.grid(column=2,row=2)
angka7.grid(column=0,row=3)
angka8.grid(column=1,row=3)
angka9.grid(column=2,row=3)
angka0.grid(column=0,row=4)
hapus.grid(column=1,row=4,columnspan=2)
tambah.grid(column=0,row=5)
samaDengan.grid(column =1,row =5,columnspan=2)
kurang.grid(column=0,row=6)
kali.grid(column=1,row=6)
bagi.grid(column=2,row=6)
root.mainloop()
