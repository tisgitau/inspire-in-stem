#1/user/bin/python

############
#  Name : Sam Gitau
#  Gui_examples
#  Date:7/6/2022
#################

from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg='blue')
window.geometry("400x700")
f_name = Label(window, text = "First name ", font = ("Aerial bold",20))
s_name = Label(window, text = "Second name", font = ("Aerial bold",20))
f_name.grid(column = 60 ,row = 100)
s_name.grid(column = 60 ,row = 100)

def open_poppedup():
    top = Toplevel(window)
    top.geometry ("300x300")
    top.title("POPPUP WINDOW")
    top.config(bg="white")
    msg = Label(top,text = "welcome user", font = ("Aerial",18))


btn = Button(text = "sign up" ,bg = "white",fg = "red")
btn.grid(column=120,row=150)

f_name_box = Entry(window, width= 20 )
f_name.grid(column = 70, row =70) 

s_name_box= Entry ( window , width = 100 ,bg = "red")
s_name.grid(column = 110, row = 110)

window.mainloop