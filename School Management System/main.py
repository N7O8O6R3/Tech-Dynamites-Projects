from tkinter import *
import sqlite3

root = Tk()
root.title("Student Management System")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
feedata=[]
def studentData():
   con=sqlite3.connect("student.db")
   cur =con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,StdID text,Firstname text,Surname text,DoB text, \
      Age text,Gender text,TotalFee text,FeePaid text,Mobile text,Address text)")
   con.commit()
   con.close()

def addStdRec(StdID, Firstname,Surname,DoB, Age,Gender,Tfee,feepaid, Address, Mobile):
   l=searchData(StdID)
   if len(l)==1:
      dataUpdate(l[0][0],StdID, Firstname,Surname,DoB, Age,Gender,Tfee,feepaid, Address, Mobile)
      return 0
   else:
      con=sqlite3.connect("student.db")
      cur = con.cursor()
      cur.execute("INSERT INTO student VALUES( NULL, ?,?,?,?,?,?,?,?,?,?)",(StdID, Firstname,Surname,DoB, Age,Gender,Tfee,feepaid,  Mobile,Address))
      con.commit()
      con.close()
      return 1

def viewData():
   con=sqlite3.connect("student.db")
   cur = con.cursor()
   cur.execute("SELECT * FROM student")
   rows =cur.fetchall()
   con.close
   return rows

def deleteRec(StdId):
   l=searchData(StdId)
   if len(l)==0:
      return 0
   else:
      con=sqlite3.connect("student.db")
      cur = con.cursor()
      cur.execute("DELETE FROM student WHERE StdID =?",(StdId,))
      con.commit()
      con.close()
      return 1

def searchData(StdId):
   con=sqlite3.connect("student.db")
   cur = con.cursor()
   cur.execute("SELECT * FROM student WHERE StdID=? ",(StdId,))
   rows=cur.fetchall()
   con.close()
   return rows

def dataUpdate(id,StdID, Firstname,Surname,DoB, Age,Gender,Tfee,feepaid, Address, Mobile):
   con=sqlite3.connect("student.db")
   cur=con.cursor()
   cur.execute("UPDATE student SET StdID=?,Firstname=?,Surname=?,DoB=?, Age=?,Gender=?,TotalFee=?,FeePaid=?,Mobile=? ,Address=? WHERE id=?",(StdID,Firstname, Surname, DoB, Age, Gender,Tfee,feepaid, Address, Mobile,id))
   con.commit()
   con.close()

	
def Home():
	def Clearall():
		studentList.delete(0,END)
		studentList.insert(END,"             ***School Management System By Noor***",str(""))
		
		
	studentData()
	root1 = Toplevel(root)
	root1.attributes('-fullscreen', True) 
	root1.configure(bg='black')
	Label(root1,text="School Management System",font=('Helvetica',50,'bold'),bg="black",fg="red",anchor="center").place(x=250,y=20)
	
	scrollbar = Scrollbar(root1)
	scrollbar.place(x=1100,y=150)
	studentList=Listbox(root1,width=58,height=24,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
	studentList.place(x=750,y=150)
	scrollbar.config(command = studentList.yview)
	Clearall()
		
	def Register():
		Clearall()
		def check():
			if Id.get() == "" or name.get()=="" or surname.get()=="" or Tfee.get() == "" or DoB.get()=="" or Age.get()=="" or Gender.get()=="" or Address.get()=="" or Mobile.get()=="" or feepaid.get()=="":
				text.config(text="Please complete the required field!", fg="red")
			else:
				l=addStdRec(Id.get(),name.get(),surname.get(),DoB.get(),Gender.get(),Age.get(),Tfee.get(),feepaid.get(),Address.get(),Mobile.get())

				if l==0:
					text.config(text="Student Data Updated", fg="red")
				else:
					text.config(text="Student Details are Registered Successfully", fg="red")
				Id.set("")
				name.set("")
				surname.set("")
				Tfee.set("")
				DoB.set("")
				Age.set("")
				Gender.set("")
				Address.set("")
				Mobile.set("")
				feepaid.set("")
				

		window = Toplevel(root1)
		window.title("Registration")
		window.geometry("750x500")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id=StringVar()
		name = StringVar()
		surname = StringVar()
		Tfee=StringVar()
		DoB = StringVar()
		Age = StringVar()
		Gender = StringVar()
		Address = StringVar()
		Mobile = StringVar()
		feepaid = StringVar()
		
		lblStdID = Label(window, text="Student Id     : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=20)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=200,y=20)
		lblStdNa = Label(window, text="First Name    : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=60)
		txtStdNa = Entry(window, textvariable=name,width=30).place(x=200,y=60)
		lblStdsn = Label(window, text="  Surname     : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=100)
		txtStdsn = Entry(window, textvariable=surname,width=30).place(x=200,y=100)
		lblStddob = Label(window,text="     DOB        : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=140)
		txtStddob = Entry(window,textvariable=DoB,width=30).place(x=200,y=140)
		lblStdgen = Label(window,text="   Gender      : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=180)
		txtStdgen = Entry(window, textvariable=Gender,width=30).place(x=200,y=180)
		lblStdage = Label(window, text="     Age         : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=220)
		txtStdage = Entry(window, textvariable=Age,width=30).place(x=200,y=220)
		lblStdfee = Label(window, text="  Total Fee    : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=260)
		txtStdfee = Entry(window, textvariable=Tfee,width=30).place(x=200,y=260)
		lblStdfp = Label(window, text="   Fee Paid     : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=300)
		txtStdfp = Entry(window, textvariable=feepaid,width=30).place(x=200,y=300)
		lblStdmob = Label(window, text="Mobile Number  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=340)
		txtStdmob = Entry(window, textvariable=Mobile,width=30).place(x=200,y=340)
		lblStdadd = Label(window, text="   Address     : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=50,y=380)
		txtStdadd = Entry(window, textvariable=Address,width=30).place(x=200,y=380)
		submit = Button(window, text="submit", bg='bisque3' , command = lambda:[check(),window.deiconify()])
		submit.place(x=250,y=450)
		window.mainloop()
		
		
		
	def DisplayData():
         studentList.delete(0,END)
         l=viewData()
         if len(l)==0:
         	l=[("No data In DataBase. DataBase is Empty.")]
         for row in l:
            studentList.insert(END,row,str(" "))	
            
	
	
	def PayFee():
		Clearall()
		def Dis(StdId,Fee):
			studentList.delete(0,END)
			l1=searchData(StdId)
			if len(l1)==0:
				studentList.insert(END,"Student with Id "+StdId+" is not found.",str(""))
			else:
				l1[0]=list(l1[0])
				if int(l1[0][7])>int(l1[0][8]):
					l1[0][8]=str(int(l1[0][8])+int(Fee))
					if int(l1[0][7])<int(l1[0][8]):
						studentList.insert(END,"You are paying Morethan your Fee.",str(""))
						studentList.insert(END,"Fee you need to pay    : "+str(int(l1[0][7])-int(l1[0][8])+int(Fee)),str(""))
						
					else:
						l1[0]=tuple(l1[0])
						dataUpdate(l1[0][0],l1[0][1],l1[0][2],l1[0][3],l1[0][4],l1[0][5],l1[0][6],l1[0][7],l1[0][8], l1[0][9], l1[0][10])
						studentList.insert(END,"Fee Paid",str(""))
						studentList.insert(END,"Total Fee         : "+str(l1[0][7]),str(""))
						studentList.insert(END,"Fee Paid today    : "+str(Fee),str(""))
						studentList.insert(END,"Fee Paid till now : "+str(l1[0][8]),str(""))
						studentList.insert(END,"Remaining Fee     : "+str(int(l1[0][7])-int(l1[0][8])),str(""))
				else:
					studentList.insert(END,"You paid all your Fee.",str(""))

		window = Toplevel(root1)
		window.title("Pay Fee")
		window.geometry("500x200")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id = StringVar()
		Fee = StringVar()
		Label(window, text="Enter Student Id to Pay Fee  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=30)
		lblStdID = Label(window, text="Student Id : ", font=('arial', 20, 'bold'),bg="bisque2").place(x=20,y=70)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=200,y=75)
		lblStdFee = Label(window, text="Enter Fee to pay : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=100)
		txtStdFee = Entry(window, textvariable=Fee,width=30).place(x=200,y=100)
		submit = Button(window, text="submit", bg='bisque3' ,command=lambda:Dis(Id.get(),Fee.get()) )
		submit.place(x=180,y=150)
		
		window.mainloop()
		
	def DisplayOne():
		Clearall()
		def Dis(StdId):
			l=["","Student Id    \t\t: ","Name           \t\t: ","Surname     \t  : ","Date of Birth \t: ","Gender    \t\t    : ","Age    \t \t \t      : ","Total Fee  \t\t   : ","Fee Paid    \t\t  : ","Remaining Fee : ","Mobile Number : ","Address   \t\t    : "]
			t=("","","","","","","","","","","","")
			studentList.delete(0,END)
			l1=searchData(StdId)
			if len(l1)==0:
				l1.append(t)
				
			for row in l1:
				studentList.insert(END,str(" "))
				for i in range(1,len(row)):
					if i==9 and row[7]!="":
						studentList.insert(END,l[i]+"  "+str(int(row[7])-int(row[8])),str(""))
						studentList.insert(END,l[i+1]+"  "+str(row[i]),str(""))
						studentList.insert(END,l[i+2]+"  "+str(row[i+1]),str(""))
						break
					else:
						studentList.insert(END,l[i]+"  "+str(row[i]),str(""))
					
		window = Toplevel(root1)
		window.title("Search Student Details")
		window.geometry("450x200")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id = StringVar()
		Label(window, text="Enter Student Id to Delete  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=30)
		lblStdID = Label(window, text="Student Id : ", font=('arial', 20, 'bold'),bg="bisque2").place(x=20,y=70)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=180,y=75)
		submit = Button(window, text="submit", bg='bisque3',command=lambda:Dis(Id.get())  )
		submit.place(x=180,y=120)
		window.mainloop()

		
	def DElete():	
		Clearall()
		def Del1(StdId):
			l=deleteRec(StdId)
			studentList.delete(0,END)
			if l==1:
				studentList.insert(END,"Student with Id "+StdId+" deleted Successfully.",str(""))
			else:
				studentList.insert(END,"Student with Id "+StdId+" is not found to delete.",str(""))
		window = Toplevel(root1)
		window.title("Delete Student Data")
		window.geometry("450x200")
		window.configure(bg='bisque2')
		window.resizable(True, True)
		lbl=Frame(window)
		lbl.pack()
		text = Label(lbl)
		text.grid(row=2,columnspan=2)
		Id = StringVar()
		Label(window, text="Enter Student Id to Delete  : ", font=('arial', 15, 'bold'),bg="bisque2").place(x=20,y=30)
		lblStdID = Label(window, text="Student Id : ", font=('arial', 20, 'bold'),bg="bisque2").place(x=20,y=70)
		txtStdID = Entry(window, textvariable=Id,width=30).place(x=180,y=75)
		submit = Button(window, text="submit", bg='bisque3',command=lambda:Del1(Id.get())  )
		submit.place(x=180,y=120)
		window.mainloop()
			
		
	b = Button(root1, text="Register \n or \nUpdate", bg='bisque3',command=Register)
	b.place(x=150,y=150,height=90,width=200)

	b1 = Button(root1, text="Search", bg='red',command=DisplayOne)
	b1.place(x=500,y=150,height=90,width=200)

	b2 = Button(root1, text="Display", bg='blue',command=DisplayData)
	b2.place(x=150,y=350,height=90,width=200)

	b3 = Button(root1, text="Pay Fee", bg='green',command=PayFee)
	b3.place(x=500,y=350,height=90,width=200)

	b4 = Button(root1, text="Delete", bg='orange',command=DElete)
	b4.place(x=150,y=550,height=90,width=200)

	b5 = Button(root1, text="Clear", bg='violet', command=Clearall)
	b5.place(x=500,y=550,height=90,width=200)



	b0 = Button(root1, text="Exit",bg='red', command=lambda:[root1.destroy(),root.deiconify()])

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


lbl_title = Label(Top, text = "School Management System", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)


username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)


btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=5, row=3, columnspan=2)
btn_login.bind('<Return>', Login)
btn_exit = Button(Form, text="Exit", width=45, command=root.destroy)
btn_exit.grid(pady=5, row=4, columnspan=5)
root.mainloop()
