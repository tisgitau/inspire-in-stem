#1/user/bin/python

############
#  Name : Sam Gitau
#  Gui_examples
#  Date:7/6/2022
#################

from tkinter import *

window = Tk()
window.title("Hi welcome to this awsome app")
window.configure(bg='blue')
window.geometry("900x700")
f_name = Label(window, text = "First name ", font = ("Aerial bold",20))
s_name = Label(window, text = "Second name", font = ("Aerial bold",20))
f_name.grid(column = 60 ,row = 100)
s_name.grid(column = 60 ,row = 100)
window.mainloop