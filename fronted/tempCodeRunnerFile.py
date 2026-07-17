me__)
model=pickle.load(open("placementpred.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def doPredict():
    cgpa=float(request.form.get('cgpa'))
    print(cgpa)
    iq=float(request.form.get('iq'))
    print(