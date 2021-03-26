from flask import Flask,render_template,redirect,request,url_for
from joblib import load
#import Crop_project
model=load("Crop.joblib")

app = Flask(__name__)
@app.route("/hello",methods=['GET','POST'])
def hello():
   pic=""
   if request.method == 'GET':
       return render_template('view.html')
   elif request.method =='POST':
       nitrogen=request.form['nitrogen']
       phosporous=request.form['phosporous']
       pottasium=request.form['pottasium']
       temp=request.form['temp']
       humidity=request.form['humidity']
       ph=request.form['ph']
       rain=request.form['rain']
       nitrogen=float(nitrogen)
       phosporous=float(phosporous)
       pottasium=float(pottasium)
       temp=float(temp)
       humidity=float(humidity)
       ph=float(ph)
       rain=float(rain)
       feature=([[nitrogen,phosporous,pottasium,temp,humidity,ph,rain]])        
       result=model.predict(feature)
       pic="https://source.unsplash.com/720x400/?"+result[0]
       print(pic)
       return render_template('view.html',pic=pic,result=result[0])
    
#@app.route("/plant",methods=['GET','POST'])
#def plant():
         
        # nitrogen=request.form['nitrogen']
       #  phosporous=request.form['phosporous']
      #   pottasium=request.form['pottasium']
     #    temp=request.form['temp']
    #     humidity=request.form['humidity']
   #      ph=request.form['ph']
  #       rain=request.form['rain']
 #        nitrogen=float(nitrogen)
#         phosporous=float(phosporous)
        # pottasium=float(pottasium)
       #  temp=float(temp)
      #   humidity=str(humidity)
     #    ph=float(ph)
    #     rain-float(rain)
   #      feature=([[nitrogen,phosporous,pottasium,temp,humidity,ph,rain]])        
  #       result=model.predict(feature)
 #        print(result[0])
#         return redirect(url_for("hello"))


app.run(debug=True)
    
