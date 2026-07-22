from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("house_price_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        area = float(request.form["area"])

        prediction = model.predict([[area]])[0]

        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)