import json
from web3 import Web3
import datetime
from flask import Flask, jsonify, request, redirect, url_for, render_template, flash, session
import requests
from uuid import uuid4
from urllib.parse import urlparse
import sys

ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))

if((web3.isConnected())):
	print("You connected to Ganache")
else:
	print("Connection Failed")
	
web3.eth.defaultAccount = web3.eth.accounts[0]
block=web3.eth.blockNumber

abi = json.loads('[{"constant":true,"inputs":[{"name":"_adhar","type":"uint256"}],"name":"getData","outputs":[{"components":[{"name":"name","type":"string"},{"name":"dob","type":"string"},{"name":"gmail","type":"string"},{"name":"passwd","type":"string"},{"name":"Type","type":"string"},{"name":"voted","type":"bool"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"}],"name":"RegisterCandidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_name","type":"string"}],"name":"getResult","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_adhar","type":"uint256"},{"name":"_name","type":"string"},{"name":"_passwd","type":"string"},{"name":"_type","type":"string"},{"name":"_date","type":"string"},{"name":"_gmail","type":"string"}],"name":"RegisterVoter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"result","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_adhar","type":"uint256"}],"name":"Vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"VoteResult","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
address  = "0x0D0D32fdDCf67272E911Fc4F2D9949b3Fa09295C"

userdata ={'123456789012': ['Noor', '1234', 'Organizer', 'male', '20-02-2002', 'shaiknoorhasan@gmail.com']}
l1=[]
voterID=['','']
candidates_list = ["CSE","ECE","MECH","CIVIL"]


contract = web3.eth.contract(address=address,abi=abi)


for i in candidates_list:
	tx_hash=contract.functions.RegisterCandidate(i).transact()
	tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)
tx_hash=contract.functions.RegisterVoter(123456789012,"Noor","1234","Organizer","2002-02-20","shaiknoorhasan786@gmail.com").transact()
tx_receipt=web3.eth.waitForTransactionReceipt(tx_hash)

def calculateAge(birthDate): 
    today = datetime.date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 
    


app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/',methods=['GET','POST'])
def home():
	if 'logged_in' in session:
		return render_template('vote.html')
	else:
		return render_template('index.html')


@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register1.html')
	else:
		l=[]
		d={}
		adhar = request.form['adhar']
		Type = request.form['RegType']
		name = request.form['user_name']
		gend = request.form['gend']
		bday = request.form['birthday']
		mail = request.form['user_email']
		passw = request.form['user_pass']
		l.extend([name,passw,Type,gend,bday,mail])
		age=calculateAge(datetime.date(int(bday[0:4]),int(bday[5:7]),int(bday[8:10])))
		d['adhar']=adhar
		d['name']=name
		d['passw']=passw
		d['Type']=Type
		d['gend']=gend
		d['bday']=bday
		d['mail']=mail
		if adhar in userdata:
			return render_template('register1.html',error="The Adhar Number already registered")
		elif mail in l1:
			return render_template('register1.html',error="The Email already in Use")
		elif age<18:
			return render_template('register1.html',error="Your age is not eligible to vote")
		else:
			tx_hash=contract.functions.RegisterVoter(int(adhar),name,passw,Type,bday,mail).transact()
			web3.eth.waitForTransactionReceipt(tx_hash)
			userdata[adhar]=l
			l1.append(mail)
			return render_template('register.html')
			
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login1.html')	
	else:
		Type = request.form['logType']
		name = request.form['user_name']
		adhar = request.form['adhar']
		passw = request.form['user_pass']
		cdata = contract.functions.getData(int(adhar)).call()
		if cdata[1] != '':
			if passw == cdata[3] and Type==cdata[4] and name == cdata[0]:
				if Type == 'Organizer':
					session['logged_in'] = True
					return redirect(url_for('get_result'))
				else:
					userId = adhar
					session['logged_in'] = True
					voterID[0]=userId
					voterID[1]=name
					return redirect(url_for('vote',user=userId))
			else:
				return render_template('login1.html',error= "Invalid Username or Password")
		else:	
			return render_template('login1.html',error = "No records found")

@app.route('/logout',methods=['GET','POST'])
def logout():
	session.pop('logged_in',None)
	return redirect(url_for('home'))
	
	
@app.route('/vote',methods=['GET','POST'])
def vote():
	if request.method == 'GET':
		return render_template('vote.html',user=voterID[1])
	else:
		candidate= request.form['optradio']
		voterId = voterID[0]
		if candidate in candidates_list:
			tx_hash3 = contract.functions.Vote(candidate,int(voterId)).transact()
			web3.eth.waitForTransactionReceipt(tx_hash3)
			msg = contract.functions.VoteResult().call()
			if msg == "True":
				return render_template('success.html',flag=1,candidateId = candidate,user=voterId),200	
			else:
				return render_template('success.html',flag=0,user=voterID[1])
		else:
			return render_template('success.html',flag=0,user=voterID[1])
		
@app.route('/admin',methods = ['GET','POST'])
def get_result():
	finalResult={}
	for i in candidates_list:
		finalResult[i]=contract.functions.getResult(i).call()
		
	if 'logged_in' not in session:
		return redirect(url_for('login'))
	else:
		return render_template('admin.html',data = finalResult,flag =1)



if __name__ == '__main__':
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument('-H', '--host', default='127.0.0.1')
	parser.add_argument('-p', '--port', default=5000, type=int)
	args = parser.parse_args()
	
	app.run(host=args.host, port=args.port, debug=True)
		



	
