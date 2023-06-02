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

        #-------------DATA FRAME----------------- this will contain two data label frame on either side inside
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        #Data frame for left side
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font="Arial 16 bold",text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        #Data frame for right side
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font="Arial 16 bold",text="Prescription")
        DataframeRight.place(x=990,y=5,width=499,height=350)


        # ----------------------BUTTON FRAME----------------------------------
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        # ----------------------Detail FRAME----------------------------------
        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,heigh=190)

root=Tk()
obj=Hospital(root)
root.mainloop()