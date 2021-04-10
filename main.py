import tkinter as tk
from tkinter import VERTICAL, RIGHT, Y, LEFT, X, HORIZONTAL, BOTTOM, TOP, ttk


class MainForm:

    # init method
    def __init__(self, root):
        # set root
        self.root = root

        # set application name
        self.root.title("My Check Register")
# ------------------------------------------------------------------------------------------------------------------------------------#
        # getting dimensions of current screen
        self.root.csw = root.winfo_screenwidth()
        self.root.csh = root.winfo_screenheight()

        # setting dimensions of application window
        # syntax here is (width x height + x + y)
        csw = int(self.root.csw * .75)
        csh = int(self.root.csh * .75)
        xw = int(self.root.csw * .1)
        yh = int(self.root.csh * .1)

        self.root.geometry(f'{csw}x{csh}+{xw}+{yh}')
# ------------------------------------------------------------------------------------------------------------------------------------#
        # setting up frames for check register
        # syntax is (parent window, background (bg), border (bd), cursor, width, height, relief, highlightbackground,
        # highlightcolor, highlightthickness)

        mainframe = tk.Frame(self.root, bg="light grey", bd=10, width=int(csw-10), height=int(csh-10), relief="ridge")
        mainframe.place(width=int(csw-10), height=int(csh-10))

        subframebottom = tk.Frame(mainframe, bg="light grey", bd=5, width=int(csw*.98), height=int((csh-10)*.14), relief="ridge")
        subframebottom.place(in_=mainframe, relx=0, rely=.86)

        subframetop = tk.Frame(mainframe, bg="white", bd=5, width=int(csw*.98), height=int((csh-10)*.84), relief="ridge")
        subframetop.place(in_=mainframe, relx=0, rely=0)

        subframetopleft = tk.Frame(subframetop, bg="white", bd=0, width=int(csw*.90), height=int((csh-15)), relief="flat")
        subframetopleft.place(in_=subframetop, relx=0, rely=0)

        subframetopright = tk.Frame(subframetop, bg="light grey", bd=1, width=int(csw*.1), height=int((csh-15)), relief="flat")
        subframetopright.place(in_=subframetop, relx=.99, rely=.04)
# ------------------------------------------------------------------------------------------------------------------------------------#
         # Vertical Scroll bar
        scroll_y = tk.Scrollbar(subframetopright, orient=VERTICAL)
        scroll_y.pack(side=LEFT, fill=Y)
# ------------------------------------------------------------------------------------------------------------------------------------#
        # setting up buttons for bottom frame
        btnAddNew = tk.Button(subframebottom, bg="snow", activebackground="light blue", fg="black", height=1, width=20,
                              pady=1, padx=1, text="Add New Transaction", font=('Calibri Light', 16, 'bold'), relief='raised')
        btnAddNew.place(in_=subframebottom, relx=.12, rely=.05)

        btnEdit = tk.Button(subframebottom, bg="snow", activebackground="light blue", fg="black", height=1, width=20,
                            pady=1, padx=1, text="Edit Transaction", font=('Calibri Light', 16, 'bold'),
                            relief='raised')
        btnEdit.place(in_=subframebottom, relx=.32, rely=.05)

        btnDelete = tk.Button(subframebottom, bg="snow", activebackground="light blue", fg="black", height=1, width=20,
                            pady=1, padx=1, text="Delete Transaction", font=('Calibri Light', 16, 'bold'),
                            relief='raised')
        btnDelete.place(in_=subframebottom, relx=.52, rely=.05)

        btnExit = tk.Button(subframebottom, bg="snow", activebackground="light blue", fg="black", height=1, width=20,
                            pady=1, padx=1, text="Exit Check Register", font=('Calibri Light', 16, 'bold'),
                            relief='raised')
        btnExit.place(in_=subframebottom, relx=.72, rely=.05)
# ------------------------------------------------------------------------------------------------------------------------------------#
        # setting up subframetopleft to support the list of transactions (Treeview)
        # rewrite this is pull from mysql

        mainTable_records = ttk.Treeview(subframetopleft, columns=("NumberCode", "Date", "TransactionDescription", "PayFeeWith", "Cleared", "DepCredRef", "Balance"), yscrollcommand=scroll_y.set)

        mainTable_records.heading("#1", text="NUMBER/CODE")
        mainTable_records.heading("#2", text="DATE")
        mainTable_records.heading("#3", text="TRANSACTION DESCRIPTION")
        mainTable_records.heading("#4", text="PAYMENT/FEE/WITHDRAWAL")
        mainTable_records.heading("#5", text="CLEARED")
        mainTable_records.heading("#6", text="DEPOSIT/CREDIT/REFUND")
        mainTable_records.heading("#7", text="BALANCE")

        mainTable_records.column("#0", stretch=tk.NO, width=0)
        mainTable_records.column("#1", stretch=tk.YES)
        mainTable_records.column("#2", stretch=tk.YES)
        mainTable_records.column("#3", stretch=tk.YES)
        mainTable_records.column("#4", stretch=tk.YES)
        mainTable_records.column("#5", stretch=tk.YES)
        mainTable_records.column("#6", stretch=tk.YES)
        mainTable_records.column("#7", stretch=tk.YES)

        mainTable_records.place(in_=subframetopleft, relx=0, rely=0)

        mainTable_records.pack()
# ------------------------------------------------------------------------------------------------------------------------------------#
        # Inserting temp records to test how this looks
        # Rewrite this to pull from mysql

        mainTable_records.insert('', 'end', values=("Deposit", "4/1/2020", "Starting Deposit", "", "Yes", "100.00", "100.00"))
        mainTable_records.insert('', 'end', values=("ACH", "4/10/2020", "McDonalds", "1.00", "Yes", "", "99.00"))

        # need to write code here for


root = tk.Tk()
application = MainForm(root)
root.mainloop()

# print(root.curscreenwidth)
# print(root.curscreenheight)
