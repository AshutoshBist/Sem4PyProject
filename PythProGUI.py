import tkinter
from tkinter import *

main = Tk()
main.title("Best Deals")
main.geometry("1280x720")


root = Frame(main, bg='#30D9D8')
root.pack()

L1 = Label(root, text='Best Deal', bg='#30D9D8', fg='#CD3131', font="Georgia 20 bold", bd=20)
L1.pack()

Sbox = Entry(root, text='Product Name', bd=5, width=50, font="Georgia 16 ")
Sbox.pack()

E_Searched = tkinter.Button(root, text="Go", font="Georgia 16 ", activebackground='#30D9D8')
E_Searched.pack()

main.mainloop()
