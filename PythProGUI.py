import tkinter
from tkinter import *


def uprod():
    prodname = Sbox.get()
    prodword = prodname.split()
    n = len(prodword)
    print(n)

    if n == 1:
        produrl = prodword[0]
    else:
        produrl = prodword[0]
        for i in range(1, n):
            produrl = str(produrl + '+' + prodword[i])

    amazon = produrl
    return amazon



main = Tk()
main.title("Best Deals")
main.geometry("800x600")

# root = Frame(main, bg='#30D9D8')
# root.pack()

L1 = Label(main, text='Best Deal', fg='#CD3131', font="Georgia 20 bold", bd=20)
L1.pack()

Sbox = Entry(main, text='Product Name', bd=5, width=50, font="Georgia 16 ")
Sbox.pack()

E_Searched = tkinter.Button(main, text="Go", font="Georgia 16 ", activebackground='#30D9D8',command=uprod)
E_Searched.pack()

for i in range(0,3):


main.mainloop()
