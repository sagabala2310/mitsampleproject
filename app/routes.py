from flask import render_template, request, redirect, url_for
from .forms import PatientForm
from .models import Patient
from . import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patient/new', methods=['GET', 'POST'])
def new_patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(name=form.name.data, age=form.age.data, gender=form.gender.data)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('patient.html', form=form)

@app.route('/patient/<int:patient_id>')
def patient_detail(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return render_template('patient.html', patient=patient)