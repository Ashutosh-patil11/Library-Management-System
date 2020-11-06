from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        MType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        Postcode = StringVar()
        MobileNo = StringVar()
        BookID = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        Prescription = StringVar()

        def iReset():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            Postcode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            #self.txtDisplayR.delete("1.0",END)

        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0",END)
            

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm You Want To Exit!" )
            if iExit > 0:
                root.destroy()
                return

        def iReceipt():

            self.txtDisplayR.insert(END,'Member Type: \t\t'+ MType.get() + "\n")
            self.txtDisplayR.insert(END,'Ref No: \t\t'+ Ref.get() + "\n")
            self.txtDisplayR.insert(END,'Title: \t\t'+ Title.get() + "\n")
            self.txtDisplayR.insert(END,'Firstname: \t\t'+ Firstname.get() + "\n")
            self.txtDisplayR.insert(END,'Surname: \t\t'+ Surname.get() + "\n")
            self.txtDisplayR.insert(END,'Address 1: \t\t'+ Address1.get() + "\n")
            self.txtDisplayR.insert(END,'Address 2: \t\t'+ Address2.get() + "\n")
            self.txtDisplayR.insert(END,'Post Code: \t\t'+ Postcode.get() + "\n")
            self.txtDisplayR.insert(END,'Mobile No: \t\t'+ MobileNo.get() + "\n")
            self.txtDisplayR.insert(END,'Book ID: \t\t'+ BookID.get() + "\n")
            self.txtDisplayR.insert(END,'Book Title: \t\t'+ BookTitle.get() + "\n")
            self.txtDisplayR.insert(END,'Author: \t\t'+ Author.get() + "\n")
            self.txtDisplayR.insert(END,'Date Borrowed: \t\t'+ DateBorrowed.get() + "\n")
            return
        def iDisplayData():
            self.txtFrameDetail.insert(END,"\t"+ MType.get()+"\t\t"+ Ref.get()+"\t"+ Title.get()+"\t"+ Firstname.get() + "\t"+ Surname.get()+ "\t\t"+ Address1.get() +"\t\t"+ Address2.get() +"\t" + Postcode.get() + "\t"+ BookTitle.get() + "\t\t"+ DateBorrowed.get() +"\t\t"+ DaysOnLoan.get() + "\n")


        #Frame Starting

        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame, width=39, font=('arial',40,'bold'),text="\tLibrary Management System\t",padx=12)
        self.lblTitle.grid()
        
        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial',12,'bold'), text ="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=('arial',12,'bold'), text ="Book Deatails:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #widget
        self.lblMemberType = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'), state='readonly', width=23, textvariable = MType)
        self.cboMemberType['value']=('','Student','Lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.lblBookID = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = BookID,width=25)
        self.lblBookID.grid(row=0, column=3)
        #
        self.lblRef = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Reference No:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = BookTitle, width=25)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'), state='readonly', width=23, textvariable = Title)
        self.cboTitle['value']=('','Mr.','Miss.','Mrs.','Dr.','Capt.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = Author, width=25)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstName = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Firstname:", padx=2, pady=2)
        self.lblFirstName.grid(row=3, column=0, sticky=W)
        self.txtFirstName = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = Firstname, width=25)
        self.txtFirstName.grid(row=3, column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Date Borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = DateBorrowed, width=25)
        self.txtDateBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Surname:", padx=2, pady=6)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = Surname ,width=25)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = DateDue,width=25)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable = Address1, width=25)
        self.txtAddress1.grid(row=5, column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Days On Loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = DaysOnLoan,width=25)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAddress2 = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = Address2, width=25)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Late Return Fine:", padx=2, pady=2)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = LateReturnFine, width=25)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Post Code:", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        self.txtPostCode = Entry(DataFrameLEFT, font=('arial',12,'bold'),  textvariable = Postcode, width=25)
        self.txtPostCode.grid(row=7, column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Date Over Due:", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        self.txtDateOverDue = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = DateOverDue, width=25)
        self.txtDateOverDue.grid(row=7, column=3)

        self.lblMobileNo = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Mobile No:", padx=2, pady=2)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        self.txtMobileNo = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = MobileNo, width=25)
        self.txtMobileNo.grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial',12,'bold'), text ="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable = SellingPrice, width=25)
        self.txtSellingPrice.grid(row=8, column=3)

        #widget 2
        self.txtDisplayR = Text(DataFrameRIGHT, font=('arial',12,'bold'), width=32, height=13, padx=8, pady=20)
        self.txtDisplayR.grid(row=0, column=2)

        #List of of books
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        
        ListOfBooks = ['Computer Network','HTML5 And CSS3 Murach','Artificial Intelligent Approach','Intermediate C++','Operating System','Compiler Construction',
                       'Automata And Computation','Linear Algebra','Machine Learning Approach','Python 3.7','Core Java Concept','Stastistics','Computational Mathematics',
                       'PHP','Biography of Alan Turning']

        def SelectedBook(evt):
            values = str(booklist.get(booklist.curselection()))
            print(values)
            w = values

            if(w == 'Computer Network'):
                BookID.set("ISBN 7478695058")
                BookTitle.set("Computer Network")
                Author.set("Andrew S. Tanenbaum")

                LateReturnFine.set("RS. 2.00")
                SellingPrice.set("Rs. 500")
                DaysOnLoan.set(14)
                iReceipt()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 =(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("Yes")

            elif(w == 'HTML5 And CSS3 Murach'):
                     
                        BookID.set("ISBN 97674390")
                        BookTitle.set("HTML5 And CSS3")
                        Author.set("Joel Murach")

                        LateReturnFine.set("RS. 0.00")
                        SellingPrice.set("Rs. 700")
                        DaysOnLoan.set(7)
                        iReceipt()

                        import datetime
                        d1 = datetime.date.today()
                        d2 = datetime.timedelta(days=7)
                        d3 =(d1 + d2)
                        DateBorrowed.set(d1)
                        DateDue.set(d3)
                        DateOverDue.set("No")

            elif(w == 'Artificial Intelligent Approach'):
                    BookID.set("ISBN 96379455")
                    BookTitle.set("Artificial Intelligent")
                    Author.set("Dr. Khemani")

                    LateReturnFine.set("RS. 0.00")
                    SellingPrice.set("Rs. 1400")
                    DaysOnLoan.set(12)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=12)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("Yes")

            elif(w == 'Intermediate C++'):
                    BookID.set("ISBN 98812906")
                    BookTitle.set("Intermediate C++")
                    Author.set("bjarne stroustrup")

                    LateReturnFine.set("RS. 4.00")
                    SellingPrice.set("Rs. 360")
                    DaysOnLoan.set(0)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=0)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Operating System'):
                    BookID.set("ISBN 42235578")
                    BookTitle.set("Operating System")
                    Author.set("Andrew S. Tanenbaum")

                    LateReturnFine.set("RS. 1.00")
                    SellingPrice.set("Rs. 510")
                    DaysOnLoan.set(3)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=3)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Compiler Construction'):
                    BookID.set("ISBN 20056748")
                    BookTitle.set("Compiler Construction")
                    Author.set("Dr. B V Pawar")

                    LateReturnFine.set("RS.5.00")
                    SellingPrice.set("Rs. 400")
                    DaysOnLoan.set(7)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=7)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("Yes")

            elif(w == 'Automata And Computation'):
                    BookID.set("ISBN 87690578")
                    BookTitle.set("Automata And Computation")
                    Author.set("Dr. Manoj Patil")

                    LateReturnFine.set("RS. 8.00")
                    SellingPrice.set("Rs. 550")
                    DaysOnLoan.set(2)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=2)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Linear Algebra'):
                    BookID.set("ISBN 677867899")
                    BookTitle.set("Linear Algebra")
                    Author.set("Gilbert Strang")

                    LateReturnFine.set("RS. 0.00")
                    SellingPrice.set("Rs. 800")
                    DaysOnLoan.set(9)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=9)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Machine Learning Approach'):
                    BookID.set("ISBN 7766557789")
                    BookTitle.set("Machine Learning Approach")
                    Author.set(" Andriy Burkov")

                    LateReturnFine.set("RS. 7.00")
                    SellingPrice.set("Rs. 900")
                    DaysOnLoan.set(2)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=2)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Python 3.7'):
                    BookID.set("ISBN 12456278")
                    BookTitle.set("Python 3.7")
                    Author.set("Eric Matthes")

                    LateReturnFine.set("RS. 0.00")
                    SellingPrice.set("Rs. 320")
                    DaysOnLoan.set(0)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=0)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Core Java Concept'):
                    BookID.set("ISBN 80060032")
                    BookTitle.set("Core Java Concept")
                    Author.set("Cay S. Horstmann")

                    LateReturnFine.set("RS. 4.00")
                    SellingPrice.set("Rs. 400")
                    DaysOnLoan.set(3)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=3)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Stastistics'):
                    BookID.set("ISBN 78421658")
                    BookTitle.set("Stastistics")
                    Author.set("Trevor Hastie")

                    LateReturnFine.set("RS. 0.00")
                    SellingPrice.set("Rs. 700")
                    DaysOnLoan.set(0)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=0)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Computational Mathematics'):
                    BookID.set("ISBN 56735244")
                    BookTitle.set("Computational Mathematics")
                    Author.set("Charles Wheelan")

                    LateReturnFine.set("RS. 5:00")
                    SellingPrice.set("Rs. 793")
                    DaysOnLoan.set(9)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=9)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'PHP'):
                    BookID.set("ISBN 59469476")
                    BookTitle.set("PHP")
                    Author.set("Joel Murach")

                    LateReturnFine.set("RS. 0.00")
                    SellingPrice.set("Rs. 350")
                    DaysOnLoan.set(0)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=0)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")

            elif(w == 'Biography of Alan Turning'):
                    BookID.set("ISBN 50060078")
                    BookTitle.set("Biography of Alan Turning")
                    Author.set("Alan Turing")

                    LateReturnFine.set("RS. 9.00")
                    SellingPrice.set("Rs. 680")
                    DaysOnLoan.set(6)
                    iReceipt()

                    import datetime
                    d1 = datetime.date.today()
                    d2 = datetime.timedelta(days=6)
                    d3 =(d1 + d2)
                    DateBorrowed.set(d1)
                    DateDue.set(d3)
                    DateOverDue.set("No")
                
        booklist = Listbox(DataFrameRIGHT, width=20, height=12, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END,items)
        #######
        self.lblLabel = Label(FrameDetail,font=('arial',10,'bold'),pady=8,
                              text="Member Type\t Reference No.\t Title\t Firstname\t Surname\t Address 1\t Address 2\t Post Code\t Book Title\t Date Borrowed\t Days On Loan",)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=('arial',12,'bold'), width=141, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)
        

        #Buttons
        self.btnDisplayData = Button(ButtonFrame, text='Display Data',font=('arial',12,'bold'), width=30, bd=4, command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnDelete = Button(ButtonFrame, text='Delete',font=('arial',12,'bold'), width=30, bd=5, command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset = Button(ButtonFrame, text='Reset',font=('arial',12,'bold'), width=30, bd=5, command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit = Button(ButtonFrame, text='Exit',font=('arial',12,'bold'), width=30, bd=5, command=iExit)
        self.btnExit.grid(row=0,column=4)
        
        

if __name__ == "__main__":
    root = Tk()
    application = Library(root)
    root.mainloop()

    
