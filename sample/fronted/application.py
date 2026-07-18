from flask import Flask, render_template,request
import pandas as pd
import pickle
app = Flask(__name__)
model=pickle.load(open("placementpred.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def doPredict():
    cgpa=float(request.form.get('cgpa'))
    print(cgpa)
    iq=float(request.form.get('iq'))
    print(iq)
    result=model.predict(pd.DataFrame([[cgpa,iq]],columns=['cgpa','iq']))
    print(result)
    if(result[0]==0):
        fresult="placement not will  done"
    else:
        fresult="placement will be  done"
    return fresult
    # return str(result[0])
if __name__ == "__main__":
    app.run(debug=True)