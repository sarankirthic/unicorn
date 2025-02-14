from flask import Flask, request, jsonify
from db import db, bcrypt, migrate
from models import User, Patient, HeartRate

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = User(email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.get_json()
    patient = Patient(name=data["name"], age=data["age"])
    db.session.add(patient)
    db.session.commit()
    return jsonify({"message": "Patient added"}), 201


@app.route("/patients/<int:id>", methods=["GET"])
def get_patient(id):
    patient = Patient.query.get(id)
    if patient:
        return jsonify({"id": patient.id, "name": patient.name, "age": patient.age}), 200
    return jsonify({"message": "Patient not found"}), 404


@app.route("/heart_rate", methods=["POST"])
def add_heart_rate():
    data = request.get_json()
    heart_rate = HeartRate(patient_id=data["patient_id"], bpm=data["bpm"])
    db.session.add(heart_rate)
    db.session.commit()
    return jsonify({"message": "Heart rate recorded"}), 201


@app.route("/heart_rate/<int:patient_id>", methods=["GET"])
def get_heart_rate(patient_id):
    heart_rates = HeartRate.query.filter_by(patient_id=patient_id).all()
    return jsonify([{"bpm": hr.bpm, "timestamp": hr.timestamp} for hr in heart_rates]), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
