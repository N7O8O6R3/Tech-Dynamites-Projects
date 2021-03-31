


# Created By Noor Hasan Shaik
# Investments Saver


from tkinter import *
import ast
import os

root = Tk()
root.title("Investiments")
width = 400
height = 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
lines = []
def create():
	if os.stat("data.txt").st_size == 0:
			l=['',' ', ' ',' ',' ',' ',' ',' ',' ',' ','']
			file1= open("data.txt","a")
			file1.write(str(l)+"\n")
def getData():
	with open("data.txt") as f:
		for line in f:
			line = line.strip()
			lines.append(line)
	for i in range(len(lines)):
		lines[i]=ast.literal_eval(lines[i])

def check2(x,y):
	log=-1
	for i in range(len(lines)):
		if lines[i][0]==x and lines[i][-2]==y:
			log=i
			break
	return log
 	

def Register(i):
	def check():
		if Id.get() == "" or name.get()=="" or purpose.get()=="" or amount.get() == "" or returnPercentage.get()=="" or date.get()=="" or moneyReturn.get()=="" or bonus.get()=="" or deadline.get()=="" or cycle.get()=="" or passwd.get()=="":
			text.config(text="Please complete the required field!", fg="red")
		else:
			l=[Id.get(),name.get(),purpose.get(),amount.get(),returnPercentage.get(),date.get(),moneyReturn.get(),bonus.get(),deadline.get(),cycle.get(),passwd.get(),"open"]
	
			file1= open("data.txt","a")
			x=check2(Id.get(),passwd.get())
			if (x!=-1):
				file2= open("data.txt","r")
				a=file2.readlines()
				a[i]=str(l)+"\n"
				file2= open("data.txt","w")
				file2.writelines(a)
				file2.close()
				lines[i]=l
				text.config(text="Invester Details are Updated Successfully", fg="red")
				
			else:
				text.config(text="Invester Details are Registered Successfully", fg="red")
				file1.write(str(l)+"\n")
				lines.append(l)
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
			file1.close

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
	
	lblStdID = Label(window, text="Invester Id: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=20)
	Id.set(lines[i][0])
	
	txtStdID = Entry(window, text="Noor", textvariable=Id,width=30).place(x=220,y=20)
	lblStdID = Label(window, text="Invester Name: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=60)
	name.set(lines[i][1])
	txtStdID = Entry(window, textvariable=name,width=30).place(x=220,y=60)
	lblStdNa = Label(window, text="Purpose of Investment: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=100)
	purpose.set(lines[i][2])
	txtStdNa = Entry(window, textvariable=purpose,width=30).place(x=220,y=100)
	lblStdsn = Label(window, text="Investing Amount: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=140)
	amount.set(lines[i][3])
	txtStdsn = Entry(window, textvariable=amount,width=30).place(x=220,y=140)
	lblStddob = Label(window,text="% returns on Investiment:", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=180)
	returnPercentage.set(lines[i][4])
	txtStddob = Entry(window,textvariable=returnPercentage,width=30).place(x=220,y=180)
	lblStdgen = Label(window,text="Date of Investment : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=220)
	date.set(lines[i][5])
	txtStdgen = Entry(window, textvariable=date,width=30).place(x=220,y=220)
	lblStdage = Label(window, text="Monthly Money Returns: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=260)
	moneyReturn.set(lines[i][6])
	txtStdage = Entry(window, textvariable=moneyReturn,width=30).place(x=220,y=260)
	lblStdfee = Label(window, text="Bonus: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=300)
	bonus.set(lines[i][7])
	txtStdfee = Entry(window, textvariable=bonus,width=30).place(x=220,y=300)
	lblStdfp = Label(window, text="DeadLine: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=340)
	deadline.set(lines[i][8])
	txtStdfp = Entry(window, textvariable=deadline,width=30).place(x=220,y=340)
	lblStdmob = Label(window, text="      Monthly Cycle: ", font=('arial', 10, 'bold'),bg="bisque2").place(x=20,y=380)
	cycle.set(lines[i][9])
	txtStdmob = Entry(window, textvariable=cycle,width=30).place(x=220,y=380)
	lblStdadd = Label(window, text="Create Password :", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=420)
	passwd.set(lines[i][10])
	txtStdadd = Entry(window, textvariable=passwd,show="*", width=30).place(x=220,y=420)
	submit = Button(window, text="submit", bg='bisque3' ,command = lambda:[check(),window.deiconify()])
	submit.place(x=250,y=460)
	window.mainloop()
	


def Home(x):
	def Close():
		file2= open("data.txt","r")
		a=file2.readlines()
		l=lines[x]
		l[-1]="close"
		a[x]=str(l)+"\n"
		file2= open("data.txt","w")
		file2.writelines(a)
		file2.close()
		lines[x]=l
		window.destroy()
		
	window = Toplevel(root)
	window.title("Investiment Details")
	window.geometry("650x500")
	window.configure(bg='bisque2')
	window.resizable(True, True)
	lbl=Frame(window)
	lbl.pack()
	text = Label(lbl)
	text.grid(row=2,columnspan=2)
	
	lblID = Label(window, text="Invester Id : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=20)
	lblID = Label(window, text=": "+lines[x][0], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=20)
	
	lblname = Label(window, text="Invester Name :", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=60)
	lblname = Label(window, text=": "+lines[x][1], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=60)
	
	lblpurpose = Label(window, text="Purpose of Investiment : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=100)
	lblpurpose = Label(window, text=": "+lines[x][2], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=100)
	
	lblamount = Label(window, text="Invested Amount : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=140)
	lblamount = Label(window, text=": "+lines[x][3], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=140)
	
	lblreturns = Label(window, text="Return Percentage : ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=180)
	lblreturns = Label(window, text=": "+lines[x][4], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=180)
	
	lbldate = Label(window, text="Date of Investiment ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=220)
	lbldate = Label(window, text=": "+lines[x][5], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=220)
	
	lblmoney = Label(window, text="Monthly money return ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=260)
	lblmoney = Label(window, text=": "+lines[x][6], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=260)
	
	lblbonus = Label(window, text="Bonus :", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=300)
	lblbonus = Label(window, text=": "+lines[x][7], font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=300)
	
	lbldeadline = Label(window, text="Return Money in one Cycle ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=340)
	val=(int(lines[x][4])/100)*(int(lines[x][3]))
	lbldeadline = Label(window, text=": "+str(val), font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=340)
	
	lblcycle = Label(window, text="Total amount after 1 cycle ", font=('arial', 10, 'bold'),bg="bisque2").place(x=50,y=380)
	lblcycle = Label(window, text=": "+str(int(lines[x][3])+val+int(lines[x][7])), font=('arial', 10, 'bold'),bg="bisque2").place(x=220,y=380)
	edit = Button(window, text="Edit", bg='bisque3' , command = lambda:[window.destroy(),Register(x)])
	edit.place(x=250,y=460)
	
	close = Button(window, text="Close Investiment", bg='bisque3' ,command = Close)
	close.place(x=320,y=460)
	


def Home1(x):
	def Open():
		file2= open("data.txt","r")
		a=file2.readlines()
		l=lines[x]
		l[-1]="open"
		a[x]=str(l)+"\n"
		file2= open("data.txt","w")
		file2.writelines(a)
		file2.close()
		lines[x]=l	
		window.destroy()
					
	window = Toplevel(root)
	window.title("Registration")
	window.geometry("600x200")
	window.configure(bg='bisque2')
	window.resizable(True, True)
	lbl=Frame(window)
	lbl.pack()
	text = Label(lbl)
	text.grid(row=2,columnspan=2)
	lblID = Label(window, text="THis Investiment is Closed \nTo reopen click on the reopen ", font=('arial', 25, 'bold'),bg="bisque2").place(x=50,y=20)
	reopen = Button(window, text="ReOpen", bg='bisque3' ,command=Open)
	reopen.place(x=250,y=130)

def Login(event=None):
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
    	log=check2(USERNAME.get(),PASSWORD.get())
    	if (log != -1):
    		USERNAME.set("")
    		PASSWORD.set("")
    		lbl_text.config(text="")
    		if lines[log][-1]=="close":
    			Home1(log)
    		else:
	    		Home(log)
    	else:
    		lbl_text.config(text="Invalid username or password", fg="red")
    		USERNAME.set("")
    		PASSWORD.set("")   
    
    
USERNAME = StringVar()
PASSWORD = StringVar()


Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

create()
getData()

lbl_title = Label(Top, text = "Invester Management System", font=('arial', 15))
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

btn_register = Button(Form, text="Register", width=45, command=lambda:[Register(0)])
btn_register.grid(pady=5, row=4, columnspan=5)

btn_exit = Button(Form, text="Exit", width=45, command=root.destroy)
btn_exit.grid(pady=5, row=5, columnspan=6)
root.mainloop()
