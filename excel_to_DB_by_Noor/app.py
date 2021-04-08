from flask import Flask, render_template, request, flash,redirect, url_for
from werkzeug.utils import secure_filename
import os
import openpyxl
import sqlite3
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "fjsadf"
def CreateDB(name,dbstr):
   con=sqlite3.connect("DB/"+name+".db")
   cur =con.cursor()
   cur.execute("DROP TABLE IF EXISTS "+name)
   cur.execute(dbstr)
   con.commit()
   con.close()

def searchData(name,searchstr):
   con=sqlite3.connect("DB/"+name+".db")
   cur = con.cursor()
   cur.execute(searchstr)
   rows=cur.fetchall()
   #print(rows)
   con.close()
   return rows

def viewData(name):
   con=sqlite3.connect("DB/"+name+".db")
   cur = con.cursor()
   cur.execute("SELECT * FROM "+name)
   rows =cur.fetchall()
   con.close
   return rows
   
def getColumns(name):
   con=sqlite3.connect("DB/"+name)
   cur = con.cursor()
   cur.execute("SELECT * FROM "+name[0:-3])
   rows =cur.fetchone()
   #names=rows.keys()
   con.close
   return [member[0] for member in cur.description]

def addData(name,insert):
	con=sqlite3.connect("DB/"+name+".db")
	cur = con.cursor()
	cur.execute(insert)
	con.commit()
	con.close()

def insertStr(l,l2,insert):
	for i in l:
		insert=insert+i+","
	insert=insert[0:-1]
	insert=insert+") VALUES ("
	for i in l2:
		insert=insert+"'"+str(i)+"',"
	insert=insert[0:-1]
	insert=insert+")"
	return insert
	
def searchStr(l,l2,searchstr):
	l1=[]
	for i in range(len(l)):
		l1.append(searchstr+str(l[i])+"='"+str(l2)+"'")
	return l1
@app.route('/')
def index():
	path = os.getcwd()
	files = os.listdir(path+"/DB")
	return render_template('index.html',colours=files)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		path = os.getcwd()
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
		files = os.listdir(path+"/DB")
		process(f.filename)
		flash('File uploaded!')
		return render_template('index.html',colours=files)

def process(s):
	l=[]
	l1=[[],[]]
	D={}
	path = os.getcwd()
	s=s.replace(' ','_')
	book = openpyxl.load_workbook(path+'/uploads/'+s)
	sheet = book.active
	cols=sheet.columns
	#print(cols)
	insert="INSERT INTO "+s[0:-5]+"("
	dbstr="CREATE TABLE IF NOT EXISTS "+s[0:-5]+"(id INTEGER PRIMARY KEY,"
	searchstr="SELECT * FROM "+s[0:-5]+" WHERE "
	rows=sheet.rows
	#name.append(s[0:-5])
	#print(rows)
	for row in rows:
		for cell in row:
			l.append(cell.value)
		break
	#print(l)
	for i in l:
		l1[0].append(i.replace(' ','_')+" TEXT")
		l1[1].append(i.replace(' ','_'))
	for i in range (len(l1[0])):
		dbstr=dbstr+l1[0][i]+","
	dbstr=dbstr[0:-1]
	dbstr=dbstr+")"
	print(dbstr)
	print(s)
	CreateDB(s[0:-5],dbstr)
	
	for row in rows:
		l2=[]
		for cell in row:
			l2.append((cell.value))
		addstr=insertStr(l1[1],l2,insert)
		addData(s[0:-5],addstr)
		#print(addstr)
	viewData(s[0:-5])
	


@app.route('/search', methods=['GET', 'POST'])
def search():
	select = request.form.get('colours')
	cols=getColumns(select)
	#print(cols)
	searchstr="SELECT * FROM "+select[0:-3]+" WHERE "
	select = request.form.get('colours')
	searchterm =request.form['pay']
	x=searchStr(cols,searchterm,searchstr)
	data=[]
	#print(x,cols)
	for i in range(len(x)):
		xyz=searchData(select[0:-3],x[i])
		data.append("\nSearch Result in column "+cols[i])
		for j in xyz:
			datastr=''
			for k in j:
				datastr=datastr+str(k)+"  "
			data.append(datastr)
		if len(xyz)==0:
			datastr="No data found in this column\n"
		else:
			datastr=" \n "
		data.append(datastr)
	if len(data)==0:
		data=["No data Found with search term "+searchterm]
	return render_template('index.html',lists=data)
    

	
		
if __name__ == '__main__':
   app.run(debug = True)
   
