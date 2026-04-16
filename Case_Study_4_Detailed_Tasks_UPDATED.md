# Case Study 4: CVD Clinic — Complete Task Breakdown
## Module: CN6001 / CN5023 | Enterprise Architecture and Cloud Computing
### Submission Deadline: 1st May 2026 | Weighting: 30%

---

## Original Case Study (Verbatim)

A group of cardiovascular specialists run a CVD clinic in West London. The patients' information is currently collected on forms that are to be filled by the patients and examined by the staff before the patient reach to the doctor. There are many different forms for different reasons such as hypertension or hypotension consultation after specialist examination of the BMI, Blood Pressure and diabetics etc. The current system was examined and all aspects of the business activities, and the way they functioned were observed. The manager, every category of staff and some patients were interviewed. Sample forms that are given to patients were collected and the information asked for, and its purpose, were observed. Most of the forms, had 2 sections, the first section filled in by the patient before cardiovascular (CVD) examination and the second section was completed by the Consultant after examination and appointment session. There was a lot of information requested from registering patients, booking appointment etc. This was a common source of error that increased waiting times. An information system can tackle the problem by automating the filling of certain fields; adding in drop-down menus and setting defaults. Finally, the Consultant gives the patient the requisite Prescriptions.

The CVD Clinic wants to create a web-based computer system that allows employees and external companies to access the company's portal (i.e. using Web site SOA, Azure or AWS cloud-based system). Model, design and implement client web pages that can access the database using MS SQL Server or any other web or cloud development package. The database must be designed from the class model and the entity data model using MySQL, MS SQL Server, Oracle database and any AI or ML components (not MS Access).

---

## Updated / Modified Case Study (Your Version — Task 1 Deliverable)

**CVD Clinic Digital Transformation — West London Cardiovascular Centre**

West London Cardiovascular Centre (WLCC) is a specialist clinic staffed by cardiovascular consultants, nurses, and administrative personnel. The clinic serves patients requiring diagnosis and management of conditions including hypertension, hypotension, and diabetes-related cardiovascular complications. Currently, all patient interactions are paper-based: patients complete Section 1 of multi-part forms on arrival, and consultants complete Section 2 after examination. This manual approach introduces transcription errors, increases patient waiting times, and prevents efficient sharing of patient history across visits.

The proposed solution is a cloud-hosted web portal that allows patients to pre-complete their forms at home before their appointment, enables nursing staff to record vital signs digitally, and gives consultants a unified dashboard to review patient data, complete clinical assessments, and generate prescriptions electronically. The system will be built as a three-tier Client-Server System (CSS) hosted on AWS or Azure, with a web front-end (SOA/COA), a business logic layer, and a relational database backend (MySQL/PostgreSQL), all compliant with UK GDPR requirements for healthcare data.

**Core Business Processes:**

| # | Process | Actor | Description |
|---|---------|-------|-------------|
| 1 | Patient Registration | Patient / Admin | New patient creates an account and enters demographic details |
| 2 | Appointment Booking | Patient / Admin | Patient requests a slot; admin confirms against consultant schedule |
| 3 | Pre-Visit Form (Section 1) | Patient | Patient fills symptoms, medications, lifestyle, medical history online |
| 4 | Vital Signs Recording | Nurse | Nurse records BP, BMI, blood sugar, heart rate on patient arrival |
| 5 | Specialist Consultation | Consultant | Consultant reviews Section 1 and vitals, conducts examination, completes Section 2 |
| 6 | Diagnosis & Prescription | Consultant | Consultant records diagnosis, severity, and generates a prescription |
| 7 | Medical Record Update | System | System compiles form, vitals, diagnosis, and prescription into patient record |
| 8 | Follow-up Scheduling | Admin / Consultant | Follow-up appointment booked before patient leaves |

---

## Task 1: Introduction (5 Marks)

### What Must Be Included

**Marking focus:** Overview of the selected case study, discussion of operations and main business processes.

**Required sections (1–2 pages total):**

1. **Clinic Background** — Location (West London), specialisation (cardiovascular diseases), staff categories (consultants, nurses, admin), current paper-based problem
2. **Current System Problems** — Manual forms cause errors; no digital patient history; appointment bottlenecks; no automated prescription generation
3. **Business Processes** — Describe the 8 key processes in the table above in prose form (do not just paste a table in the final report)
4. **Proposed Digital Solution** — Cloud-hosted web portal (AWS/Azure), digital Section 1 + Section 2 forms, nurse vital-sign entry, consultant dashboard, prescription generation, patient record management
5. **Scope Statement** — What the prototype will and will not implement (e.g., "The prototype implements patient registration, appointment booking, Section 1 and Section 2 forms, vital signs recording, and prescription generation. NHS national system integration is out of scope.")

**Word count target:** ~400–500 words for this section.

---

## Task 2: Business Process Model — BPMN (10 Marks)

**Tool:** Bonita BPM Software  
**Requirement:** Each group member selects one BPMN lane and develops it further with additional activities.

### BPMN Diagram 1: Patient Registration & Pre-Visit Form Submission

**Pool: CVD Clinic**

| Lane | Key Activities |
|------|---------------|
| **Patient** | Start → Register/Login → Fill Section 1 (symptoms, medications, allergies, lifestyle) → Gateway: Form complete? → Submit Form → End |
| **Admin Staff** | Receive registration request → Verify identity → Create patient record in system → Send confirmation → End |

**BPMN elements to show:**
- Start Event (patient arrives at portal)
- User Tasks (fill form fields)
- Exclusive Gateway ("Is this patient already registered?")
- Service Task (auto-fill fields from previous visit)
- Data Object (Patient Form — Section 1)
- End Event (form submitted and saved)

---

### BPMN Diagram 2: Appointment Booking Process

**Pool: CVD Clinic**

| Lane | Key Activities |
|------|---------------|
| **Patient** | Start → Request appointment (date/consultant preference) → Gateway: Slot available? → Confirm booking → Receive email/SMS → Complete pre-visit form → End |
| **Admin Staff** | Check consultant calendar → Gateway: Requested slot free? → Block slot → Send confirmation → Send Section 1 form link → End |
| **Consultant** | View scheduled appointments → Gateway: Any clashes? → Approve schedule → End |

**BPMN elements to show:**
- Message Events (email/SMS confirmation)
- Parallel Gateway (admin blocks slot AND sends form simultaneously)
- Exclusive Gateway (slot available check)
- Timer Event (reminder 24 hours before appointment)

---

### BPMN Diagram 3: Consultation & Prescription Process

**Pool: CVD Clinic**

| Lane | Key Activities |
|------|---------------|
| **Patient** | Start → Check in → Wait → Consultation → Receive prescription → End |
| **Nurse / Admin** | Receive patient → Verify identity → Record Vital Signs (BP, BMI, blood sugar, heart rate) → Escort to consultant → End |
| **Consultant** | Review Section 1 (patient-submitted) → Review vital signs → Conduct examination → Complete Section 2 → Exclusive Gateway: Diagnosis type? → Hypertension/Hypotension/Diabetes treatment path → Generate prescription → Schedule follow-up → Save medical record → End |

**BPMN elements to show:**
- Parallel Gateway (consultant reviews Section 1 AND vital signs in parallel)
- Exclusive Gateway (diagnosis branching: Hypertension / Hypotension / Diabetes / General)
- Service Task (auto-generate prescription template based on diagnosis)
- Data Objects (Section 1 Form, Section 2 Form, Vital Signs Record, Prescription)
- Sub-process (Prescription Generation)

### BPMN Notation Key (must include in diagram):

| Symbol | Name | Used For |
|--------|------|---------|
| Circle (thin) | Start Event | Process begins |
| Circle (thick) | End Event | Process ends |
| Rounded rectangle | Task | An activity |
| Diamond (X) | Exclusive Gateway | One path chosen |
| Diamond (+) | Parallel Gateway | Multiple paths simultaneously |
| Envelope icon | Message Event | Email/notification sent |
| Cylinder | Data Store | Database access |
| Document icon | Data Object | Form/document |

---

## Task 3: Class Diagram & ERD (10 Marks)

**Tool:** StarUML or Yworks  
**Requirement:** Classes with full attributes and operations, correct UML notation, all associations with cardinalities. Convert to ERD showing UML-to-ERD transformation.

### Class Diagram — Corrected & Improved

**Key corrections from original:**
- `SectionOne` and `SectionTwo` use **composition** from `MedicalForm`, not inheritance. They should NOT inherit AND be associated simultaneously.
- A `Staff` class (superclass) is needed to model nurses, consultants, and admin distinctly — they have different operations.
- Attribute visibility: private (`-`) for IDs and sensitive data; public (`+`) for operations.
- `MedicalRecord` should not store single FKs to vitals/prescriptions — it is a summary/aggregation entity that links via the patient.
- `Consultant` should have `firstName` and `lastName` separately (not a single `name`), consistent with ERD.

#### Classes (Corrected)

**Staff** *(abstract superclass)*
```
- staffID : String  {PK}
- firstName : String
- lastName : String
- email : String
- phone : String
- passwordHash : String
- role : String  [Consultant / Nurse / Admin]
+ login() : Boolean
+ logout() : void
+ updateProfile() : void
```

**Consultant** *(extends Staff)*
```
- specialization : String  [Cardiologist / Diabetologist]
- licenseNumber : String
+ examinePatient(patientID : String) : void
+ completeSectionTwo(formID : String) : void
+ generatePrescription(patientID : String) : Prescription
+ viewPatientHistory(patientID : String) : List<MedicalRecord>
```

**Nurse** *(extends Staff)*
```
+ recordVitalSigns(patientID : String, appointmentID : String) : VitalSigns
+ verifyPatientIdentity(patientID : String) : Boolean
+ escortPatient(patientID : String) : void
```

**Admin** *(extends Staff)*
```
+ scheduleAppointment(patientID : String, consultantID : String) : Appointment
+ cancelAppointment(appointmentID : String) : void
+ generateReport() : void
```

**Patient**
```
- patientID : String  {PK}
- firstName : String
- lastName : String
- dateOfBirth : Date
- gender : String
- phoneNumber : String
- email : String
- address : String
- emergencyContact : String
- nhsNumber : String  {unique}
- passwordHash : String
- registrationDate : Date
+ register() : void
+ login() : Boolean
+ updateProfile() : void
+ viewHistory() : List<MedicalRecord>
+ bookAppointment(date : DateTime, consultantID : String) : Appointment
```

**MedicalForm**
```
- formID : String  {PK}
- patientID : String  {FK}
- consultantID : String  {FK}
- appointmentID : String  {FK}
- formType : String  [Hypertension / Hypotension / Diabetes / General]
- dateCreated : DateTime
- status : String  [Draft / Submitted / Completed]
+ submitForm() : void
+ editForm() : void
+ validateForm() : Boolean
```

**SectionOne** *(composed within MedicalForm — NOT a subclass)*
```
- sectionOneID : String  {PK}
- formID : String  {FK}
- symptoms : String
- currentMedications : String
- allergies : String
- familyHistory : String
- lifestyleSmoking : String
- lifestyleExercise : String
- patientSignature : String
- submittedDate : DateTime
+ autoFillFromHistory(patientID : String) : void
+ validateRequiredFields() : Boolean
```

**SectionTwo** *(composed within MedicalForm — NOT a subclass)*
```
- sectionTwoID : String  {PK}
- formID : String  {FK}
- consultantID : String  {FK}
- clinicalNotes : String
- diagnosis : String
- severity : String  [Mild / Moderate / Severe]
- examinationDate : DateTime
- consultantSignature : String
+ addClinicalNotes(notes : String) : void
+ setDiagnosis(diagnosis : String, severity : String) : void
```

**VitalSigns**
```
- vitalID : String  {PK}
- patientID : String  {FK}
- appointmentID : String  {FK}
- recordedBy : String  {FK → Staff.staffID}
- recordedDate : DateTime
- bloodPressureSystolic : Integer
- bloodPressureDiastolic : Integer
- bmi : Float
- weightKg : Float
- heightCm : Float
- bloodSugar : Float
- heartRate : Integer
+ calculateBMI(weight : Float, height : Float) : Float
+ flagAbnormalValues() : List<String>
+ compareWithPrevious(patientID : String) : String
```

**Prescription**
```
- prescriptionID : String  {PK}
- patientID : String  {FK}
- consultantID : String  {FK}
- formID : String  {FK}
- issueDate : Date
- medications : String
- dosage : String
- frequency : String
- duration : String
- instructions : String
- status : String  [Active / Completed / Cancelled]
+ generatePrescription() : void
+ sendToPharmacy() : void
+ emailToPatient() : void
+ printPrescription() : void
```

**Appointment**
```
- appointmentID : String  {PK}
- patientID : String  {FK}
- consultantID : String  {FK}
- appointmentDate : Date
- appointmentTime : Time
- durationMinutes : Integer
- type : String  [Initial / Follow-up / Emergency]
- status : String  [Scheduled / Completed / Cancelled / No-show]
- roomNumber : String
+ scheduleAppointment() : void
+ reschedule(newDate : DateTime) : void
+ cancel(reason : String) : void
+ sendReminder() : void
```

**MedicalRecord** *(summary/view entity — aggregates patient data)*
```
- recordID : String  {PK}
- patientID : String  {FK}
- createdDate : Date
- lastUpdated : Date
+ compileCompleteRecord() : void
+ exportToPDF() : File
+ shareWithSpecialist(consultantID : String) : void
```

### Class Associations (Corrected)

```
Staff <|-- Consultant        (generalisation)
Staff <|-- Nurse             (generalisation)
Staff <|-- Admin             (generalisation)

Patient "1" *-- "*" Appointment      : books        (composition — appointment cannot exist without patient)
Patient "1" *-- "*" MedicalForm      : has          (composition)
Patient "1" *-- "*" VitalSigns       : has          (composition)
Patient "1" *-- "*" Prescription     : receives     (composition)
Patient "1" *-- "1" MedicalRecord    : owns         (composition)

MedicalForm "1" *-- "1" SectionOne   : contains     (composition — section cannot exist without form)
MedicalForm "1" *-- "0..1" SectionTwo : contains   (composition — Section 2 filled after consultation, optional initially)

Consultant "1" --> "*" Appointment   : conducts     (association)
Consultant "1" --> "*" SectionTwo    : completes    (association)
Consultant "1" --> "*" Prescription  : issues       (association)

Nurse "1" --> "*" VitalSigns         : records      (association)

Appointment "1" --> "0..1" MedicalForm : generates  (association — appointment triggers form creation)
Appointment "1" --> "0..1" VitalSigns  : triggers   (association)
```

**Cardinality Summary Table:**

| Association | Multiplicity | Type | Justification |
|------------|-------------|------|--------------|
| Patient → Appointment | 1 to * | Composition | Patient can have many appointments over time |
| Patient → MedicalForm | 1 to * | Composition | A new form is created per visit type |
| Patient → VitalSigns | 1 to * | Composition | Vitals recorded at every visit |
| Patient → Prescription | 1 to * | Composition | Patient receives prescriptions over time |
| Patient → MedicalRecord | 1 to 1 | Composition | One longitudinal medical record per patient |
| MedicalForm → SectionOne | 1 to 1 | Composition | Every form has exactly one Section 1 |
| MedicalForm → SectionTwo | 1 to 0..1 | Composition | Section 2 only filled after consultation |
| Consultant → Appointment | 1 to * | Association | Consultant sees many patients |
| Consultant → Prescription | 1 to * | Association | Consultant issues many prescriptions |
| Nurse → VitalSigns | 1 to * | Association | Nurse records vitals for many patients |

---

### ERD — Entity Relationship Diagram (Corrected)

**Key corrections from original:**
- `MEDICAL_RECORDS` cannot hold single `vitalID` and `prescriptionID` FKs if a patient has many vitals/prescriptions. These links belong in the individual tables pointing back to `patientID`. `MEDICAL_RECORDS` acts as a summary header record.
- A `STAFF` table is added as the parent of `CONSULTANTS` (a Consultant is a type of Staff; nurses and admins are also Staff).
- `MEDICAL_FORMS` gains a `consultantID FK` to properly link which consultant is responsible for the form.
- `APPOINTMENTS` gains a `formID FK` to link the appointment to the form it produced.

#### Entity Table Summary

| Entity | Primary Key | Foreign Keys | Notes |
|--------|-------------|--------------|-------|
| PATIENTS | patientID | — | Core demographic table |
| STAFF | staffID | — | Supertype for all clinic staff |
| CONSULTANTS | consultantID | staffID FK | Specialised staff subtype |
| MEDICAL_FORMS | formID | patientID FK, consultantID FK, appointmentID FK | One form per visit/appointment |
| SECTION_ONE | sectionOneID | formID FK | Patient-completed section |
| SECTION_TWO | sectionTwoID | formID FK, consultantID FK | Consultant-completed section |
| VITAL_SIGNS | vitalID | patientID FK, appointmentID FK, recordedBy FK | Nurse-recorded readings |
| PRESCRIPTIONS | prescriptionID | patientID FK, consultantID FK, formID FK | Issued after consultation |
| APPOINTMENTS | appointmentID | patientID FK, consultantID FK | Booking record |
| MEDICAL_RECORDS | recordID | patientID FK | One per patient; child records link back separately |

#### Relationships

| Relationship | Notation | Justification |
|-------------|----------|--------------|
| PATIENTS to APPOINTMENTS | 1 : N | A patient can have many appointments |
| PATIENTS to MEDICAL_FORMS | 1 : N | A patient can submit many forms over time |
| PATIENTS to VITAL_SIGNS | 1 : N | Vitals recorded at each appointment |
| PATIENTS to PRESCRIPTIONS | 1 : N | Multiple prescriptions over time |
| PATIENTS to MEDICAL_RECORDS | 1 : 1 | One longitudinal record per patient |
| STAFF to CONSULTANTS | 1 : 1 | A consultant IS a staff member (specialisation) |
| CONSULTANTS to APPOINTMENTS | 1 : N | Consultant conducts many appointments |
| CONSULTANTS to PRESCRIPTIONS | 1 : N | Consultant issues many prescriptions |
| CONSULTANTS to SECTION_TWO | 1 : N | Consultant completes many Section 2 forms |
| MEDICAL_FORMS to SECTION_ONE | 1 : 1 | Every form has exactly one Section 1 |
| MEDICAL_FORMS to SECTION_TWO | 1 : 0..1 | Section 2 may not yet be completed |
| APPOINTMENTS to VITAL_SIGNS | 1 : 0..1 | One set of vitals per appointment |
| APPOINTMENTS to MEDICAL_FORMS | 1 : 0..1 | Appointment produces one form |

#### Full SQL Schema (Corrected)

```sql
CREATE TABLE PATIENTS (
    patientID     VARCHAR(20)  PRIMARY KEY,
    firstName     VARCHAR(50)  NOT NULL,
    lastName      VARCHAR(50)  NOT NULL,
    dateOfBirth   DATE         NOT NULL,
    gender        VARCHAR(10),
    phoneNumber   VARCHAR(20),
    email         VARCHAR(100) UNIQUE NOT NULL,
    address       TEXT,
    emergencyContact VARCHAR(100),
    nhsNumber     VARCHAR(20)  UNIQUE NOT NULL,
    passwordHash  VARCHAR(255) NOT NULL,
    registrationDate DATE      DEFAULT CURRENT_DATE
);

CREATE TABLE STAFF (
    staffID       VARCHAR(20)  PRIMARY KEY,
    firstName     VARCHAR(50)  NOT NULL,
    lastName      VARCHAR(50)  NOT NULL,
    email         VARCHAR(100) UNIQUE NOT NULL,
    phone         VARCHAR(20),
    passwordHash  VARCHAR(255) NOT NULL,
    role          VARCHAR(20)  NOT NULL  -- 'Consultant', 'Nurse', 'Admin'
);

CREATE TABLE CONSULTANTS (
    consultantID  VARCHAR(20)  PRIMARY KEY,
    staffID       VARCHAR(20)  NOT NULL UNIQUE,
    specialization VARCHAR(100),
    licenseNumber VARCHAR(50)  UNIQUE NOT NULL,
    FOREIGN KEY (staffID) REFERENCES STAFF(staffID)
);

CREATE TABLE APPOINTMENTS (
    appointmentID VARCHAR(20)  PRIMARY KEY,
    patientID     VARCHAR(20)  NOT NULL,
    consultantID  VARCHAR(20)  NOT NULL,
    appointmentDate DATE       NOT NULL,
    appointmentTime TIME       NOT NULL,
    durationMinutes INT        DEFAULT 30,
    type          VARCHAR(50),  -- 'Initial', 'Follow-up', 'Emergency'
    status        VARCHAR(20),  -- 'Scheduled', 'Completed', 'Cancelled', 'No-show'
    roomNumber    VARCHAR(10),
    FOREIGN KEY (patientID)    REFERENCES PATIENTS(patientID),
    FOREIGN KEY (consultantID) REFERENCES CONSULTANTS(consultantID)
);

CREATE TABLE MEDICAL_FORMS (
    formID        VARCHAR(20)  PRIMARY KEY,
    patientID     VARCHAR(20)  NOT NULL,
    consultantID  VARCHAR(20),
    appointmentID VARCHAR(20),
    formType      VARCHAR(50),  -- 'Hypertension', 'Hypotension', 'Diabetes', 'General'
    dateCreated   DATETIME     DEFAULT CURRENT_TIMESTAMP,
    status        VARCHAR(20),  -- 'Draft', 'Submitted', 'Completed'
    FOREIGN KEY (patientID)    REFERENCES PATIENTS(patientID),
    FOREIGN KEY (consultantID) REFERENCES CONSULTANTS(consultantID),
    FOREIGN KEY (appointmentID) REFERENCES APPOINTMENTS(appointmentID)
);

CREATE TABLE SECTION_ONE (
    sectionOneID  VARCHAR(20)  PRIMARY KEY,
    formID        VARCHAR(20)  NOT NULL UNIQUE,
    symptoms      TEXT,
    currentMedications TEXT,
    allergies     TEXT,
    familyHistory TEXT,
    lifestyleSmoking VARCHAR(20),
    lifestyleExercise VARCHAR(50),
    patientSignature VARCHAR(255),
    submittedDate DATETIME,
    FOREIGN KEY (formID) REFERENCES MEDICAL_FORMS(formID)
);

CREATE TABLE SECTION_TWO (
    sectionTwoID  VARCHAR(20)  PRIMARY KEY,
    formID        VARCHAR(20)  NOT NULL UNIQUE,
    consultantID  VARCHAR(20)  NOT NULL,
    clinicalNotes TEXT,
    diagnosis     VARCHAR(200),
    severity      VARCHAR(20),  -- 'Mild', 'Moderate', 'Severe'
    examinationDate DATETIME,
    consultantSignature VARCHAR(255),
    FOREIGN KEY (formID)       REFERENCES MEDICAL_FORMS(formID),
    FOREIGN KEY (consultantID) REFERENCES CONSULTANTS(consultantID)
);

CREATE TABLE VITAL_SIGNS (
    vitalID       VARCHAR(20)  PRIMARY KEY,
    patientID     VARCHAR(20)  NOT NULL,
    appointmentID VARCHAR(20),
    recordedBy    VARCHAR(20)  NOT NULL,  -- FK to STAFF.staffID (nurse)
    bpSystolic    INT,
    bpDiastolic   INT,
    heartRate     INT,
    weightKg      DECIMAL(5,2),
    heightCm      DECIMAL(5,2),
    bmi           DECIMAL(4,2),
    bloodSugar    DECIMAL(5,2),
    recordedDate  DATETIME     DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patientID)    REFERENCES PATIENTS(patientID),
    FOREIGN KEY (appointmentID) REFERENCES APPOINTMENTS(appointmentID),
    FOREIGN KEY (recordedBy)   REFERENCES STAFF(staffID)
);

CREATE TABLE PRESCRIPTIONS (
    prescriptionID VARCHAR(20) PRIMARY KEY,
    patientID     VARCHAR(20)  NOT NULL,
    consultantID  VARCHAR(20)  NOT NULL,
    formID        VARCHAR(20),
    issueDate     DATE         NOT NULL,
    medications   TEXT,
    dosage        TEXT,
    frequency     TEXT,
    duration      TEXT,
    instructions  TEXT,
    status        VARCHAR(20)  DEFAULT 'Active',  -- 'Active', 'Completed', 'Cancelled'
    FOREIGN KEY (patientID)    REFERENCES PATIENTS(patientID),
    FOREIGN KEY (consultantID) REFERENCES CONSULTANTS(consultantID),
    FOREIGN KEY (formID)       REFERENCES MEDICAL_FORMS(formID)
);

CREATE TABLE MEDICAL_RECORDS (
    recordID      VARCHAR(20)  PRIMARY KEY,
    patientID     VARCHAR(20)  NOT NULL UNIQUE,
    createdDate   DATE         DEFAULT CURRENT_DATE,
    lastUpdated   DATETIME     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patientID) REFERENCES PATIENTS(patientID)
    -- All vitals, forms, prescriptions are retrieved via patientID FK in their own tables
);
```

---

## Task 4: Enterprise Cloud Architecture Model (10 Marks)

**Tool:** Draw.io (recommended) or any CASE tool  
**Requirement:** Must include On-Premise system, AWS or Azure with VPC, and connectivity between on-premise and cloud. Must address the clinic's connectivity/digitisation problem.

### Architecture Components

#### On-Premise (Clinic LAN)
- Consultant workstations (examination rooms)
- Nurse/Admin desktops (reception)
- Prescription printer
- Local firewall / router
- Site-to-site VPN client

#### Cloud (AWS / Azure — Three-Tier VPC)

**VPC: `cvd-clinic-vpc`**

```
Internet
    |
[Internet Gateway]
    |
[Web Application Firewall (WAF)]  — blocks SQLi, XSS
    |
[Application Load Balancer]  — SSL/TLS termination
    |
 ┌──────────────────────────────────────┐
 │          PUBLIC SUBNET               │
 │  EC2 / App Service: Web Tier         │
 │  - Patient Portal (HTML/CSS/JS)      │
 │  - Staff Portal (Consultants/Nurses) │
 └──────────────────────────────────────┘
    |
 ┌──────────────────────────────────────┐
 │          PRIVATE SUBNET — App Tier   │
 │  EC2 / App Service: Business Logic   │
 │  - Form validation engine            │
 │  - Appointment scheduling service    │
 │  - Prescription generation service   │
 └──────────────────────────────────────┘
    |
 ┌──────────────────────────────────────┐
 │       PRIVATE SUBNET — DB Tier       │
 │  RDS MySQL / Azure SQL Database      │
 │  - Encrypted at rest (KMS/TDE)       │
 │  - Multi-AZ / Geo-replication        │
 │  - Daily automated backups to S3     │
 └──────────────────────────────────────┘
    |
[NAT Gateway] — allows private subnets to receive updates
[VPN Gateway / Azure VPN] — secure tunnel to clinic on-premise
```

#### Security Components

| Component | Purpose |
|-----------|---------|
| WAF | Blocks SQL injection and XSS attacks at edge |
| IAM / Azure AD | Role-based access: Patient, Nurse, Consultant, Admin roles |
| KMS / Azure Key Vault | Encryption keys for patient data at rest |
| SSL/TLS | All data in transit encrypted (HTTPS) |
| VPN Gateway | Encrypted tunnel between clinic LAN and cloud |
| Bastion Host | Jump-box for secure admin access to private subnets |
| CloudWatch / Azure Monitor | Audit logging; all access to patient records logged |
| S3 / Blob Storage | Encrypted backups and exported PDF prescriptions |

#### GDPR / NHS Compliance Notes to Include

- Data residency: UK/EU data centres only
- Right to erasure: anonymisation process defined
- Access control: patients can only see their own data
- Audit trail: all data access logged and retained for 7 years

#### Diagram Must Show

1. Internet → WAF → Load Balancer (cloud side)
2. Three-tier VPC: Public (web), Private (app), Private (database)
3. VPN tunnel between clinic and cloud
4. On-premise clinic devices connecting through VPN
5. S3/Blob backup arrow
6. IAM/Azure AD authentication flow
7. A clear key/legend for all symbols used
8. Title: "CVD Clinic Enterprise Cloud Architecture — AWS/Azure"

---

## Task 5: Prototype Implementation (30 Marks)

**Requirement:** Two interfaces — AOA (Admin/Staff desktop interface) and one of SOA (website) or COA (cloud) — connected to a database backend. The CSS must execute the main business processes from Tasks 2 and 3.

### Recommended Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript (or React.js) |
| Backend | PHP 8 or Node.js (Express) |
| Database | MySQL 8 or PostgreSQL |
| Hosting | AWS EC2 / Azure App Service |
| Email | SMTP (PHPMailer) or AWS SES |
| PDF Generation | FPDF (PHP) or Puppeteer (Node) |

### Minimum Required Screens (6 interfaces)

#### Interface 1 — Patient Portal: Login / Registration
**Functionality:** Patient registers with NHS number, DOB, email, password. Existing patient logs in. Password reset via email. Role-based redirect (patient goes to patient dashboard, staff goes to staff dashboard).

#### Interface 2 — Patient Portal: Pre-Visit Form (Section 1)
**Functionality:** Auto-filled from previous visits where applicable. Dropdowns for: symptoms (chest pain, dizziness, shortness of breath, etc.), conditions (hypertension Y/N, diabetes Y/N), smoking (Yes/No/Ex-smoker), exercise frequency. Save as draft. Submit triggers status update in `MEDICAL_FORMS` table.

#### Interface 3 — Nurse/Admin Portal: Staff Dashboard
**Functionality:** View today's appointments list with patient name, time, type, status. Record vital signs (BP, weight, height — BMI auto-calculated). Search patients by name or NHS number.

#### Interface 4 — Consultant Portal: Patient Consultation (Section 2)
**Functionality:** View submitted Section 1 alongside nurse-recorded vital signs. Text area for clinical notes. Dropdown for diagnosis (Hypertension Stage 1/2, Hypotension, Type 2 Diabetes, etc.) and severity (Mild/Moderate/Severe). Button to generate prescription.

#### Interface 5 — Prescription Generation
**Functionality:** Template auto-populated with patient name, NHS number, consultant name, date. Table for medications, dosage, frequency. Print button. Email to patient button.

#### Interface 6 — Admin Portal: Appointment Scheduling
**Functionality:** Calendar/date picker view of consultant availability. Book slot (select patient, consultant, type). Confirmation sends email/SMS notification to patient.

### Implementation Requirements from Marking Criteria

- Backend must match the ERD (correct table names, FKs, constraints)
- Prepared statements must be used (prevents SQL injection — also evidences security awareness in the evaluation)
- Password hashing (`bcrypt` or `password_hash` in PHP)
- Session management with role-based access control
- Form validation on both client side (JavaScript) and server side (PHP/Node)
- Screenshot every screen with figure numbers for the report

---

## Task 6: Agile Project Management — ScrumDesk (7 Marks)

**Tool:** ScrumDesk  
**Requirement:** Show each group member's role and activities. Share dashboard with tutorial lecturers.

### Project Setup

- **Project Name:** CVD Clinic Digital Transformation
- **Team Roles:**

| Role | Responsibilities |
|------|----------------|
| Scrum Master | Facilitates standups, removes blockers, maintains burndown chart |
| Product Owner | Writes and prioritises user stories, accepts completed tasks |
| Developer 1 | Frontend (HTML/CSS/JavaScript, form interfaces) |
| Developer 2 | Backend (PHP/Node) + database schema, CRUD operations |
| QA/Documentation | Test plans, bug tracking, report writing |

*(With 3–4 students, combine roles as needed; clearly document who does what)*

### Sprint Structure (4 Sprints × 2 Weeks)

#### Sprint 1 — Foundation (Weeks 1–2)
User stories: patient registration, login, database setup  
Tasks: create DB schema, patient registration page, login with sessions, hash passwords

#### Sprint 2 — Patient Features (Weeks 3–4)
User stories: fill Section 1 online, book appointment, view history  
Tasks: Section 1 form with dropdowns, appointment booking page, auto-save draft, email confirmation

#### Sprint 3 — Staff Features (Weeks 5–6)
User stories: nurse records vitals, consultant views forms, consultant completes Section 2  
Tasks: vital signs entry form, consultant dashboard, Section 2 completion, link to Section 1

#### Sprint 4 — Prescription & QA (Weeks 7–8)
User stories: generate prescription, email patient, admin reporting  
Tasks: prescription template, PDF generation, email sending, full test cycle, documentation

### ScrumDesk Screenshots Required in Report

1. Project board showing all user stories
2. Sprint backlog with task assignments per member
3. Burndown chart for at least one sprint
4. Team member task log showing individual contributions

---

## Task 7: Individual Reflective Evaluation (10 Marks)

**Requirement:** Each student writes individually. Must cover personal contribution, AWS/Azure analysis with 2 lab exercise references, a test plan with results, and Harvard-referenced literature.

**Word count:** 500–800 words per student.

### Structure

#### 1. Personal Contribution (~100 words)
State specifically which tasks you worked on: which BPMN lanes, which classes in StarUML, which screens you implemented, which SQL tables you created. Be precise — vague statements lose marks.

#### 2. AWS vs Azure Cloud Analysis (~200 words)

| Criteria | AWS | Azure |
|----------|-----|-------|
| Database service | RDS (MySQL/PostgreSQL) | Azure SQL Database |
| Web hosting | EC2 / Elastic Beanstalk | App Service |
| Storage | S3 | Blob Storage |
| Security | IAM, KMS, WAF | Azure AD, Key Vault |
| Pricing model | Pay-as-you-go | Pay-as-you-go |
| Free tier | 12 months | 12 months |
| GDPR data residency | UK region available | UK South region available |

Reference two specific lab exercises from module sessions. Example: *"In Week 5, the AWS VPC lab demonstrated subnet isolation; this directly informed our decision to separate the patient portal from the database tier."*

Conclude with justified recommendation: why your group chose AWS **or** Azure for this project (cost, team familiarity, NHS compatibility, etc.).

#### 3. Test Plan & Results (~150 words + table)

| Test ID | Test Case | Test Data | Expected Result | Actual Result | Pass/Fail |
|---------|-----------|-----------|-----------------|---------------|-----------|
| T01 | Patient registration | Valid NHS number, email, password | Account created; redirect to dashboard | As expected | Pass |
| T02 | Login — valid credentials | Registered email + correct password | Access granted; role-based redirect | As expected | Pass |
| T03 | Login — invalid password | Registered email + wrong password | Error message; no access | As expected | Pass |
| T04 | Section 1 — submit incomplete form | Missing required symptom field | Validation error; form not submitted | As expected | Pass |
| T05 | Section 1 — submit complete form | All fields filled | Saved to DB; status = Submitted | As expected | Pass |
| T06 | Vital signs — BMI auto-calculation | Weight 80kg, Height 175cm | BMI = 26.1 displayed | As expected | Pass |
| T07 | SQL injection attempt | `' OR '1'='1` in login field | Blocked; no DB access | As expected | Pass |
| T08 | Prescription generation | Completed Section 2 | PDF generated with correct patient details | As expected | Pass |
| T09 | Appointment double-booking | Same slot, same consultant, two patients | Second booking rejected with message | As expected | Pass |
| T10 | Session timeout | Inactive for 15 minutes | User logged out automatically | As expected | Pass |

Include brief commentary on security tests (T07, T10) and explain what prepared statements / bcrypt hashing do.

#### 4. Critical Reflection (~150 words)
- What technical challenges did you face and how did you resolve them?
- What would you do differently (e.g., "I would use React instead of plain HTML for better form state management")?
- How does this project connect to Enterprise Architecture principles covered in lectures?
- How does it prepare you for industry?

#### 5. References (Harvard Style — minimum 5)
Example format:
- AWS (2024) *Amazon Web Services Documentation*. Available at: https://docs.aws.amazon.com/ (Accessed: 1 April 2026).
- Microsoft (2025) *Azure Documentation*. Available at: https://docs.microsoft.com/azure/ (Accessed: 1 April 2026).
- Sommerville, I. (2016) *Software Engineering*. 10th ed. Boston: Pearson.
- Erl, T., Puttini, R. and Mahmood, Z. (2013) *Cloud Computing: Concepts, Technology & Architecture*. Upper Saddle River, NJ: Prentice Hall.
- NHS Digital (2023) *Data Security and Protection Toolkit*. Available at: https://www.dsptoolkit.nhs.uk/ (Accessed: 1 April 2026).

---

## Task 8: Group Conclusion (10 Marks)

**Requirement:** Summarise the work done. Must be critical, relevant, and highlight major points and issues.

**Word count:** 400–600 words.

### Structure

1. **Summary of deliverables** — List what was produced: 3 BPMN models (Bonita), class diagram + ERD (StarUML), ECA model (Draw.io), working web portal (2 interfaces + DB), ScrumDesk project management evidence
2. **How the system addresses the original problem** — Reduced manual form filling (Section 1 now done online), automated BMI calculation in vital signs, dropdown-driven forms reduce errors, digital prescriptions remove paper
3. **Technical successes** — Three-tier cloud architecture correctly implemented, role-based access control working, database matches ERD, all test cases passed
4. **Challenges and how they were resolved** — e.g., database FK constraint errors (resolved by inserting records in correct order), form validation cross-browser issues, team coordination via ScrumDesk standups
5. **Future improvements** — Mobile app for patient portal; AI-based cardiovascular risk scoring using patient history data; NHS Spine integration; wearable device data import (BP monitors, fitness trackers); telemedicine video consultation
6. **Critical reflection on enterprise architecture** — How did using BPMN, class diagrams, and ERDs before coding improve the quality of the implementation? What was the value of the cloud architecture model?

---

## Task 9: Presentation & References (8 Marks)

### Report Structure Requirements

1. Title Page — Module code (CN6001/CN5023), assignment title, group member names and student IDs, submission date
2. Table of Contents — All sections with page numbers
3. List of Figures — Every diagram and screenshot numbered sequentially
4. Introduction (Task 1)
5. Updated Case Study
6. BPMN Models (Task 2) — 3 diagrams with figure numbers and explanatory paragraphs
7. Class Diagram (Task 3) — Full diagram + explanation of classes and relationships
8. ERD (Task 3) — Full diagram + brief UML-to-ERD conversion explanation
9. Enterprise Cloud Architecture (Task 4) — Diagram + component descriptions
10. Prototype Screenshots (Task 5) — Minimum 6 screens, each with figure number and explanation
11. ScrumDesk Evidence (Task 6) — Screenshots with explanatory text
12. Individual Reflective Evaluations (Task 7) — Clearly labelled by student ID
13. Group Conclusion (Task 8)
14. References — Full Harvard-style reference list
15. Appendices — Test plan table, additional screenshots, SQL schema

### References — Harvard Style (Minimum 8–10 across the report)

All in-text citations must correspond to a full entry in the reference list. Use format: `(Author, Year)` in text. Example reference list entries:

- AWS (2024) *Amazon Web Services Documentation*. Available at: https://docs.aws.amazon.com/ (Accessed: 1 April 2026).
- Microsoft (2025) *Azure Documentation*. Available at: https://learn.microsoft.com/en-us/azure/ (Accessed: 1 April 2026).
- NHS Digital (2023) *Data Security and Protection Toolkit*. Available at: https://www.dsptoolkit.nhs.uk/ (Accessed: 1 April 2026).
- OMG (2014) *Business Process Model and Notation (BPMN) Version 2.0.2*. Needham, MA: Object Management Group.
- Sommerville, I. (2016) *Software Engineering*. 10th edn. Boston: Pearson.
- Erl, T., Puttini, R. and Mahmood, Z. (2013) *Cloud Computing: Concepts, Technology & Architecture*. Upper Saddle River, NJ: Prentice Hall.
- Fowler, M. (2003) *UML Distilled: A Brief Guide to the Standard Object Modelling Language*. 3rd edn. Boston: Addison-Wesley.
- Chen, P. (1976) 'The entity-relationship model: toward a unified view of data', *ACM Transactions on Database Systems*, 1(1), pp. 9–36.

---

## Marks Checklist

| Task | Deliverable | Marks Available | Key Requirement |
|------|-------------|-----------------|----------------|
| 1 | Introduction + updated case study | 5 | Business processes clearly described |
| 2 | 3 BPMN diagrams (Bonita) | 10 | Correct notation, all lanes, gateways, data objects |
| 3 | Class diagram + ERD (StarUML) | 10 | Full attributes + operations, correct cardinalities, ERD conversion explained |
| 4 | Enterprise Cloud Architecture (Draw.io) | 10 | On-premise + cloud VPC + VPN + security components |
| 5 | Working web portal (6 screens + DB) | 30 | Two interfaces, DB-driven, main business processes functional |
| 6 | ScrumDesk screenshots | 7 | All member roles shown, sprint burndown, user stories |
| 7 | Individual reflective evaluation | 10 | AWS/Azure analysis, 2 lab references, test plan, Harvard refs |
| 8 | Group conclusion | 10 | Critical, relevant, future improvements included |
| 9 | Presentation + references | 8 | Structured report, figure numbers, ≥8 Harvard refs |
| **Total** | | **100** | Pass mark: 40% |

---

## Diagram Issues & Corrections Summary

### Class Diagram — Issues Found

| # | Issue | Severity | Correction |
|---|-------|----------|-----------|
| 1 | `SectionOne` and `SectionTwo` use BOTH inheritance (`<|--`) AND association (`-->`) from `MedicalForm` | **Critical** | Remove the inheritance arrows; use composition (`*--`) only — they are parts of a form, not subtypes of a form |
| 2 | `Consultant` has a single `name: String` attribute | **Moderate** | Split into `firstName` and `lastName` (consistent with ERD and standard practice) |
| 3 | All attributes marked `+` (public) including IDs and passwords | **Moderate** | Mark IDs and sensitive fields as `-` (private); expose via operations |
| 4 | No `Staff` superclass — nurses who record vitals have no representation | **Significant** | Add `Staff` abstract class; `Consultant`, `Nurse`, `Admin` extend it |
| 5 | `MedicalRecord` has single `vitalID` and `prescriptionID` fields | **Significant** | Remove those FKs; `MedicalRecord` is a patient summary header; child records point back to `patientID` |
| 6 | `MedicalForm` has no `appointmentID` or `consultantID` attribute | **Moderate** | Add both — a form is created for an appointment and completed by a consultant |
| 7 | Operations lack parameter signatures | **Minor** | Add parameters and return types e.g. `examinePatient(patientID: String): void` |

### ERD — Issues Found

| # | Issue | Severity | Correction |
|---|-------|----------|-----------|
| 1 | `MEDICAL_RECORDS` has single `vitalID FK` and `prescriptionID FK` — but a patient has many vitals and prescriptions | **Critical** | Remove these FKs from `MEDICAL_RECORDS`; the relationship is already captured in `VITAL_SIGNS.patientID` and `PRESCRIPTIONS.patientID` |
| 2 | No `STAFF` table — `CONSULTANTS` serves all roles via a `role` field, but nurses (who record vitals) have no proper table entry | **Significant** | Add `STAFF` table as supertype; `CONSULTANTS` has `staffID FK`; `VITAL_SIGNS.recordedBy` references `STAFF.staffID` |
| 3 | `MEDICAL_FORMS` missing `consultantID FK` and `appointmentID FK` | **Significant** | Add both foreign keys to properly link forms to their appointment and responsible consultant |
| 4 | `APPOINTMENTS` missing `formID FK` (or the relationship is not navigable from appointment to form) | **Minor** | Either add `formID FK` to `APPOINTMENTS`, or ensure the ERD relationship line `APPOINTMENTS ||--o{ MEDICAL_FORMS` is present |
| 5 | `PATIENTS ||--|| MEDICAL_RECORDS` shown as mandatory on both sides | **Minor** | Should be `PATIENTS ||--o| MEDICAL_RECORDS` — a patient may not yet have a medical record created if they just registered |
| 6 | `CONSULTANTS` table has no link to `STAFF` — operates as a standalone entity | **Significant** | Add `staffID FK` to `CONSULTANTS` table referencing `STAFF` |
