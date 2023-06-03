from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
# import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root  # Initializing the root inside  init
        self.root.title("Hospital Management System")
        # (WidthxHeight+start x-axis+start y-axis)
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                         fg="red", bg="black", font="Arial 50 bold")
        lbltitle.pack(side=TOP, fill=X)

        # -------------DATA FRAME----------------- this will contain two data label frame on either side inside
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        # Data frame for left side
        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE,
                                   padx=10, text="Patient Information", font="Arial 16 bold")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        # Data frame for right side
        DataframeRight = LabelFrame(
            Dataframe, bd=10, relief=RIDGE, padx=10, font="Arial 16 bold", text="Prescription")
        DataframeRight.place(x=990, y=5, width=499, height=350)

        # ----------------------BUTTON FRAME----------------------------------
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ----------------------Detail FRAME----------------------------------
        Detailframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailframe.place(x=0, y=600, width=1530, heigh=190)

        # -----------------Creating Label and Entry field in Data frame on the left hand side-----------------------
        lblNameTablet = Label(DataframeLeft, text="Name of Tablet",
                              font="Arial 12 bold", padx=2, pady=4)  # Label Name
        lblNameTablet.grid(row=0, column=0, sticky=W)
        comNametablet = ttk.Combobox(
            DataframeLeft, font="Arial 12 bold", width=30)  # Entry field
        comNametablet["values"] = (
            "", "Ibuprofen", "Paracetamol", "Aspirin", "Omeprazole", "Atorvastatin", "Metformin")
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, text="Reference",
                       font="Arial 12 bold", padx=4)  # Label Name
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtref.grid(row=1, column=1)

        lbldose = Label(DataframeLeft, text="Doseage",
                        font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbldose.grid(row=2, column=0, sticky=W)
        txtdose = Entry(DataframeLeft, font="Arial 12 bold",
                        width=35)  # Entry field
        txtdose.grid(row=2, column=1)

        lblnumbertabs = Label(DataframeLeft, text="No.of Tablets",
                              font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblnumbertabs.grid(row=3, column=0, sticky=W)
        txtnumtabs = Entry(DataframeLeft, font="Arial 12 bold",
                           width=35)  # Entry field
        txtnumtabs.grid(row=3, column=1)

        lbllot = Label(DataframeLeft, text="Lot",
                       font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbllot.grid(row=4, column=0, sticky=W)
        txtlot = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtlot.grid(row=4, column=1)

        lblissue = Label(DataframeLeft, text="Issue Date",
                         font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblissue.grid(row=5, column=0, sticky=W)
        txtissue = Entry(DataframeLeft, font="Arial 12 bold",
                         width=35)  # Entry field
        txtissue.grid(row=5, column=1)

        lblend = Label(DataframeLeft, text="Expiary Date",
                       font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblend.grid(row=6, column=0, sticky=W)
        txtend = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtend.grid(row=6, column=1)

        lbldailydose = Label(DataframeLeft, text="Daily Dose",
                             font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbldailydose.grid(row=7, column=0, sticky=W)
        txtdailydose = Entry(
            DataframeLeft, font="Arial 12 bold", width=35)  # Entry field
        txtdailydose.grid(row=7, column=1)

        lbleffect = Label(DataframeLeft, text="Side Effects",
                          font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbleffect.grid(row=8, column=0, sticky=W)
        txteffect = Entry(DataframeLeft, font="Arial 12 bold",
                          width=35)  # Entry field
        txteffect.grid(row=8, column=1)

        lblinfo = Label(DataframeLeft, text="Further Information",
                        font="Arial 12 bold", padx=2)  # Label Name
        lblinfo.grid(row=0, column=2, sticky=W)
        txtinfo = Entry(DataframeLeft, font="Arial 12 bold",
                        width=35)  # Entry field
        txtinfo.grid(row=0, column=3)

        lblbloodp = Label(DataframeLeft, text="Blood Pressure",
                          font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblbloodp.grid(row=1, column=2, sticky=W)
        txtbloodp = Entry(DataframeLeft, font="Arial 12 bold",
                          width=35)  # Entry field
        txtbloodp.grid(row=1, column=3)

        lblstore = Label(DataframeLeft, text="Storing Space",
                         font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblstore.grid(row=2, column=2, sticky=W)
        txtstore = Entry(DataframeLeft, font="Arial 12 bold",
                         width=35)  # Entry field
        txtstore.grid(row=2, column=3)

        lblmed = Label(DataframeLeft, text="Medication",
                       font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblmed.grid(row=3, column=2, sticky=W)
        txtmed = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtmed.grid(row=3, column=3)

        lblid = Label(DataframeLeft, text="Patient Id",
                      font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblid.grid(row=4, column=2, sticky=W)
        txtid = Entry(DataframeLeft, font="Arial 12 bold",
                      width=35)  # Entry field
        txtid.grid(row=4, column=3)

        lblname = Label(DataframeLeft, text="Patient Name",
                        font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblname.grid(row=5, column=2, sticky=W)
        txtname = Entry(DataframeLeft, font="Arial 12 bold",
                        width=35)  # Entry field
        txtname.grid(row=5, column=3)

        lblnhs = Label(DataframeLeft, text="NHS Number",
                       font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lblnhs.grid(row=6, column=2, sticky=W)
        txtnhs = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtnhs.grid(row=6, column=3)

        lbldob = Label(DataframeLeft, text="Date of Birth",
                       font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbldob.grid(row=7, column=2, sticky=W)
        txtdob = Entry(DataframeLeft, font="Arial 12 bold",
                       width=35)  # Entry field
        txtdob.grid(row=7, column=3)

        lbllocation = Label(DataframeLeft, text="Address",
                            font="Arial 12 bold", padx=2, pady=6)  # Label Name
        lbllocation.grid(row=8, column=2, sticky=W)
        txtlocation = Entry(
            DataframeLeft, font="Arial 12 bold", width=35)  # Entry field
        txtlocation.grid(row=8, column=3)

        # -----------------Creating Label and Entry field in Data frame on the right hand side-----------------------
        Text(DataframeRight, font="Arial 12 bold",
             width=50, height=16, padx=2, pady=2).grid(row=0, column=0)  # Crating txt field

        # --------------------CREATING BUTTONS inside Buttonframe------------------------------------------
        butnpres = Button(Buttonframe, text="Presciption", bg="red", fg="black",
                          font="Arial 13 bold", width=23, height=1, padx=5, pady=3)
        butnpres.grid(row=0, column=0)

        butndata = Button(Buttonframe, text="Presciption Data", bg="red", fg="black",
                          font="Arial 12 bold", width=23, height=1, padx=5, pady=3)
        butndata.grid(row=0, column=1)

        butnupdate = Button(Buttonframe, text="Update", bg="red", fg="black",
                            font="Arial 13 bold", width=23, height=1, padx=5, pady=3)
        butnupdate.grid(row=0, column=2)

        butndel = Button(Buttonframe, text="Delete", bg="red", fg="black",
                         font="Arial 13 bold", width=23, height=1, padx=5, pady=3)
        butndel.grid(row=0, column=3)

        butnclr = Button(Buttonframe, text="Clear", bg="red", fg="black",
                         font="Arial 13 bold", width=23, height=1, padx=5, pady=3)
        butnclr.grid(row=0, column=4)

        butnexit = Button(Buttonframe, text="Exit", bg="red", fg="black",
                          font="Arial 13 bold", width=23, height=1, padx=5, pady=3)
        butnexit.grid(row=0, column=5)


        # ------------------------------DATA STORAGE INFORM OF TABLE for Detail Frame------------------

        # Making Scroll Bar inside Detail frame
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)    #Scroll bar on x axis
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)      #Scroll bar on y axis

        #Creating table
        self.table=ttk.Treeview(Detailframe,column=("tabls","ref","dose","nooftabs","lot","issue","expy","daily",
                                                    "store","nhs","name","dob","address"),xscrollcommand=scroll_x.set,
                                                    yscrollcommand=scroll_y.set)    #Giving temp name to headers to each column
                                                                                  

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.table.xview)
        scroll_y=ttk.Scrollbar(command=self.table.yview)

        #Giving Column Names
        self.table.heading("tabls",text="Name of Table")
        self.table.heading("ref",text="Reference Number")
        self.table.heading("dose",text="Doseage")
        self.table.heading("nooftabs",text="No of Tablets")
        self.table.heading("lot",text="Lot")
        self.table.heading("issue",text="Issue date")
        self.table.heading("expy",text="Expiary Date")
        self.table.heading("daily",text="Daily Dose")
        self.table.heading("store",text="Storage")
        self.table.heading("nhs",text="NHS Number")
        self.table.heading("name",text="Name")
        self.table.heading("dob",text="Date of Birth")
        self.table.heading("address",text="Address")

        self.table["show"]="headings"


        self.table.column("tabls",width=100)
        self.table.column("ref",width=100)
        self.table.column("dose",width=100)
        self.table.column("nooftabs",width=100)
        self.table.column("lot",width=100)
        self.table.column("issue",width=100)
        self.table.column("expy",width=100)
        self.table.column("daily",width=100)
        self.table.column("store",width=100)
        self.table.column("nhs",width=100)
        self.table.column("name",width=100)
        self.table.column("dob",width=100)
        self.table.column("address",width=100)

        self.table.pack(fill=BOTH,expand=1)


        






root = Tk()
obj = Hospital(root)
root.mainloop()
