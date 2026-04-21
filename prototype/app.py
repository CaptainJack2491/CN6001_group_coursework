import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from models import db, Patient, Appointment, MedicalForm, SectionOne, SectionTwo, VitalSigns, Consultant, Nurse, AdminStaff

app = Flask(__name__)

# Enterprise standard: Use PostgreSQL on AWS (if DATABASE_URL is set), otherwise fallback to SQLite for local testing
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///cvd_clinic.db')

# Note: For AWS PostgreSQL, the DATABASE_URL environment variable should look like:
# postgresql://username:password@rds-endpoint-url.amazonaws.com:5432/cvd_clinic

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey_cvd_clinic' # Needed for sessions

db.init_app(app)

# ---------------------------------------------------------
# Patient Portal (SOA) Routes
# ---------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def patient_login():
    patient_id = request.form.get('patient_id')
    password = request.form.get('password')
    
    patient = Patient.query.filter_by(patientID=patient_id, password=password).first()
    if patient:
        session['user_id'] = patient.patientID
        session['role'] = 'patient'
        return redirect(url_for('dashboard'))
    return render_template('index.html', error="Invalid Patient ID or Password")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session['role'] != 'patient':
        return redirect(url_for('index'))
    
    patient = Patient.query.get(session['user_id'])
    appointments = Appointment.query.filter_by(patientID=patient.patientID).all()
    return render_template('dashboard.html', patient=patient, appointments=appointments)

# ---------------------------------------------------------
# Staff Portal (AOA) Routes
# ---------------------------------------------------------
@app.route('/staff')
def staff_login_page():
    return render_template('staff_login.html')

@app.route('/staff/login', methods=['POST'])
def staff_login():
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    role = request.form.get('role') # consultant, nurse, or admin

    user = None
    if role == 'consultant':
        user = Consultant.query.filter_by(consultantID=user_id, password=password).first()
    elif role == 'nurse':
        user = Nurse.query.filter_by(nurseID=user_id, password=password).first()
    elif role == 'admin':
        user = AdminStaff.query.filter_by(adminID=user_id, password=password).first()

    if user:
        session['user_id'] = user_id
        session['role'] = role
        session['user_name'] = f"{user.firstName} {user.lastName}"
        return redirect(url_for('staff_dashboard'))
    
    return render_template('staff_login.html', error="Invalid Credentials")

@app.route('/staff/dashboard')
def staff_dashboard():
    if 'role' not in session or session['role'] not in ['consultant', 'nurse', 'admin']:
        return redirect(url_for('staff_login_page'))
    
    appointments = Appointment.query.all()
    return render_template('staff_dashboard.html', 
                           role=session['role'], 
                           user_name=session['user_name'],
                           appointments=appointments)

@app.route('/medical_record/<appt_id>')
def view_medical_record(appt_id):
    if 'user_id' not in session: return redirect(url_for('index'))
    
    appt = Appointment.query.get(appt_id)
    if not appt: return "Appointment not found", 404
    
    # Check authorization (patient can only see their own, staff can see any)
    if session['role'] == 'patient' and appt.patientID != session['user_id']:
        return "Unauthorized", 401
    
    patient = Patient.query.get(appt.patientID)
    form = MedicalForm.query.filter_by(appointmentID=appt_id).first()
    sec1 = SectionOne.query.filter_by(formID=form.formID).first() if form else None
    sec2 = SectionTwo.query.filter_by(formID=form.formID).first() if form else None
    vitals = VitalSigns.query.filter_by(appointmentID=appt_id).first()
    
    return render_template('medical_record.html', 
                           appt=appt, patient=patient, 
                           sec1=sec1, sec2=sec2, vitals=vitals)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# ---------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------
@app.route('/api/patient/register', methods=['POST'])
def api_register_patient():
    data = request.json
    try:
        new_patient = Patient(
            patientID=data['patientID'],
            firstName=data['firstName'],
            lastName=data['lastName'],
            dateOfBirth=datetime.strptime(data['dateOfBirth'], '%Y-%m-%d').date(),
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Success"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/appointment/book', methods=['POST'])
def api_book_appointment():
    if 'user_id' not in session: return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    try:
        new_appt = Appointment(
            appointmentID=data['appointmentID'],
            patientID=session['user_id'],
            appointmentDate=datetime.strptime(data['appointmentDate'], '%Y-%m-%d %H:%M:%S'),
            status='Scheduled',
            type=data.get('type', 'General Checkup')
        )
        db.session.add(new_appt)
        db.session.commit()
        
        new_form = MedicalForm(
            formID=f"F-{data['appointmentID']}",
            appointmentID=new_appt.appointmentID,
            formType='CVD Standard',
            status='Pending'
        )
        db.session.add(new_form)
        db.session.commit()
        return jsonify({"message": "Success"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/form/section_one', methods=['POST'])
def api_submit_section_one():
    data = request.json
    try:
        sec1 = SectionOne(
            sectionOneID=f"S1-{data['formID']}",
            formID=data['formID'],
            symptoms=data['symptoms'],
            allergies=data['allergies']
        )
        db.session.add(sec1)
        form = MedicalForm.query.get(data['formID'])
        if form: form.status = 'Section 1 Completed'
        db.session.commit()
        return jsonify({"message": "Success"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/vitals', methods=['POST'])
def api_record_vitals():
    if session.get('role') != 'nurse': return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    try:
        vitals = VitalSigns(
            vitalID=f"V-{data['appointmentID']}",
            appointmentID=data['appointmentID'],
            nurseID=session['user_id'],
            bpSystolic=data['bpSystolic'],
            bpDiastolic=data['bpDiastolic'],
            bmi=data['bmi']
        )
        db.session.add(vitals)
        db.session.commit()
        return jsonify({"message": "Vitals recorded"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/consultation/finalize', methods=['POST'])
def api_finalize_consultation():
    if session.get('role') != 'consultant': return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    try:
        sec2 = SectionTwo(
            sectionTwoID=f"S2-{data['formID']}",
            formID=data['formID'],
            consultantID=session['user_id'],
            diagnosis=data['diagnosis'],
            clinicalNotes=data['notes']
        )
        db.session.add(sec2)
        form = MedicalForm.query.get(data['formID'])
        if form: form.status = 'Completed'
        db.session.commit()
        return jsonify({"message": "Consultation finalized"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# ---------------------------------------------------------
# Database Initialization
# ---------------------------------------------------------
def init_db():
    with app.app_context():
        db.drop_all() # Reset for clean dual-interface setup
        db.create_all()
        # Create default staff
        c = Consultant(consultantID="C001", firstName="Jayrup", lastName="Nakawala", specialization="Cardiology", password="123")
        n = Nurse(nurseID="N001", firstName="Fatema", lastName="Doctor", registrationNo="REG123", password="123")
        a = AdminStaff(adminID="A001", firstName="Sangeet", lastName="Kaur", role="Admin", password="123")
        db.session.add_all([c, n, a])
        db.session.commit()

if __name__ == '__main__':
    if not os.path.exists('cvd_clinic.db'):
        init_db()
    app.run(debug=True, port=5000)
