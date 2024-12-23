# filepath: /Volumes/SAGA/sample project/patient-info-app/create_db.py
from app import app, db
from app.models import Patient

with app.app_context():
    db.create_all()
    print("Database and tables created successfully.")