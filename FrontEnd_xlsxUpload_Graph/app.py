from flask import Flask, render_template, request, flash,redirect, url_for
from werkzeug.utils import secure_filename
import os
import openpyxl
import matplotlib.pyplot as plt

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "fjsadf"
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		path = os.getcwd()
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
		print(app.config['UPLOAD_FOLDER'] ,f.filename)
      
		files = os.listdir(path+"/uploads")
		print(files)
		process(f.filename)
		s=f.filename
		flash('File uploaded!')
		return render_template('index.html',colours=files)

def process(s):
	l=[]
	D={}
	path = os.getcwd()
	book = openpyxl.load_workbook(path+'/uploads/'+s)
	print("hi")
	sheet = book.active
	cols=sheet.columns
	for col in cols:
		for cell in col:
			if cell.value:
				l.append(cell.value)
	D = {i:l.count(i) for i in l}
	print(D)
	plt.rcParams["figure.figsize"] = (14, 7)
	plt.bar(D.keys(),D.values())
	
	for index, value in enumerate(list(D.values())):
		plt.text(index, value, str(value))

	mng = plt.get_current_fig_manager()
	mng.full_screen_toggle()
	plt.savefig(path+"/static/"+s[:-5]+'.png',dpi=600)
	
'''@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename=filename), code=301)'''
@app.route("/display" , methods=['GET', 'POST'])
def display():
    select = request.form.get('colours')
    print(str(select))
    return redirect(url_for('static', filename=select[:-5]+'.png'), code=301)
	
		
if __name__ == '__main__':
   app.run(debug = True)
   
