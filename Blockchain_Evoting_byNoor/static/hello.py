from flask import Flask, request,render_template

app = Flask (__name__)

@app.route('/hello/<name>')
def hello_world(name):
	return "Hello %s!"% name
	
@app.route('/home')
def index():
	return render_template('home.html')
	
	
if __name__ =='__main__':
	app.debug = True
	app.run()
	app.run(debug=True)
