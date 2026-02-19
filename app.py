from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["number_inpatient"]),
        float(request.form["diag_1"]),
        float(request.form["diag_2"]),
        float(request.form["num_lab_procedures"]),
        float(request.form["diag_3"]),
        float(request.form["num_medications"]),
        float(request.form["discharge_disposition_id"]),
        float(request.form["time_in_hospital"]),
        float(request.form["age"]),
        float(request.form["number_diagnoses"]),
        float(request.form["number_emergency"]),
        float(request.form["num_procedures"]),
        float(request.form["admission_type_id"]),
        float(request.form["insulin"]),
        float(request.form["number_outpatient"]),
    ]

    final_input = np.array([features])

    prediction = model.predict(final_input)[0]

    if prediction == 1:
        result = "⚠️ High Risk — Visit Doctor Soon"
    else:
        result = "✅ Low Risk"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)
