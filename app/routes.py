from flask import render_template, request, redirect, url_for
from app import app, db
from .forms import PatientForm
from .models import Patient

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patient_list():
    patients = Patient.query.all()
    return render_template('patient.html', patients=patients)

@app.route('/submit_patient_info', methods=['POST'])
def submit_patient_info():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(name=form.name.data, age=form.age.data, condition=form.condition.data)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patient_list'))
    patients = Patient.query.all()
    return render_template('patient.html', form=form, patients=patients)