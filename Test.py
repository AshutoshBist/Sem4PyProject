from tkinter import *
import  webbrowser

def open_url(url):
    pass
    link=url
    webbrowser.open_new_tab(link)

main = Tk()
url_list=[]
for i in range(10):
    l3 = Label(main, text="www.google.com/search?client=firefox-b-d&q=" + str(i), font="Georgia 16", wraplength=700,fg="blue", cursor="hand2")
    print(l3)
    url_list.append(l3.cget("text"))
    url=l3.cget("text")
    l3.bind("<Button-1>",lambda e,url=url:open_url(url))
    l3.pack()

main.mainloop()
