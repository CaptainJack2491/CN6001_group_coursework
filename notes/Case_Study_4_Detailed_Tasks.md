# Case Study 4: CVD Clinic - Detailed Task Breakdown

## Case Study Summary

A cardiovascular (CVD) clinic in West London needs to digitize patient information currently collected on paper forms. The clinic handles:
- **Hypertension/Hypotension consultations**
- **BMI, Blood Pressure, and diabetes monitoring**
- **Multi-section forms**: Section 1 (patient-filled) + Section 2 (consultant-completed)
- **Prescription management** after examination

**Key Pain Points to Solve:**
- Manual form filling causes errors and waiting times
- No digital record of patient history
- Prescription generation is manual

---

## Task 1: Introduction (5 Marks)

### What to Write:

**1. Clinic Overview (1 paragraph)**
- Location: West London
- Specialization: Cardiovascular diseases
- Staff: Cardiovascular specialists/consultants, nurses, admin staff
- Current Problem: Paper-based form system causing delays and errors

**2. Business Processes (4-5 key processes)**

| Process | Description |
|---------|-------------|
| Patient Registration | New patients provide personal/medical history |
| Pre-Examination Forms | Patients complete Section 1 (symptoms, personal details) before seeing doctor |
| Vital Signs Recording | BMI, Blood Pressure, blood sugar checks |
| Specialist Consultation | Consultant reviews forms, conducts examination, completes Section 2 |
| Prescription Generation | Consultant issues prescriptions based on diagnosis |
| Appointment Booking | Scheduling follow-up visits |

**3. Proposed Solution**
- Web-based portal for patients to pre-fill forms
- Digital system for staff to complete consultations
- Automated prescription generation
- Cloud-based storage for patient records

**4. Scope of Work**
- Digital forms with dropdowns and validation
- Patient self-service portal
- Consultant dashboard
- Prescription printing/email system

**Deliverable:** 1-2 pages introducing the clinic, current problems, and your proposed digital solution.

---

## Task 2: Business Process Model - BPMN (10 Marks)

**Use:** Bonita Software

### BPMN Diagrams to Create:

#### Diagram 1: Patient Admission & Form Completion Process

**Lane: Patient**
- Start Event: "Arrive at Clinic"
- Task: "Login to Portal/Register"
- Task: "Fill Section 1 Form" (symptoms, personal info, medical history)
- Gateway: "Form Complete?"
  - No -> Task: "Complete Missing Fields"
  - Yes -> Task: "Submit Form"
- Task: "Wait for Vital Signs Check"
- Task: "Consultation with Specialist"
- Task: "Receive Prescription"
- End Event

**Lane: Nurse/Admin Staff**
- Start Event: "Patient Arrives"
- Task: "Verify Patient Identity"
- Task: "Check Vitals" (BMI, BP, Blood Sugar)
- Task: "Record Vital Signs in System"
- Task: "Escort to Consultant"
- End Event

**Lane: Consultant**
- Start Event: "Patient Ready"
- Task: "Review Section 1 (Patient Data)"
- Task: "Conduct Examination"
- Task: "Complete Section 2 (Consultant Notes)"
- Gateway: "Diagnosis Required?"
  - Hypertension -> Task: "Hypertension Treatment Plan"
  - Hypotension -> Task: "Hypotension Treatment Plan"
  - Diabetes -> Task: "Diabetes Management Plan"
- Task: "Generate Prescription"
- Task: "Schedule Follow-up"
- Task: "Save Medical Record"
- End Event

#### Diagram 2: Appointment Booking Process

**Lane: Patient**
- Task: "Request Appointment Online"
- Gateway: "Preferred Date Available?"
  - No -> Task: "Select Alternative Date"
  - Yes -> Task: "Confirm Appointment"
- Task: "Receive Confirmation"
- Task: "Complete Pre-Visit Forms"

**Lane: Admin Staff**
- Task: "Check Consultant Schedule"
- Task: "Block Appointment Slot"
- Task: "Send Confirmation Email/SMS"
- Task: "Send Pre-Visit Form Link"

#### Diagram 3: Form Processing & Data Flow

Show how Section 1 (Patient Data) flows to Consultant who adds Section 2 (Clinical Assessment) resulting in Complete Medical Record.

### BPMN Elements to Include:

| Element | Example in CVD Clinic |
|---------|----------------------|
| **Start/End Events** | Patient arrives -> Consultation complete |
| **User Tasks** | Fill form, Review patient data |
| **Service Tasks** | Auto-save form, Send email confirmation |
| **Exclusive Gateways** | "Hypertension OR Diabetes?" |
| **Parallel Gateways** | Check BP AND Check BMI simultaneously |
| **Data Objects** | Patient Form, Medical Record, Prescription |
| **Pools** | Clinic, Patient (external), Laboratory (external) |

**Tip:** Create 3 separate BPMN files for clarity.

---

## Task 3: Class Diagram & ERD (10 Marks)

**Use:** StarUML

### Classes to Create:

#### 1. Patient
```
Attributes:
- patientID: String (PK)
- firstName: String
- lastName: String
- dateOfBirth: Date
- gender: String
- phoneNumber: String
- email: String
- address: String
- emergencyContact: String
- nhsNumber: String

Operations:
- register()
- updateProfile()
- viewHistory()
- bookAppointment()
```

#### 2. MedicalForm (Abstract/Parent)
```
Attributes:
- formID: String (PK)
- patientID: String (FK)
- formType: String [Hypertension/Hypotension/Diabetes/General]
- dateCreated: Date
- status: String [Draft/Submitted/Completed]

Operations:
- submitForm()
- editForm()
- validateForm()
```

#### 3. SectionOne (Patient Section) - Extends MedicalForm
```
Attributes:
- symptoms: String
- currentMedications: String
- allergies: String
- familyHistory: String
- lifestyleFactors: String
- patientSignature: String

Operations:
- autoFillFromHistory()
- validateRequiredFields()
```

#### 4. SectionTwo (Consultant Section) - Extends MedicalForm
```
Attributes:
- clinicalNotes: String
- diagnosis: String
- severity: String [Mild/Moderate/Severe]
- consultantID: String (FK)
- examinationDate: Date
- consultantSignature: String

Operations:
- addClinicalNotes()
- setDiagnosis()
```

#### 5. Consultant (Staff)
```
Attributes:
- consultantID: String (PK)
- name: String
- specialization: String [Cardiologist/Diabetologist]
- licenseNumber: String
- email: String
- phone: String

Operations:
- examinePatient()
- completeSectionTwo()
- generatePrescription()
- viewPatientHistory()
```

#### 6. VitalSigns
```
Attributes:
- vitalID: String (PK)
- patientID: String (FK)
- recordedDate: DateTime
- bloodPressureSystolic: Integer
- bloodPressureDiastolic: Integer
- bmi: Float
- weight: Float
- height: Float
- bloodSugar: Float
- heartRate: Integer
- recordedBy: String (FK)

Operations:
- calculateBMI()
- flagAbnormalValues()
- compareWithPrevious()
```

#### 7. Prescription
```
Attributes:
- prescriptionID: String (PK)
- patientID: String (FK)
- consultantID: String (FK)
- issueDate: Date
- medications: String
- dosage: String
- frequency: String
- duration: String
- instructions: String
- status: String [Active/Completed/Cancelled]

Operations:
- generatePrescription()
- sendToPharmacy()
- emailToPatient()
- printPrescription()
```

#### 8. Appointment
```
Attributes:
- appointmentID: String (PK)
- patientID: String (FK)
- consultantID: String (FK)
- appointmentDate: DateTime
- duration: Integer (minutes)
- type: String [Initial/Follow-up/Emergency]
- status: String [Scheduled/Completed/Cancelled/No-show]
- roomNumber: String

Operations:
- scheduleAppointment()
- reschedule()
- cancel()
- sendReminder()
```

#### 9. MedicalRecord (Complete Patient History)
```
Attributes:
- recordID: String (PK)
- patientID: String (FK)
- formID: String (FK)
- vitalID: String (FK)
- prescriptionID: String (FK)
- createdDate: Date
- lastUpdated: Date

Operations:
- compileCompleteRecord()
- exportToPDF()
- shareWithSpecialist()
```

### Class Relationships (Cardinalities):

```
Patient 1 --- * MedicalForm (One patient has many forms over time)
Patient 1 --- * VitalSigns (Multiple vital checks)
Patient 1 --- * Prescription (Many prescriptions)
Patient 1 --- * Appointment (Many appointments)
Patient 1 --- 1 MedicalRecord (One comprehensive record)

MedicalForm 1 --- 1 SectionOne (Each form has exactly one Section 1)
MedicalForm 1 --- 1 SectionTwo (Each form has exactly one Section 2)
MedicalForm 1 --- * Prescription (One form may lead to prescriptions)

Consultant 1 --- * MedicalForm (Consultant completes many Section 2s)
Consultant 1 --- * Prescription (Issues many prescriptions)
Consultant 1 --- * Appointment (Has many appointments)

Appointment 1 --- 1 MedicalForm (Each appointment generates one form)
VitalSigns 1 --- * MedicalRecord (Recorded in history)
```

### ERD (Entity Relationship Diagram) Conversion:

**Entities & Attributes:**

| Entity | Primary Key | Foreign Keys | Attributes |
|--------|-------------|--------------|------------|
| Patients | patientID | - | All patient demographics |
| Consultants | consultantID | - | Name, specialization, license |
| MedicalForms | formID | patientID, consultantID | formType, dateCreated, status |
| SectionOne | sectionOneID | formID | All patient-filled fields |
| SectionTwo | sectionTwoID | formID, consultantID | All consultant-filled fields |
| VitalSigns | vitalID | patientID, recordedBy | BP, BMI, sugar, heart rate |
| Prescriptions | prescriptionID | patientID, consultantID, formID | Medications, dosage, instructions |
| Appointments | appointmentID | patientID, consultantID | Date, type, status, room |
| MedicalRecords | recordID | patientID, formID, vitalID, prescriptionID | Compilation of all data |

**Relationships:**
- **1:1** - MedicalForm to SectionOne, MedicalForm to SectionTwo
- **1:N** - Patient to MedicalForms, Patient to Prescriptions
- **N:M** - Patients to Consultants (through Appointments)

**SQL Table Examples:**

```sql
CREATE TABLE Patients (
    patientID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    email VARCHAR(100),
    phoneNumber VARCHAR(20)
);

CREATE TABLE MedicalForms (
    formID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    formType VARCHAR(50),
    status VARCHAR(20),
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);

CREATE TABLE SectionOne (
    sectionOneID VARCHAR(20) PRIMARY KEY,
    formID VARCHAR(20),
    symptoms TEXT,
    allergies TEXT,
    FOREIGN KEY (formID) REFERENCES MedicalForms(formID)
);

CREATE TABLE SectionTwo (
    sectionTwoID VARCHAR(20) PRIMARY KEY,
    formID VARCHAR(20),
    consultantID VARCHAR(20),
    clinicalNotes TEXT,
    diagnosis VARCHAR(200),
    FOREIGN KEY (formID) REFERENCES MedicalForms(formID)
);
```

---

## Task 4: Enterprise Cloud Architecture (10 Marks)

**Use:** Draw.io or Visio

### Architecture Overview:

The CVD Clinic system needs:
1. **Patient Portal** (public-facing)
2. **Staff Portal** (secure internal access)
3. **Database** (patient records - highly sensitive)
4. **Backup/Disaster Recovery**

### Architecture Components:

#### 1. On-Premise (Clinic)
- Workstations for consultants (7 exam rooms)
- Admin computers
- Network infrastructure
- Printer for prescriptions
- Firewall

#### 2. Off-Premise (AWS/Azure Cloud)

**VPC Structure:**

```
[VPC: cvd-clinic-vpc]
|
├── [Public Subnet 1] - Web Tier
│   └── EC2 Instance: Web Server
│       └── Patient Portal (Frontend)
│
├── [Public Subnet 2] - Web Tier
│   └── EC2 Instance: Web Server
│       └── Staff Portal (Frontend)
│
├── [Private Subnet 1] - App Tier
│   └── EC2 Instance: Application Server
│       └── Business Logic (Form validation, Workflows)
│
├── [Private Subnet 2] - Database Tier
│   └── RDS: MySQL/PostgreSQL
│       ├── Patients Database
│       ├── Forms Database
│       └── Audit Logs
│
└── [Management Subnet]
    └── Jump Box/Bastion Host (for secure admin access)
```

#### 3. Connectivity & Security

| Component | Purpose |
|-----------|---------|
| **Internet Gateway** | Allows public access to patient portal |
| **NAT Gateway** | Allows private subnets to reach internet for updates |
| **VPN Gateway** | Secure connection from clinic to cloud |
| **Load Balancer** | Distributes traffic, ensures availability |
| **WAF** | Blocks SQL injection, XSS attacks |
| **IAM Roles** | Access control (Patient role, Nurse role, Consultant role) |
| **KMS** | Encryption keys for patient data |

#### 4. Security Considerations (GDPR/HIPAA)

- **Encryption at Rest:** Database encryption using KMS
- **Encryption in Transit:** SSL/TLS for all connections
- **Access Control:** Role-based access (patients see only their data)
- **Audit Logging:** All access to patient records logged
- **Backup:** Daily backups to S3/Blob storage
- **Data Residency:** EU/UK data centers only

#### 5. Diagram Structure

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    INTERNET (Public)                        │
    └──────────────────────────┬──────────────────────────────────┘
                               │
                    [AWS/Azure Cloud]
                               │
              ┌────────────┴────────────┐
              │      Internet Gateway   │
              └────────────┬────────────┘
                           │
        ┌─────────────────┴─────────────────┐
        │                                   │
   ┌────▼────────┐                   ┌───────▼────────┐
   │ Public      │                   │ VPN Gateway    │
   │ Subnet      │                   │ (Clinic LAN)   │
   │ Patient     │                   │ Secure Tunnel  │
   │ Portal      │                   └───────┬────────┘
   └────┬────────┘                           │
        │                                     │
        │    ┌──────────────────┐             │
        └───►│ Load Balancer    │◄────────────┘
             │ (SSL Termination)│
             └────────┬───────────┘
                      │
           ┌────────────┴──────────────┐
           │                           │
    ┌──────▼────────┐         ┌─────────▼─────────┐
    │ Private       │         │ Private           │
    │ Subnet        │         │ Subnet            │
    │ App Server    │         │ Database (RDS)    │
    │ (Node.js/PHP) │         │ MySQL/PostgreSQL  │
    │ - Form Logic  │         │ - Encrypted       │
    │ - Validation  │         │ - Auto Backup     │
    └─────────────────┘       └──────────────────┘
                 │
           ┌─────▼──────────┐
           │ S3/Blob Storage│
           │ (Backups/Docs) │
           └────────────────┘
```

### Key Points to Address:

1. **Why Cloud?**
   - Scalability: Handle peak appointment times
   - Accessibility: Patients access portal from home
   - Cost: Pay-as-you-go vs. on-premise servers
   - Disaster Recovery: Automated backups

2. **Security Justification:**
   - Patient data is sensitive (GDPR compliance required)
   - Multi-layered security approach
   - Regular security audits

---

## Task 5: Prototype Implementation (30 Marks)

### Technology Stack Options:

**Option A (Recommended for simplicity):**
- Frontend: HTML5, CSS3, JavaScript
- Backend: PHP or Node.js
- Database: MySQL
- Hosting: AWS EC2 or Azure VM

**Option B (Cloud-Native):**
- Frontend: React.js
- Backend: AWS Lambda/Azure Functions
- Database: AWS RDS/Azure SQL
- Storage: AWS S3/Azure Blob

### Screens to Build:

#### Screen 1: Patient Portal - Login/Registration

```
┌─────────────────────────────────────────┐
│         CVD Clinic Portal [Logo]      │
├─────────────────────────────────────────┤
│                                         │
│   New Patient?      Existing Patient?   │
│   [Register]        [Login]           │
│                                         │
│   ─────────────────────────────────   │
│                                         │
│   Email: [____________________]         │
│   Password: [____________________]      │
│                                         │
│           [ Login ]                     │
│                                         │
│   [Forgot Password?]                    │
└─────────────────────────────────────────┘
```

**Functionality:**
- Patient registration (create account)
- Login with email/password
- Password reset via email

#### Screen 2: Patient - Pre-Visit Form (Section 1)

```
┌─────────────────────────────────────────┐
│      Pre-Consultation Form            │
│ Patient: John Doe | Appt: 15/04         │
├─────────────────────────────────────────┤
│                                         │
│ Personal Information:                   │
│ Name: [John Doe         ] [Auto-fill]  │
│ DOB: [01/01/1980       ]               │
│                                         │
│ Medical History:                        │
│ Do you have hypertension? [Yes/No] ▼   │
│ Current medications: [_______________] │
│                                         │
│ Symptoms:                               │
│ □ Chest pain                            │
│ □ Shortness of breath                   │
│ □ Dizziness                             │
│ □ Other: [_______________]               │
│                                         │
│ Lifestyle:                              │
│ Do you smoke? [Yes/No] ▼               │
│ Exercise? [Daily/Weekly/Never] ▼      │
│                                         │
│ [Save Draft] [Submit Form]              │
└─────────────────────────────────────────┘
```

**Key Features:**
- Dropdown menus (reduce errors)
- Auto-fill from previous visits
- Form validation (required fields)
- Save as draft functionality

#### Screen 3: Staff - Patient Dashboard

```
┌─────────────────────────────────────────┐
│      CVD Clinic Staff Portal            │
│ Dr. Sarah Smith | Cardiologist          │
├─────────────────────────────────────────┤
│                                         │
│ Today's Appointments:                   │
│ ┌────────┬──────────┬────────┬────────┐ │
│ │ Time   │ Patient  │ Type   │ Status │ │
│ ├────────┼──────────┼────────┼────────┤ │
│ │ 09:00  │ John Doe │ Initial│ Waiting│ │
│ │ 09:30  │ Jane S.  │ Follow │ Done   │ │
│ │ 10:00  │ Mike R.  │ Initial│ Waiting│ │
│ └────────┴──────────┴────────┴────────┘ │
│                                         │
│ [View Patient] [Start Consultation]     │
│                                         │
│ Notifications:                          │
│ ⚠ 3 patients have incomplete forms      │
└─────────────────────────────────────────┘
```

#### Screen 4: Consultant - Examination Form (Section 2)

```
┌─────────────────────────────────────────┐
│ Consultation - Patient: John Doe        │
│ Section 2: Clinical Assessment          │
├─────────────────────────────────────────┤
│                                         │
│ Section 1 Review (Patient Data):        │
│ ┌───────────────────────────────────┐   │
│ │ Symptoms: Chest pain, dizziness   │   │
│ │ BP History: 140/90 (last visit)   │   │
│ └───────────────────────────────────┘   │
│                                         │
│ Vital Signs (Nurse Recorded):           │
│ BP: [140/90] HR: [72 bpm]               │
│ BMI: [28.5] Sugar: [110 mg/dL]          │
│                                         │
│ Clinical Notes:                         │
│ [Patient reports intermittent           │
│  chest pain during exertion...          │
│  ______________________________ ]       │
│                                         │
│ Diagnosis: [Hypertension - Stage 1] ▼   │
│ Severity: [Mild ▼]                      │
│                                         │
│ [Generate Prescription]                 │
└─────────────────────────────────────────┘
```

#### Screen 5: Prescription Generation

```
┌─────────────────────────────────────────┐
│           Prescription                │
│ Date: 15/04/2026                      │
├─────────────────────────────────────────┤
│                                         │
│ Patient: John Doe                       │
│ NHS Number: 1234567890                  │
│                                         │
│ Medications:                            │
│ ┌──────────────┬────────┬────────────┐  │
│ │ Drug         │ Dosage │ Frequency  │  │
│ ├──────────────┼────────┼────────────┤  │
│ │ Lisinopril   │ 10mg   │ Once daily │  │
│ │ Aspirin      │ 75mg   │ Once daily │  │
│ └──────────────┴────────┴────────────┘  │
│                                         │
│ Instructions:                           │
│ [Take with food. Monitor BP daily.      │
│  Return in 2 weeks...]                  │
│                                         │
│ [Print] [Email to Patient] [Save]       │
└─────────────────────────────────────────┘
```

#### Screen 6: Admin - Appointment Scheduling

```
┌─────────────────────────────────────────┐
│      Appointment Booking                │
├─────────────────────────────────────────┤
│                                         │
│ Select Date: [15/04/2026 ▼]            │
│                                         │
│ Available Slots:                        │
│ ┌──────────────────────────┐            │
│ │ 09:00 AM - Available [Book]           │
│ │ 09:30 AM - Booked   [Full]           │
│ │ 10:00 AM - Available [Book]           │
│ │ ...                      │            │
│ └──────────────────────────┘            │
│                                         │
│ Select Consultant: [Dr. Smith ▼]       │
│ Appointment Type: [Initial/Follow ▼]  │
│                                         │
│ Patient Details:                        │
│ [Search by name/NHS number...]         │
│ [Or register new patient]               │
│                                         │
│ [Confirm Booking]                       │
└─────────────────────────────────────────┘
```

### Database Schema:

```sql
-- Core Tables
CREATE TABLE Patients (
    patientID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    nhsNumber VARCHAR(20) UNIQUE,
    password_hash VARCHAR(255),
    registrationDate DATE
);

CREATE TABLE Consultants (
    consultantID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    licenseNumber VARCHAR(50),
    email VARCHAR(100),
    password_hash VARCHAR(255),
    role VARCHAR(20) -- 'Consultant', 'Nurse', 'Admin'
);

CREATE TABLE MedicalForms (
    formID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    formType VARCHAR(50),
    status VARCHAR(20), -- 'Draft', 'Submitted', 'Completed'
    createdDate TIMESTAMP,
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);

CREATE TABLE SectionOne (
    sectionOneID VARCHAR(20) PRIMARY KEY,
    formID VARCHAR(20),
    symptoms TEXT,
    currentMedications TEXT,
    allergies TEXT,
    familyHistory TEXT,
    lifestyleSmoking VARCHAR(20),
    lifestyleExercise VARCHAR(50),
    submittedDate TIMESTAMP,
    FOREIGN KEY (formID) REFERENCES MedicalForms(formID)
);

CREATE TABLE SectionTwo (
    sectionTwoID VARCHAR(20) PRIMARY KEY,
    formID VARCHAR(20),
    consultantID VARCHAR(20),
    clinicalNotes TEXT,
    diagnosis VARCHAR(200),
    severity VARCHAR(20),
    completedDate TIMESTAMP,
    FOREIGN KEY (formID) REFERENCES MedicalForms(formID),
    FOREIGN KEY (consultantID) REFERENCES Consultants(consultantID)
);

CREATE TABLE VitalSigns (
    vitalID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    appointmentID VARCHAR(20),
    bpSystolic INT,
    bpDiastolic INT,
    heartRate INT,
    weightKg DECIMAL(5,2),
    heightCm DECIMAL(5,2),
    bmi DECIMAL(4,2),
    bloodSugar DECIMAL(5,2),
    recordedBy VARCHAR(20),
    recordedDate TIMESTAMP,
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);

CREATE TABLE Prescriptions (
    prescriptionID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    consultantID VARCHAR(20),
    formID VARCHAR(20),
    issueDate DATE,
    medications TEXT,
    dosage TEXT,
    frequency TEXT,
    duration TEXT,
    instructions TEXT,
    status VARCHAR(20),
    FOREIGN KEY (patientID) REFERENCES Patients(patientID),
    FOREIGN KEY (consultantID) REFERENCES Consultants(consultantID)
);

CREATE TABLE Appointments (
    appointmentID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    consultantID VARCHAR(20),
    appointmentDate DATE,
    appointmentTime TIME,
    duration INT,
    type VARCHAR(50),
    status VARCHAR(20), -- 'Scheduled', 'Completed', 'Cancelled'
    roomNumber VARCHAR(10),
    FOREIGN KEY (patientID) REFERENCES Patients(patientID),
    FOREIGN KEY (consultantID) REFERENCES Consultants(consultantID)
);
```

### Implementation Tips:

1. **Start Simple:** Build login and patient registration first
2. **Form Validation:** Use JavaScript for client-side validation
3. **Security:** Hash passwords, use prepared statements (prevent SQL injection)
4. **Responsive Design:** Make it mobile-friendly (patients may use phones)
5. **Error Handling:** Show user-friendly error messages

---

## Task 6: Agile Management - ScrumDesk (7 Marks)

### ScrumDesk Setup:

**Project Name:** "CVD Clinic Digital Transformation"

### Sprint Structure (4 Sprints):

#### Sprint 1: Foundation (Weeks 1-2)

**User Stories:**
- "As a patient, I want to register an account so that I can access the portal"
- "As a patient, I want to login so that I can view my information"
- "As an admin, I want to add consultants to the system"

**Tasks:**
- Setup database schema
- Create patient registration page
- Implement login authentication
- Design database tables

#### Sprint 2: Patient Features (Weeks 3-4)

**User Stories:**
- "As a patient, I want to fill Section 1 online so that I don't wait at the clinic"
- "As a patient, I want to book appointments online"
- "As a patient, I want to view my medical history"

**Tasks:**
- Build Section 1 form with dropdowns
- Create appointment booking system
- Implement form auto-save
- Send email confirmations

#### Sprint 3: Staff Features (Weeks 5-6)

**User Stories:**
- "As a nurse, I want to record vital signs so that consultants can review them"
- "As a consultant, I want to view patient forms before examination"
- "As a consultant, I want to complete Section 2"

**Tasks:**
- Build vital signs entry form
- Create consultant dashboard
- Implement Section 2 completion
- Link Section 1 and Section 2

#### Sprint 4: Prescription & Finalization (Weeks 7-8)

**User Stories:**
- "As a consultant, I want to generate prescriptions"
- "As a patient, I want to receive prescriptions via email"
- "As an admin, I want to generate reports"

**Tasks:**
- Create prescription template
- Implement PDF generation
- Add email functionality
- Testing and bug fixes
- Documentation

### ScrumDesk Board Columns:

```
[Backlog] -> [To Do] -> [In Progress] -> [Testing] -> [Done]
```

### Team Roles Assignment:

| Role | Responsibilities |
|------|----------------|
| **Scrum Master** | Facilitate daily standups, remove blockers |
| **Product Owner** | Prioritize user stories, accept completed work |
| **Developer 1** | Frontend (HTML/CSS/JavaScript) |
| **Developer 2** | Backend (PHP/Node.js) + Database |
| **QA/Tester** | Test plans, bug reporting |

### Tracking Metrics:

- **Sprint Burndown Chart:** Track remaining work daily
- **Velocity:** Story points completed per sprint
- **Task Board:** Visual progress tracking

**Deliverable:** Screenshots of ScrumDesk showing:
- Sprint planning
- User stories with tasks
- Burndown charts
- Team member assignments

---

## Task 7: Individual Reflective Evaluation (10 Marks)

### Structure (500-800 words):

#### 1. Personal Contribution (20%)

*Example:*
> "I was responsible for designing the database schema and implementing the patient registration module. I created the ERD in StarUML and built the MySQL database with all tables and relationships. I also developed the PHP scripts for CRUD operations on patient data."

**What to include:**
- Specific modules you worked on
- Diagrams you created (BPMN, Class, ERD, ECA)
- Challenges faced (e.g., "Had difficulty with many-to-many relationships, resolved by creating junction tables")

#### 2. Cloud Technology Analysis (35%)

**Compare AWS vs Azure:**

| Criteria | AWS | Azure | Your Choice |
|----------|-----|-------|-------------|
| Pricing | Pay-as-you-go, complex | Similar, easier calculator | AWS/Azure |
| Database | RDS (MySQL/PostgreSQL) | Azure SQL Database | Your choice |
| Security | IAM, KMS, WAF | Azure AD, Key Vault | |
| Documentation | Extensive | Good | |
| Learning Curve | Steeper | Easier for .NET | |

**Key Points to Discuss:**
- Why you chose your cloud provider
- Cost analysis (free tier usage)
- Security features implemented (encryption, IAM roles)
- Scalability considerations (handling 1000+ patients)
- GDPR compliance in cloud

**Reference Lab Exercises:**
- "Based on Week 5 lab exercise on AWS VPC setup..."
- "Applied concepts from Week 7 Azure security lab..."

#### 3. Testing Conducted (30%)

**Test Plan:**

| Test ID | Test Case | Expected Result | Actual Result | Status |
|---------|-----------|-----------------|---------------|--------|
| T01 | Patient registration | Account created, confirmation email sent | As expected | Pass |
| T02 | Login with valid credentials | Access granted to portal | As expected | Pass |
| T03 | Login with invalid password | Error message displayed | As expected | Pass |
| T04 | Section 1 form submission | Form saved to database | As expected | Pass |
| T05 | Form validation - missing fields | Error shown, form not submitted | As expected | Pass |
| T06 | Concurrent patient bookings | No double-booking occurs | As expected | Pass |
| T07 | SQL injection attempt | Blocked, no database breach | As expected | Pass |

**Security Testing:**
- SQL injection prevention tested
- XSS vulnerability testing
- Password hashing verification
- Session timeout testing

**Performance Testing:**
- Page load times (target: <3 seconds)
- Database query optimization
- Concurrent user handling

#### 4. Learning Outcomes (15%)

**Skills Gained:**
- Technical: Database design, cloud architecture, web development
- Tools: StarUML, Bonita, Draw.io, ScrumDesk, AWS/Azure
- Soft skills: Team collaboration, agile methodology, documentation

**Critical Reflection:**
- What would you do differently?
- How did this project prepare you for industry?
- Connection to Enterprise Architecture principles

**References:** Include 5-8 sources using Harvard style

---

## Task 8: Group Conclusion (10 Marks)

### Structure (400-600 words):

#### 1. Summary of Achievements

> "Our group successfully designed and implemented a cloud-based patient record system for the CVD Clinic. We delivered:
> - 3 BPMN process models using Bonita
> - Complete UML class diagram and ERD using StarUML
> - Enterprise Cloud Architecture on AWS/Azure
> - Working web portal with patient and staff interfaces
> - Agile project management using ScrumDesk"

#### 2. Successes

- Effective team communication
- Successful integration of all components
- Meeting project deadlines
- Positive feedback during testing

#### 3. Challenges Faced

| Challenge | Solution |
|-----------|----------|
| Database connection issues | Used PDO/prepared statements, proper error handling |
| Form validation complexity | Implemented both client-side and server-side validation |
| Team coordination | Daily standups via ScrumDesk |

#### 4. Future Improvements

- **Mobile App:** iOS/Android app for patients
- **AI Integration:** Predictive analytics for cardiovascular risk
- **Telemedicine:** Video consultation feature
- **NHS Integration:** Connect with NHS patient records
- **Wearable Integration:** Import data from fitness trackers (BP monitors)

#### 5. Final Reflection

- Project met all requirements
- Demonstrated enterprise architecture principles
- Practical application of cloud technologies
- Prepared group for real-world software development

---

## Task 9: Presentation & References (8 Marks)

### Report Structure:

1. **Title Page**
   - Module: CN6001/CN5023
   - Title: "CVD Clinic Patient Record System"
   - Group members with Student IDs
   - Date

2. **Table of Contents**
   - List all sections with page numbers

3. **List of Figures**
   - Figure 1: BPMN - Patient Admission Process
   - Figure 2: BPMN - Appointment Booking
   - Figure 3: Class Diagram
   - Figure 4: ERD
   - Figure 5: Enterprise Cloud Architecture
   - Figure 6-10: Prototype Screenshots
   - Figure 11: ScrumDesk Dashboard

4. **Figures Quality:**
   - High resolution
   - Clear labels
   - Properly numbered (Figure 1, Figure 2, etc.)
   - Captions explaining each diagram

### References (Harvard Style - Minimum 8-10):

**Example References:**

- AWS (2024) *Amazon Web Services Documentation*. Available at: https://docs.aws.amazon.com/
- Microsoft (2024) *Azure Documentation*. Available at: https://docs.microsoft.com/azure/
- OMG (2024) *Business Process Model and Notation (BPMN) Version 2.0*.
- Sommerville, I. (2016) *Software Engineering*. 10th ed. Boston: Pearson.
- Erl, T., Puttini, R. and Mahmood, Z. (2013) *Cloud Computing: Concepts, Technology & Architecture*. Upper Saddle River, NJ: Prentice Hall.

---

## Summary: Case Study 4 vs Case Study 6

| Factor | Case Study 4 (CVD Clinic) | Case Study 6 (State Clinic) |
|--------|---------------------------|----------------------------|
| **Complexity** | Moderate | High |
| **Entities** | ~8-10 | ~12-15 |
| **Processes** | Forms-based, linear | Multi-faceted (booking, billing, equipment) |
| **Best For** | Groups new to EA/cloud | Experienced developers |
| **Marks Potential** | Good (easier to do well) | Higher (more to demonstrate) |
| **Implementation Time** | Shorter | Longer |
| **Cloud Justification** | Good (patient data security) | Excellent (complex multi-tier) |

### Recommendation:

**Choose Case Study 4 if:**
- Your group has less development experience
- You want a focused, manageable scope
- You prefer a healthcare system with clear, linear workflows
- You want to emphasize form processing and data validation

**Choose Case Study 6 if:**
- Your group has strong technical skills
- You want to showcase complex business logic
- You want to demonstrate advanced cloud architecture
- You want to impress with multi-module implementation

**For most groups, Case Study 4 is safer** - it's easier to complete all requirements fully, while Case Study 6 offers higher marks potential but requires more time and expertise.

---

## Quick Checklist for Case Study 4

| Task | Deliverable | Marks |
|------|-------------|-------|
| 1 | Introduction (1-2 pages) | 5 |
| 2 | 3 BPMN diagrams in Bonita | 10 |
| 3 | Class diagram + ERD in StarUML | 10 |
| 4 | Cloud Architecture in Draw.io | 10 |
| 5 | Working web portal (4-6 screens) | 30 |
| 6 | ScrumDesk screenshots | 7 |
| 7 | Individual reflection (500-800 words) | 10 |
| 8 | Group conclusion (400-600 words) | 10 |
| 9 | Formatting + References | 8 |
| **Total** | | **100** |
