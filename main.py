import tkinter as tk


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

        mainframe = tk.Frame(self.root, bg="snow", bd=10, width=int(csw-10), height=int(csh-10), relief="ridge")

        mainframe.place(width=int(csw-10), height=int(csh-10))

        subframebottom = tk.Frame(mainframe, bg="purple", bd=5, width=int(csw*.98), height=int((csh-10)*.24), relief="flat")
        subframebottom.place(in_=mainframe, relx=0, rely=.76)

        subframetop = tk.Frame(mainframe, bg="snow", bd=5, width=int(csw*.98), height=int((csh-10)*.74), relief="flat")
        subframetop.place(in_=mainframe, relx=0, rely=0)
# ------------------------------------------------------------------------------------------------------------------------------------#
        # setting up labels for top frame
        self.lblsubframe1 = tk.Label(subframetop, font=('font', 10, 'bold'), text="NUMBER/CODE", bd=5, relief='groove')
        self.lblsubframe2 = tk.Label(subframetop, font=('font', 10, 'bold'), text="DATE", bd=5, relief='groove')
        self.lblsubframe3 = tk.Label(subframetop, font=('font', 10, 'bold'), text="TRANSACTION DESCRIPTION", bd=5, relief='groove')
        self.lblsubframe4 = tk.Label(subframetop, font=('font', 10, 'bold'), text="PAYMENT/FEE/WITHDRAWAL", bd=5, relief='groove')
        self.lblsubframe5 = tk.Label(subframetop, font=('font', 10, 'bold'), text="CLEARED", bd=5, relief='groove')
        self.lblsubframe6 = tk.Label(subframetop, font=('font', 10, 'bold'), text="DEPOSIT/CREDIT/REFUND", bd=5, relief='groove')
        self.lblsubframe7 = tk.Label(subframetop, font=('font', 10, 'bold'), text="BALANCE", bd=5, relief='groove')

        self.lblsubframe1.place(in_=subframetop, relx=0, rely=0, width=int(csw*.10))    # NUMBER/CODE
        self.lblsubframe2.place(in_=subframetop, relx=.10, rely=0, width=int(csw*.10))   # DATE
        self.lblsubframe3.place(in_=subframetop, relx=.20, rely=0, width=int(csw*.30))  # TRANSACTION DESCRIPTION
        self.lblsubframe4.place(in_=subframetop, relx=.50, rely=0, width=int(csw*.15))   # PAYMENT/FEE/WITHDRAWAL
        self.lblsubframe5.place(in_=subframetop, relx=.65, rely=0, width=int(csw*.10))   # CLEARED
        self.lblsubframe6.place(in_=subframetop, relx=.75, rely=0, width=int(csw*.15))   # DEPOSIT/CREDIT/REFUND
        self.lblsubframe7.place(in_=subframetop, relx=.9, rely=0, width=int(csw*.10))   # BALANCE
# ------------------------------------------------------------------------------------------------------------------------------------#
        # setting up buttons for bottom frame



root = tk.Tk()
application = MainForm(root)
root.mainloop()

# print(root.curscreenwidth)
# print(root.curscreenheight)
