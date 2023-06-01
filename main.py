from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random 
import time
import datetime
# import mysql.connector


class Hospital: 
    def __init__(self,root):
        self.root=root   #Initializing the root inside  init
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")   #(WidthxHeight+start x-axis+start y-axis)

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="black",font="Arial 50 bold")
        lbltitle.pack(side=TOP,fill=X)




root=Tk()
obj=Hospital(root)
root.mainloop()