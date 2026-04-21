from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'
    patientID = db.Column(db.String(20), primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    dateOfBirth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False, default='password123')
    
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    records = db.relationship('MedicalRecord', backref='patient', lazy=True)

class MedicalRecord(db.Model):
    __tablename__ = 'medical_records'
    recordID = db.Column(db.String(20), primary_key=True)
    patientID = db.Column(db.String(20), db.ForeignKey('patients.patientID'), nullable=False)
    createdDate = db.Column(db.Date, default=datetime.utcnow)

class AdminStaff(db.Model):
    __tablename__ = 'admin_staff'
    adminID = db.Column(db.String(20), primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False, default='admin123')

class Consultant(db.Model):
    __tablename__ = 'consultants'
    consultantID = db.Column(db.String(20), primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False, default='consultant123')

class Nurse(db.Model):
    __tablename__ = 'nurses'
    nurseID = db.Column(db.String(20), primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    registrationNo = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False, default='nurse123')

class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointmentID = db.Column(db.String(20), primary_key=True)
    patientID = db.Column(db.String(20), db.ForeignKey('patients.patientID'), nullable=False)
    adminID = db.Column(db.String(20), db.ForeignKey('admin_staff.adminID'), nullable=True)
    consultantID = db.Column(db.String(20), db.ForeignKey('consultants.consultantID'), nullable=True)
    appointmentDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Scheduled')
    type = db.Column(db.String(50), nullable=False)

class MedicalForm(db.Model):
    __tablename__ = 'medical_forms'
    formID = db.Column(db.String(20), primary_key=True)
    appointmentID = db.Column(db.String(20), db.ForeignKey('appointments.appointmentID'), nullable=False)
    recordID = db.Column(db.String(20), db.ForeignKey('medical_records.recordID'), nullable=True)
    formType = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Pending')

class SectionOne(db.Model):
    __tablename__ = 'section_one'
    sectionOneID = db.Column(db.String(20), primary_key=True)
    formID = db.Column(db.String(20), db.ForeignKey('medical_forms.formID'), nullable=False)
    symptoms = db.Column(db.Text, nullable=True)
    allergies = db.Column(db.Text, nullable=True)

class SectionTwo(db.Model):
    __tablename__ = 'section_two'
    sectionTwoID = db.Column(db.String(20), primary_key=True)
    formID = db.Column(db.String(20), db.ForeignKey('medical_forms.formID'), nullable=False)
    consultantID = db.Column(db.String(20), db.ForeignKey('consultants.consultantID'), nullable=False)
    diagnosis = db.Column(db.String(200), nullable=True)
    clinicalNotes = db.Column(db.Text, nullable=True)

class VitalSigns(db.Model):
    __tablename__ = 'vital_signs'
    vitalID = db.Column(db.String(20), primary_key=True)
    appointmentID = db.Column(db.String(20), db.ForeignKey('appointments.appointmentID'), nullable=False)
    nurseID = db.Column(db.String(20), db.ForeignKey('nurses.nurseID'), nullable=True)
    bpSystolic = db.Column(db.Integer, nullable=True)
    bpDiastolic = db.Column(db.Integer, nullable=True)
    bmi = db.Column(db.Float, nullable=True)

class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    prescriptionID = db.Column(db.String(20), primary_key=True)
    consultantID = db.Column(db.String(20), db.ForeignKey('consultants.consultantID'), nullable=False)
    formID = db.Column(db.String(20), db.ForeignKey('medical_forms.formID'), nullable=False)
    medications = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.Text, nullable=False)
