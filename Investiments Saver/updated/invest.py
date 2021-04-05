from tkinter import *
import sqlite3

root = Tk()
root.title("Investment Management System")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
feedata=[]
def investorData():
   con=sqlite3.connect("invest.db")
   cur =con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS investment(id INTEGER PRIMARY KEY,InvestId,InvestName text,purpose text,amount text,percentage text,date text,moneyReturn text,bonus text,deadline text,cycle text,status text)")
   con.commit()
   con.close()

def addinvestRec(InvestId,InvestName, purpose,amount,percentage, date,moneyReturn,bonus,deadline, cycle,status):
   l=searchData(InvestId)
   if len(l)==1:
      dataUpdate(l[0][0],InvestId,InvestName,purpose,amount,percentage, date,moneyReturn,bonus,deadline, cycle,status)
      return 0
   else:
      con=sqlite3.connect("invest.db")
      cur = con.cursor()
      cur.execute("INSERT INTO investment VALUES( NULL, ?,?,?,?,?,?,?,?,?,?,?)",(InvestId,InvestName,purpose,amount,percentage, date,moneyReturn,bonus,deadline, cycle,status))
      con.commit()
      con.close()
      return 1

def viewData():
   con=sqlite3.connect("invest.db")
   cur = con.cursor()
   cur.execute("SELECT * FROM investment")
   rows =cur.fetchall()
   con.close
   return rows

def editRec(InvestId,status):
   l=searchData(InvestId)
   if len(l)==0:
      return 0
   else:
      con=sqlite3.connect("invest.db")
      cur = con.cursor()
      cur.execute("UPDATE investment SET status=? WHERE InvestId =?",(status,InvestId))
      con.commit()
      con.close()
      return 1

def searchData(InvestId):
   con=sqlite3.connect("invest.db")
   cur = con.cursor()
   cur.execute("SELECT * FROM investment WHERE InvestId=? ",(InvestId,))
   rows=cur.fetchall()
   con.close()
   return rows

def dataUpdate(id,InvestId,InvestName, purpose,amount,percentage, date,moneyReturn,bonus,deadline, cycle,status):
   con=sqlite3.connect("invest.db")
   cur=con.cursor()
   cur.execute("UPDATE investment SET InvestId=?,InvestName=?,purpose=?,amount=?, percentage=?,date=?,moneyReturn=?,bonus=?,deadline=? ,cycle=?,status=? WHERE id=?",(InvestId,InvestName, purpose,amount,percentage, date,moneyReturn,bonus,deadline, cycle,status,id))
   con.commit()
   con.close()

def Home():
	def Clearall():
		investList.delete(0,END)
		investList.insert(END,"          ***Investment Management System By Noor***",str(""))
		
		
	investorData()
	root1 = Toplevel(root)
	root1.attributes('-fullscreen', True) 
	root1.configure(bg='black')
	Label(root1,text="Investment Management System",font=('Helvetica',50,'bold'),bg="black",fg="red",anchor="center").place(x=250,y=20)
	
	scrollbar = Scrollbar(root1)
	scrollbar.place(x=1100,y=150)
	investList=Listbox(root1,width=58,height=24,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
	investList.place(x=750,y=150)
	scrollbar.config(command = investList.yview)
	Clearall()
		
	def Register():
		def check():
			if Id.get() == "" or name.get()=="" or purpose.get()=="" or amount.get() == "" or returnPercentage.get()=="" or date.get()=="" or moneyReturn.get()=="" or bonus.get()=="" or deadline.get()=="" or cycle.get()=="" :
				text.config(text="Please complete the required field!", fg="red")
			else:
				l=addinvestRec(Id.get(),name.get(),purpose.get(),amount.get(),returnPercentage.get(),date.get(),moneyReturn.get(),bonus.get(),deadline.get(),cycle.get(),"Opened")

				if l==0:
					text.config(text="Investment Data Updated", fg="red")
				else:
					text.config(text="Investment Details are Registered Successfully", fg="red")
					Id.set("")
					name.set("")
					purpose.set("")
					amount.set("")
					returnPercentage.set("")
					date.set("")
					moneyReturn.set("")
					bonus.set("")
					deadline.set("")
					cycle.set("")
					passwd.set("")

		window = Toplevel(root)
		window.title("Registration")
		window.geometry("750x500")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id=StringVar()
		name=StringVar()
		purpose = StringVar()
		amount = StringVar()
		returnPercentage=StringVar()
		date = StringVar()
		moneyReturn = StringVar()
		bonus = StringVar()
		deadline = StringVar()
		cycle = StringVar()
		passwd = StringVar()
		
		lblStdID = Label(window, text="Investiment Id: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=20)
		
		txtStdID = Entry(window, text="Noor", textvariable=Id,width=30).place(x=220,y=20)
		lblStdID = Label(window, text="Invester Name: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=60)
		txtStdID = Entry(window, textvariable=name,width=30).place(x=220,y=60)
		lblStdNa = Label(window, text="Purpose of Investment: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=100)
		txtStdNa = Entry(window, textvariable=purpose,width=30).place(x=220,y=100)
		lblStdsn = Label(window, text="Investing Amount: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=140)
		txtStdsn = Entry(window, textvariable=amount,width=30).place(x=220,y=140)
		lblStddob = Label(window,text="% returns on Investiment:", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=180)
		txtStddob = Entry(window,textvariable=returnPercentage,width=30).place(x=220,y=180)
		lblStdgen = Label(window,text="Date of Investment : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=220)
		txtStdgen = Entry(window, textvariable=date,width=30).place(x=220,y=220)
		lblStdage = Label(window, text="Monthly Money Returns: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=260)
		txtStdage = Entry(window, textvariable=moneyReturn,width=30).place(x=220,y=260)
		lblStdfee = Label(window, text="Bonus: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=300)
		txtStdfee = Entry(window, textvariable=bonus,width=30).place(x=220,y=300)
		lblStdfp = Label(window, text="DeadLine: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=340)
		txtStdfp = Entry(window, textvariable=deadline,width=30).place(x=220,y=340)
		lblStdmob = Label(window, text="      Monthly Cycle: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=20,y=380)
		txtStdmob = Entry(window, textvariable=cycle,width=30).place(x=220,y=380)
		submit = Button(window, text="submit", bg='bisque3' ,command = lambda:[check(),window.deiconify()])
		submit.place(x=250,y=460)
		window.mainloop()
		
		
		
	def DisplayData():
         investList.delete(0,END)
         l=viewData()
         if len(l)==0:
         	l=[("No data In DataBase. DataBase is Empty.")]
         for row in l:
            investList.insert(END,row,str(" "))	
            
	
	def DisplayOne():
		Clearall()
		def Dis(StdId):
			l=["","Investment Id  -------------> :","Investment Name ------------> : ","Purpose  -------------------> : ","Invested Amount ------------> : ","Retrun Percentage ----------> :","Date of Investment ---------> :  ","Monthly Money Return  ------> : ","Bonus   --------------------> : ","Return money in 1 cycle ----> :","Total Amount after 1 cycle -->:"]
			t=("","","","","","","","","","","","")
			investList.delete(0,END)
			l1=searchData(StdId)
			if len(l1)==0:
				investList.insert(END,"The Investment Id "+StdId+" is not found",str(" "))
			else:
				for row in l1:
					investList.insert(END,str(" "))
					if row[-1]=="Closed":
						l=["The Investment with id "+StdId+" is closed.","Please reopen to see Investment Details"]
						for row in l:
							investList.insert(END,row,str(" "))	
					else:
						for i in range(1,len(row)):
							if i==9:
								investList.insert(END,l[i]+"  "+str((int(row[5])/100)*(int(row[4]))),str(""))
								investList.insert(END,l[i]+"  "+str(((int(row[5])/100)*(int(row[4])))+int(row[4])+int(row[8])),str(""))
								break
							else:
								investList.insert(END,l[i]+"  "+str(row[i]),str(""))
							
		window = Toplevel(root1)
		window.title("Search Investment Details")
		window.geometry("450x200")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id = StringVar()
		Label(window, text="Enter Investment Id to Delete  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=30)
		lblStdID = Label(window, text="Investment Id : ", font=('arial', 18, 'bold'),bg="bisque2").place(x=20,y=70)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=180,y=75)
		submit = Button(window, text="submit", bg='bisque3',command=lambda:Dis(Id.get())  )
		submit.place(x=180,y=120)
		window.mainloop()

		
	def Edit(status):	
		Clearall()
		def Del1(InvestId,status):
			l=editRec(InvestId,status)
			investList.delete(0,END)
			if l==1:
				investList.insert(END,"Investment with Id "+InvestId+" "+ status+" Successfully.",str(""))
			else:
				investList.insert(END,"Investment with Id "+InvestId+" is not found to delete.",str(""))
		window = Toplevel(root1)
		window.title("Delete Investment Data")
		window.geometry("450x200")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id = StringVar()
		Label(window, text="Enter Investment Id to Delete  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=30)
		lblStdID = Label(window, text="Investment Id : ", font=('arial', 18, 'bold'),bg="bisque2").place(x=20,y=70)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=180,y=75)
		submit = Button(window, text="submit", bg='bisque3',command=lambda:Del1(Id.get(),status))
		submit.place(x=180,y=120)
		window.mainloop()
			
		
	b = Button(root1, text="ADD or UPDATE\nInvestment", bg='bisque3',command=Register)
	b.place(x=150,y=150,height=90,width=200)

	b1 = Button(root1, text="GET \nInvestment\nData", bg='red',command=DisplayOne)
	b1.place(x=500,y=150,height=90,width=200)

	b2 = Button(root1, text="Display all\nInvestments ", bg='blue',command=DisplayData)
	b2.place(x=150,y=350,height=90,width=200)
	
	b3 = Button(root1, text="Close \nInvestment", bg='orange',command=lambda:Edit("Closed"))
	b3.place(x=500,y=350,height=90,width=200)

	b4 = Button(root1, text="ReOpen \nInvestment", bg='blue',command=lambda:Edit("Opened"))
	b4.place(x=150,y=550,height=90,width=200)
	
	

	b5 = Button(root1, text="Clear", bg='violet', command=Clearall)
	b5.place(x=500,y=550,height=90,width=200)

	b0 = Button(root1, text="Exit",bg='red', command=lambda:[root1.destroy(),root.deiconify(),USERNAME.set(""),PASSWORD.set("") ])

	b0.place(x=290,y=700,height=50,width=250)

	
	root1.mainloop()
	

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()
    
def Login(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
            Home()
            
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
        cursor.close()
    conn.close()

 

USERNAME = StringVar()
PASSWORD = StringVar()


Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)


lbl_title = Label(Top, text = "Investor Login", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

USERNAME.set("")
PASSWORD.set("") 
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)


btn_login = Button(Form, text="Login", width=45, command=Home)
btn_login.grid(pady=5, row=3, columnspan=2)
btn_login.bind('<Return>', Login)
btn_exit = Button(Form, text="Exit", width=45, command=root.destroy)
btn_exit.grid(pady=5, row=4, columnspan=5)
root.mainloop()
