// ============================================================================
// CN6001 / CN5023 — CVD Clinic Patient Record System
// Enterprise Architecture and Cloud Computing — Group Coursework Report
// Typst Document — Minimalistic Modern Theme
// ============================================================================

// ---------------------------------------------------------------------------
// 1. THEME CONFIGURATION
// ---------------------------------------------------------------------------

#let primary   = rgb("#1a1a2e")   // Deep navy
#let accent    = rgb("#0f3460")   // Mid-blue
#let highlight = rgb("#e94560")   // Vibrant accent
#let muted     = rgb("#6c757d")   // Grey for secondary text
#let light-bg  = rgb("#f8f9fa")   // Light grey background
#let white     = rgb("#ffffff")

// Group member details — EDIT THESE
#let module-code  = "CN6001 / CN5023"
#let module-title = "Enterprise Architecture and Cloud Computing"
#let report-title = "Design and Implementation of a Web-Based Portal\nfor a CVD Clinic using Enterprise Cloud Architecture CASE Tools"
#let case-study   = "Case Study 4: Patients' Record for a CVD Clinic"
#let university   = "University of East London"
#let school       = "School of Architecture, Computing & Engineering"
#let academic-year = "2025 / 2026 — Spring Semester"
#let submission-date = "1 May 2026"

#let members = (
  (name: "Member 1 Name", id: "Student ID 1", role: "Role 1"),
  (name: "Member 2 Name", id: "Student ID 2", role: "Role 2"),
  (name: "Member 3 Name", id: "Student ID 3", role: "Role 3"),
  (name: "Member 4 Name", id: "Student ID 4", role: "Role 4"),
)

// ---------------------------------------------------------------------------
// 2. DOCUMENT SETUP — Page, Fonts, Paragraph
// ---------------------------------------------------------------------------

#set document(
  title: "CVD Clinic Patient Record System — Group Coursework",
  author: members.map(m => m.name),
)

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
  fill: primary,
  lang: "en",
  region: "GB",
)

#set par(
  justify: true,
  leading: 0.75em,
  first-line-indent: 0em,
)

#set heading(numbering: "1.1")

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(1em)
  block(width: 100%)[
    #text(size: 20pt, weight: "bold", fill: accent)[#it]
    #v(0.3em)
    #line(length: 100%, stroke: 1.5pt + highlight)
  ]
  v(0.8em)
}

#show heading.where(level: 2): it => {
  v(0.8em)
  text(size: 14pt, weight: "bold", fill: accent)[#it]
  v(0.4em)
}

#show heading.where(level: 3): it => {
  v(0.6em)
  text(size: 12pt, weight: "bold", fill: muted)[#it]
  v(0.3em)
}

// Figure styling
#show figure.caption: it => {
  text(size: 9pt, fill: muted, style: "italic")[#it]
}

// Table styling
#set table(
  stroke: 0.5pt + muted,
  inset: 8pt,
)

#show table.cell.where(y: 0): set text(weight: "bold", fill: white)
#show table.cell.where(y: 0): set table.cell(fill: accent)

// Raw code styling
#show raw.where(block: true): block.with(
  fill: light-bg,
  inset: 12pt,
  radius: 4pt,
  width: 100%,
)

// Link styling
#show link: it => text(fill: accent)[#underline[#it]]

// ---------------------------------------------------------------------------
// 3. COVER PAGE (Page 1)
// ---------------------------------------------------------------------------

#page(
  margin: (top: 0cm, bottom: 0cm, left: 0cm, right: 0cm),
  header: none,
  footer: none,
)[
  #box(
    width: 100%,
    height: 100%,
    fill: primary,
  )[
    #align(center + horizon)[
      #block(width: 80%)[
        // University & School
        #text(size: 12pt, fill: rgb("#ffffff88"), tracking: 2pt, weight: "regular")[
          #upper[#university]
        ]
        #v(0.3em)
        #text(size: 10pt, fill: rgb("#ffffff66"), tracking: 1pt)[
          #school
        ]

        #v(2em)

        // Decorative line
        #line(length: 40%, stroke: 1.5pt + highlight)

        #v(2em)

        // Report title
        #par(leading: 0.6em)[#text(size: 24pt, fill: white, weight: "bold")[
          Design and Implementation of a Web-Based Portal for a CVD Clinic
        ]]

        #v(0.8em)

        #text(size: 13pt, fill: rgb("#ffffffbb"), style: "italic")[
          Using Enterprise Cloud Architecture CASE Tools
        ]

        #v(2em)

        // Case study badge
        #box(
          fill: highlight,
          radius: 4pt,
          inset: (x: 16pt, y: 8pt),
        )[
          #text(size: 10pt, fill: white, weight: "bold")[
            #case-study
          ]
        ]

        #v(3em)

        // Module info
        #text(size: 11pt, fill: rgb("#ffffffaa"))[
          #module-code #h(1em) | #h(1em) #module-title
        ]

        #v(0.5em)

        #text(size: 10pt, fill: rgb("#ffffff88"))[
          #academic-year
        ]

        #v(3em)

        // Group members
        #box(
          width: 70%,
          stroke: 0.5pt + rgb("#ffffff33"),
          radius: 6pt,
          inset: 16pt,
        )[
          #text(size: 9pt, fill: rgb("#ffffff66"), tracking: 1.5pt)[
            #upper[Group Members]
          ]
          #v(0.8em)
          #grid(
            columns: (1fr, 1fr),
            row-gutter: 12pt,
            ..members.map(m => {
              align(center)[
                #text(size: 10pt, fill: white, weight: "medium")[#m.name] \
                #text(size: 8.5pt, fill: rgb("#ffffffaa"))[#m.id] \
                #text(size: 8pt, fill: rgb("#ffffff77"), style: "italic")[#m.role]
              ]
            })
          )
        ]

        #v(2em)

        // Submission date
        #text(size: 10pt, fill: rgb("#ffffff88"))[
          Submission Date: #submission-date
        ]
      ]
    ]
  ]
]

// ---------------------------------------------------------------------------
// 4. TABLE OF CONTENTS (Page 2)
// ---------------------------------------------------------------------------

#page(
  header: none,
  footer: context align(center, text(size: 9pt, fill: muted)[
    #module-code #h(1fr) #counter(page).display("i")
  ]),
)[
  #v(1em)
  #text(size: 22pt, weight: "bold", fill: accent)[Table of Contents]
  #v(0.3em)
  #line(length: 100%, stroke: 1.5pt + highlight)
  #v(1em)

  #outline(
    title: none,
    indent: 1.5em,
    depth: 3,
  )

  #v(2em)

  #text(size: 18pt, weight: "bold", fill: accent)[List of Figures]
  #v(0.3em)
  #line(length: 60%, stroke: 1pt + muted)
  #v(0.8em)

  #outline(
    title: none,
    target: figure.where(kind: image),
  )

  #v(1.5em)

  #text(size: 18pt, weight: "bold", fill: accent)[List of Tables]
  #v(0.3em)
  #line(length: 60%, stroke: 1pt + muted)
  #v(0.8em)

  #outline(
    title: none,
    target: figure.where(kind: table),
  )
]

// ---------------------------------------------------------------------------
// 5. CONTENT PAGES — Headers & Footers begin here
// ---------------------------------------------------------------------------

// Reset page counter for main content
#set page(
  header: context {
    let current = here().page()
    if current > 2 {
      set text(size: 8.5pt, fill: muted)
      grid(
        columns: (1fr, 1fr),
        align(left)[#module-code — #module-title],
        align(right)[CVD Clinic Patient Record System],
      )
      v(0.2em)
      line(length: 100%, stroke: 0.5pt + rgb("#dee2e6"))
    }
  },
  footer: context {
    let current = here().page()
    if current > 2 {
      line(length: 100%, stroke: 0.5pt + rgb("#dee2e6"))
      v(0.2em)
      set text(size: 8.5pt, fill: muted)
      grid(
        columns: (1fr, 1fr, 1fr),
        align(left)[#university],
        align(center)[Page #counter(page).display("1")],
        align(right)[#submission-date],
      )
    }
  },
)

#counter(page).update(1)

// ============================================================================
// SECTION 1: INTRODUCTION (5 Marks)
// ============================================================================

= Introduction <introduction>

== Overview of the CVD Clinic

A group of cardiovascular (CVD) specialists operate a clinic located in West London, providing specialised care for patients with hypertension, hypotension, diabetes-related cardiovascular conditions, and general cardiovascular health monitoring. The clinic employs cardiovascular consultants, registered nurses, and administrative staff who collectively manage patient intake, vital signs recording, specialist consultations, and prescription management.

Currently, all patient data is collected through paper-based forms that patients fill in prior to examination. Each form typically consists of two sections: *Section 1*, completed by the patient (covering personal details, symptoms, medical history, and lifestyle factors), and *Section 2*, completed by the consultant following the clinical examination (including diagnosis, clinical notes, and treatment plan). This manual process has been identified as a key source of operational inefficiency, contributing to increased waiting times, data entry errors, and limited access to historical patient records.

== Core Business Processes

The following table summarises the principal business processes currently in operation at the CVD Clinic:

#figure(
  table(
    columns: (auto, 1fr),
    [*Process*], [*Description*],
    [Patient Registration], [New patients provide personal and medical history details upon their first visit to the clinic.],
    [Pre-Examination Forms], [Patients complete Section 1 of the medical form — covering symptoms, current medications, allergies, and lifestyle factors — prior to seeing the consultant.],
    [Vital Signs Recording], [Nursing staff record BMI, blood pressure (systolic/diastolic), blood sugar levels, and heart rate before the consultation.],
    [Specialist Consultation], [The consultant reviews the patient's Section 1 data, conducts a physical examination, and completes Section 2 with diagnosis and clinical notes.],
    [Prescription Generation], [Following diagnosis, the consultant generates a prescription detailing medications, dosage, frequency, and instructions.],
    [Appointment Booking], [Administrative staff manage scheduling of initial and follow-up appointments, allocating consultant time slots.],
  ),
  caption: [Core business processes at the CVD Clinic.],
) <tab-processes>

== Proposed Digital Solution

This project proposes the design and implementation of a *web-based enterprise portal* to digitise the CVD Clinic's operations. The proposed system addresses the current pain points through the following capabilities:

- *Patient Self-Service Portal* — Enabling patients to register, complete pre-visit forms (Section 1) online, view their medical history, and book appointments remotely.
- *Staff Clinical Dashboard* — Providing consultants and nurses with a centralised interface to view patient data, record vital signs, complete clinical assessments (Section 2), and generate prescriptions.
- *Cloud-Based Infrastructure* — Hosting the system on AWS/Azure with a secure VPC architecture to ensure data availability, GDPR compliance, and disaster recovery.
- *Automated Workflows* — Implementing form validation with drop-down menus, auto-fill from historical data, and automated prescription generation to reduce manual errors.

== Scope of Work

The scope of this coursework encompasses the full enterprise architecture lifecycle:

+ Business process modelling using *Bonita BPMN*
+ Class diagram and Entity Relationship Diagram (ERD) design using *StarUML*
+ Enterprise Cloud Architecture (ECA) design using *Draw.io*
+ Prototype web portal implementation with database backend
+ Agile project management using *ScrumDesk*
+ Individual reflective evaluations and group conclusion

// ============================================================================
// SECTION 2: BUSINESS PROCESS MODEL — BPMN (10 Marks)
// ============================================================================

= Business Process Model — BPMN <bpmn>

This section presents the Business Process Model and Notation (BPMN) diagrams created using *Bonita* software. Three process models have been developed to capture the key workflows of the CVD Clinic system. Each diagram identifies the participants (lanes/pools), tasks, gateways, and data objects involved.

== Diagram 1: Patient Admission and Form Completion

The first BPMN diagram models the end-to-end patient admission process, from arrival at the clinic through to consultation and prescription receipt. The process involves three swim lanes: *Patient*, *Nurse/Admin Staff*, and *Consultant*.

#figure(
  image("images/bpmn-admission.svg", width: 100%),
  caption: [Figure 1: BPMN Diagram 1 — Patient Admission and Form Completion Process (Bonita).],
) <fig-bpmn1>

*Process Description:*

The patient arrives at the clinic and either logs into the existing portal or registers as a new patient. They then complete Section 1 of the medical form online, providing personal information, symptoms, current medications, allergies, and lifestyle factors. A form validation gateway checks whether all required fields are completed; if not, the patient is prompted to fill in missing information. Once submitted, nursing staff verify the patient's identity, record vital signs (blood pressure, BMI, heart rate, blood sugar), and enter these into the system. The patient is then directed to the consultant, who reviews the Section 1 data, conducts the examination, completes Section 2 (diagnosis, clinical notes, severity), generates a prescription, schedules a follow-up if necessary, and saves the complete medical record.

*Key BPMN Elements Used:*
- *Start/End Events* — Patient arrival and consultation completion
- *User Tasks* — Form filling, vital signs recording, clinical examination
- *Service Tasks* — Auto-save form, send email confirmation
- *Exclusive Gateways* — Form validation, diagnosis type (Hypertension/Hypotension/Diabetes)
- *Parallel Gateways* — Simultaneous BP and BMI recording
- *Data Objects* — Patient Form, Medical Record, Prescription

== Diagram 2: Appointment Booking Process

The second BPMN diagram captures the appointment scheduling workflow involving the *Patient* and *Administrative Staff* lanes.

#figure(
  image("images/bpmn-booking.svg", width: 100%),
  caption: [Figure 2: BPMN Diagram 2 — Appointment Booking Process (Bonita).],
) <fig-bpmn2>

*Process Description:*

The patient initiates an appointment request through the online portal. Administrative staff check the consultant's schedule and available time slots. An exclusive gateway determines whether the preferred date is available — if not, the patient selects an alternative date. Once confirmed, the admin blocks the appointment slot, sends a confirmation email/SMS to the patient, and dispatches a pre-visit form link for the patient to complete Section 1 in advance of their visit.

== Diagram 3: Form Processing and Data Flow

The third BPMN diagram illustrates how data flows between Section 1 (patient-completed) and Section 2 (consultant-completed) to create a comprehensive medical record.

#figure(
  image("images/bpmn-dataflow.svg", width: 100%),
  caption: [Figure 3: BPMN Diagram 3 — Form Processing and Data Flow (Bonita).],
) <fig-bpmn3>

*Process Description:*

This diagram models the data lifecycle from initial patient form submission through clinical assessment to complete medical record compilation. Section 1 data (symptoms, medical history) flows from the patient to the system. The nurse adds vital signs data. The consultant then accesses the combined data, performs the examination, and populates Section 2 (clinical notes, diagnosis, severity). The system combines all data objects — Section 1, vital signs, and Section 2 — into a unified Medical Record, which triggers the prescription generation service task.

== Summary of BPMN Notation Usage

#figure(
  table(
    columns: (auto, 1fr),
    [*BPMN Element*], [*Application in CVD Clinic*],
    [Start/End Events], [Patient arrives $arrow.r$ Consultation complete],
    [User Tasks], [Fill form, Record vitals, Clinical examination],
    [Service Tasks], [Auto-save, Email confirmation, PDF generation],
    [Exclusive Gateways], [Form complete? Diagnosis type?],
    [Parallel Gateways], [Simultaneous BP + BMI checks],
    [Data Objects], [Patient Form, Medical Record, Prescription],
    [Pools/Lanes], [Patient, Nurse, Consultant, Admin],
  ),
  caption: [Summary of BPMN elements used across the three process models.],
) <tab-bpmn-elements>


// ============================================================================
// SECTION 3: CLASS DIAGRAM & ERD (10 Marks)
// ============================================================================

= Class Diagram and Entity Relationship Diagram <class-erd>

This section presents the object-oriented class model and its corresponding Entity Relationship Diagram (ERD) for the CVD Clinic system, both designed using *StarUML*. The class diagram captures the structure, attributes, operations, and relationships between domain objects, while the ERD translates these into a relational database schema.

== Class Diagram

The class diagram identifies nine core classes within the CVD Clinic domain. Each class includes its attributes (with types), operations (with parameters), and the associations/cardinalities between classes.

#figure(
  image("images/class-diagram.svg", width: 100%),
  caption: [Figure 4: UML Class Diagram for the CVD Clinic Patient Record System (StarUML).],
) <fig-class>

=== Core Classes

The following table summarises the nine classes, their key attributes, and primary operations:

#figure(
  table(
    columns: (auto, 1fr, 1fr),
    [*Class*], [*Key Attributes*], [*Key Operations*],
    [Patient], [patientID (PK), firstName, lastName, DOB, email, nhsNumber], [register(), updateProfile(), viewHistory(), bookAppointment()],
    [MedicalForm], [formID (PK), patientID (FK), formType, status, dateCreated], [submitForm(), editForm(), validateForm()],
    [SectionOne], [sectionOneID (PK), formID (FK), symptoms, medications, allergies], [autoFillFromHistory(), validateRequiredFields()],
    [SectionTwo], [sectionTwoID (PK), formID (FK), consultantID (FK), diagnosis, severity], [addClinicalNotes(), setDiagnosis()],
    [Consultant], [consultantID (PK), name, specialization, licenseNumber], [examinePatient(), completeSectionTwo(), generatePrescription()],
    [VitalSigns], [vitalID (PK), patientID (FK), bpSystolic, bpDiastolic, bmi, bloodSugar], [calculateBMI(), flagAbnormalValues()],
    [Prescription], [prescriptionID (PK), patientID (FK), consultantID (FK), medications, dosage], [generatePrescription(), sendToPharmacy(), printPrescription()],
    [Appointment], [appointmentID (PK), patientID (FK), consultantID (FK), date, type, status], [schedule(), reschedule(), cancel(), sendReminder()],
    [MedicalRecord], [recordID (PK), patientID (FK), formID (FK), vitalID (FK), prescriptionID (FK)], [compileCompleteRecord(), exportToPDF()],
  ),
  caption: [Summary of classes, attributes, and operations in the CVD Clinic system.],
) <tab-classes>

=== Class Relationships and Cardinalities

The following associations have been identified between the domain classes:

- *Patient* `1 --- *` *MedicalForm* — A patient may have multiple medical forms over time.
- *Patient* `1 --- *` *VitalSigns* — A patient has multiple vital sign recordings.
- *Patient* `1 --- *` *Prescription* — A patient may receive multiple prescriptions.
- *Patient* `1 --- *` *Appointment* — A patient can have multiple appointments.
- *Patient* `1 --- 1` *MedicalRecord* — Each patient has one comprehensive medical record.
- *MedicalForm* `1 --- 1` *SectionOne* — Each form has exactly one patient section.
- *MedicalForm* `1 --- 1` *SectionTwo* — Each form has exactly one consultant section.
- *Consultant* `1 --- *` *SectionTwo* — A consultant completes many Section 2 forms.
- *Consultant* `1 --- *` *Prescription* — A consultant issues many prescriptions.
- *Consultant* `1 --- *` *Appointment* — A consultant has many appointments.
- *Appointment* `1 --- 1` *MedicalForm* — Each appointment generates one medical form.

== Entity Relationship Diagram (ERD)

The ERD was derived from the class diagram by converting classes to entities, attributes to columns, and associations to foreign key relationships, following standard UML-to-ERD transformation principles.

#figure(
  image("images/erd.svg", width: 100%),
  caption: [Figure 5: Entity Relationship Diagram (ERD) for the CVD Clinic system (StarUML).],
) <fig-erd>

=== UML to ERD Conversion

The following table describes how each class was mapped to a relational entity:

#figure(
  table(
    columns: (auto, auto, auto, 1fr),
    [*Entity*], [*Primary Key*], [*Foreign Keys*], [*Description*],
    [Patients], [patientID], [—], [All patient demographics and contact information],
    [Consultants], [consultantID], [—], [Staff details, specialisation, licence],
    [MedicalForms], [formID], [patientID, consultantID], [Form metadata: type, status, dates],
    [SectionOne], [sectionOneID], [formID], [Patient-completed fields: symptoms, allergies, lifestyle],
    [SectionTwo], [sectionTwoID], [formID, consultantID], [Consultant-completed fields: diagnosis, severity, notes],
    [VitalSigns], [vitalID], [patientID, recordedBy], [BP, BMI, blood sugar, heart rate recordings],
    [Prescriptions], [prescriptionID], [patientID, consultantID, formID], [Medication details, dosage, instructions],
    [Appointments], [appointmentID], [patientID, consultantID], [Scheduling: date, time, type, status, room],
    [MedicalRecords], [recordID], [patientID, formID, vitalID, prescriptionID], [Compiled patient history],
  ),
  caption: [Entity table mapping from class diagram to ERD.],
) <tab-erd>

=== Relationship Types

- *1:1* — MedicalForm $arrow.l.r$ SectionOne; MedicalForm $arrow.l.r$ SectionTwo
- *1:N* — Patient $arrow.r$ MedicalForms; Patient $arrow.r$ Prescriptions; Patient $arrow.r$ Appointments
- *M:N* — Patients $arrow.l.r$ Consultants (resolved through the Appointments junction)


// ============================================================================
// SECTION 4: ENTERPRISE CLOUD ARCHITECTURE (10 Marks)
// ============================================================================

= Enterprise Cloud Architecture <eca>

This section presents the Enterprise Cloud Architecture (ECA) model for the CVD Clinic system, designed using *Draw.io*. The architecture addresses both on-premise infrastructure within the clinic and off-premise cloud services hosted on AWS, connected via a secure VPN tunnel within a Virtual Private Cloud (VPC).

== Architecture Overview

The CVD Clinic system requires the following architectural components:

+ *Patient Portal* — A public-facing web application accessible from any device.
+ *Staff Portal* — A secure internal application for clinical and administrative staff.
+ *Database Layer* — Highly sensitive patient data requiring encryption and GDPR compliance.
+ *Backup & Disaster Recovery* — Automated backups with multi-region redundancy.

#figure(
  image("images/eca-diagram.svg", width: 80%),
  caption: [Figure 6: Enterprise Cloud Architecture — On-Premise and AWS VPC Design (Draw.io).],
) <fig-eca>

== On-Premise Infrastructure (Clinic)

The clinic's local infrastructure connects to the cloud through a secured VPN tunnel:

- *Workstations* — 7 examination rooms, each equipped with a computer for consultant access
- *Admin Terminals* — Front-desk computers for appointment management
- *Network Infrastructure* — Local Area Network with firewall protection
- *Peripherals* — Prescription printers, barcode scanners for patient ID verification
- *VPN Gateway* — Site-to-site VPN tunnel providing encrypted connectivity to the cloud

== Off-Premise Cloud Architecture (AWS)

The cloud infrastructure is organised within an AWS Virtual Private Cloud (VPC) with clearly separated tiers:

=== VPC Structure

#figure(
  table(
    columns: (auto, auto, 1fr),
    [*Subnet*], [*Tier*], [*Components*],
    [Public Subnet 1], [Web Tier], [EC2 Instance — Patient Portal (frontend)],
    [Public Subnet 2], [Web Tier], [EC2 Instance — Staff Portal (frontend)],
    [Private Subnet 1], [Application Tier], [EC2 Instance — Business logic, form validation, API],
    [Private Subnet 2], [Database Tier], [RDS (MySQL/PostgreSQL) — Encrypted patient data, forms, audit logs],
    [Management Subnet], [Admin], [Bastion Host — Secure SSH access for administration],
  ),
  caption: [AWS VPC subnet structure for the CVD Clinic system.],
) <tab-vpc>

=== Connectivity and Security Components

#figure(
  table(
    columns: (auto, 1fr),
    [*Component*], [*Purpose*],
    [Internet Gateway], [Public access to the patient portal],
    [NAT Gateway], [Private subnets access internet for updates without public exposure],
    [VPN Gateway], [Encrypted site-to-site connection from clinic LAN to AWS VPC],
    [Application Load Balancer], [SSL/TLS termination, traffic distribution, high availability],
    [Web Application Firewall (WAF)], [Protection against SQL injection, XSS, and DDoS attacks],
    [IAM Roles], [Role-based access control — Patient, Nurse, Consultant, Admin roles],
    [AWS KMS], [Encryption key management for data at rest],
    [Amazon S3], [Backup storage for database snapshots and document exports],
    [CloudWatch], [Monitoring, logging, and alerting for all system components],
  ),
  caption: [AWS security and connectivity components.],
) <tab-security>

== Security and GDPR Compliance

Given the sensitivity of patient health data, the architecture implements multi-layered security:

- *Encryption at Rest* — All database storage encrypted using AWS KMS-managed keys.
- *Encryption in Transit* — TLS 1.3 enforced for all client-server communications.
- *Role-Based Access Control* — IAM policies ensuring patients access only their own data; consultants access only assigned patients.
- *Audit Logging* — All access to patient records logged via AWS CloudTrail for compliance auditing.
- *Automated Backups* — Daily RDS snapshots replicated to a secondary availability zone.
- *Data Residency* — All data stored exclusively in EU/UK AWS regions (eu-west-2, London) to comply with UK GDPR.

== Justification for Cloud Adoption

The decision to adopt cloud infrastructure over a purely on-premise solution is driven by:

+ *Scalability* — The ability to handle peak appointment booking periods without over-provisioning hardware.
+ *Accessibility* — Patients can complete pre-visit forms and book appointments from any location.
+ *Cost Efficiency* — Pay-as-you-go pricing eliminates upfront capital expenditure on servers.
+ *Disaster Recovery* — Automated backups and multi-AZ deployment ensure business continuity.
+ *Security* — AWS provides enterprise-grade security services that would be prohibitively expensive to replicate on-premise.


// ============================================================================
// SECTION 5: PROTOTYPE IMPLEMENTATION (30 Marks)
// ============================================================================

= Prototype Implementation <prototype>

This section documents the implementation of the Client-Server System (CSS) prototype for the CVD Clinic. The prototype comprises a web-based portal with a database backend, demonstrating the core business processes identified in the BPMN models and the data structures defined in the class diagram and ERD.

== Technology Stack

#figure(
  table(
    columns: (auto, 1fr),
    [*Layer*], [*Technology*],
    [Frontend], [HTML5, CSS3, JavaScript (responsive design)],
    [Backend], [PHP / Node.js (server-side logic)],
    [Database], [MySQL (hosted on AWS RDS)],
    [Hosting], [AWS EC2 instances within VPC],
    [Version Control], [Git / GitHub],
  ),
  caption: [Technology stack used for the prototype implementation.],
) <tab-tech-stack>

== Database Implementation

The database schema was implemented based on the ERD from @class-erd. The following SQL demonstrates the core table creation:

```sql
CREATE TABLE Patients (
    patientID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE,
    gender VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    address TEXT,
    nhsNumber VARCHAR(20) UNIQUE,
    password_hash VARCHAR(255),
    registrationDate DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Consultants (
    consultantID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    licenseNumber VARCHAR(50),
    email VARCHAR(100),
    password_hash VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE MedicalForms (
    formID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    formType VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Draft',
    createdDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);

CREATE TABLE Appointments (
    appointmentID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    consultantID VARCHAR(20),
    appointmentDate DATE,
    appointmentTime TIME,
    duration INT DEFAULT 30,
    type VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Scheduled',
    roomNumber VARCHAR(10),
    FOREIGN KEY (patientID) REFERENCES Patients(patientID),
    FOREIGN KEY (consultantID) REFERENCES Consultants(consultantID)
);
```

== Prototype Screens

The prototype implements six key screens that demonstrate the core functionalities of the system.

=== Screen 1: Patient Login / Registration

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-login.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Patient Login / Registration Page]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Patient registration with email, password, and personal details
- Login authentication with hashed password verification
- Session management for secure portal access
- Input validation for all required fields

=== Screen 2: Pre-Visit Form (Section 1)

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-section1.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Pre-Visit Form (Section 1)]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Drop-down menus for symptoms (reducing manual entry errors)
- Auto-fill from previous visit data where available
- Client-side and server-side form validation
- Save as draft capability for incomplete forms

=== Screen 3: Staff Dashboard

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-dashboard.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Staff / Consultant Dashboard]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Today's appointments list with patient details, type, and status
- Quick access to patient records and forms
- Notifications for incomplete patient forms
- Role-based view (Consultant vs. Nurse vs. Admin)

=== Screen 4: Examination Form (Section 2)

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-section2.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Examination Form (Section 2)]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Read-only display of Section 1 (patient data) for consultant review
- Vital signs display (recorded by nursing staff)
- Free-text field for clinical notes
- Diagnosis and severity selection via drop-downs
- Direct link to prescription generation

=== Screen 5: Prescription Generation

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-prescription.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Prescription Generation]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Pre-populated patient and consultant details
- Medication entry with dosage, frequency, and duration fields
- Free-text instructions for the patient
- Print, email, and save actions

=== Screen 6: Appointment Booking

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with: #figure(image("images/screen-appointment.png", width: 80%), caption: [...])
      #block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      [Insert Screenshot — Appointment Booking]
    ]
  ]
]
    ]
  ]
]

*Functionality:*
- Date picker with available slot display
- Consultant selection from drop-down
- Appointment type selection (Initial / Follow-up / Emergency)
- Confirmation with email/SMS notification
- Prevention of double-booking through database constraints

== Key Implementation Features

- *Security* — Passwords hashed using bcrypt; prepared statements to prevent SQL injection; HTTPS enforced.
- *Responsive Design* — Mobile-friendly layout for patient access from smartphones and tablets.
- *Error Handling* — User-friendly error messages with server-side validation fallback.
- *Database Connectivity* — PDO (PHP Data Objects) or equivalent ORM for secure database access.


// ============================================================================
// SECTION 6: AGILE PROJECT MANAGEMENT (7 Marks)
// ============================================================================

= Agile Project Management <agile>

This section documents the use of *Agile ScrumDesk* software for managing the group project. The Scrum framework was adopted to plan, track, and deliver the coursework in iterative sprints. All group members' roles and activities are visible on the ScrumDesk dashboard, which has been shared with the tutorial lecturers.

== Team Roles

#figure(
  table(
    columns: (auto, auto, 1fr),
    [*Team Member*], [*Scrum Role*], [*Responsibilities*],
    [Member 1], [Scrum Master], [Facilitate daily standups, remove blockers, ensure sprint goals are met],
    [Member 2], [Product Owner], [Prioritise user stories, define acceptance criteria, accept completed work],
    [Member 3], [Developer], [Frontend development (HTML/CSS/JS), UI design, responsive layouts],
    [Member 4], [Developer / QA], [Backend development (PHP/Node.js), database, testing],
  ),
  caption: [Team roles and responsibilities within the Scrum framework.],
) <tab-roles>

== Sprint Structure

The project was divided into four two-week sprints:

=== Sprint 1: Foundation (Weeks 1--2)

*User Stories:*
- _"As a patient, I want to register an account so that I can access the portal"_
- _"As a patient, I want to login securely so that I can view my information"_
- _"As an admin, I want to add consultants to the system"_

*Tasks:* Database schema setup, patient registration page, login authentication, initial UI templates.

=== Sprint 2: Patient Features (Weeks 3--4)

*User Stories:*
- _"As a patient, I want to fill Section 1 online so that I don't wait at the clinic"_
- _"As a patient, I want to book appointments online"_
- _"As a patient, I want to view my medical history"_

*Tasks:* Section 1 form with dropdowns, appointment booking system, form auto-save, email confirmations.

=== Sprint 3: Staff Features (Weeks 5--6)

*User Stories:*
- _"As a nurse, I want to record vital signs so that consultants can review them"_
- _"As a consultant, I want to view patient forms before examination"_
- _"As a consultant, I want to complete Section 2 during consultation"_

*Tasks:* Vital signs entry form, consultant dashboard, Section 2 completion, data linking between sections.

=== Sprint 4: Prescription and Finalisation (Weeks 7--8)

*User Stories:*
- _"As a consultant, I want to generate prescriptions after examination"_
- _"As a patient, I want to receive prescriptions via email"_
- _"As an admin, I want to generate usage reports"_

*Tasks:* Prescription template, PDF generation, email integration, testing, bug fixes, documentation.

== ScrumDesk Dashboard

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      // Replace with actual ScrumDesk screenshots:
      // #figure(image("images/scrumdesk-board.png", width: 100%), caption: [...])
      // #figure(image("images/scrumdesk-burndown.png", width: 100%), caption: [...])
      #text(fill: muted, size: 10pt, style: "italic")[
      [Insert ScrumDesk Dashboard Screenshots — Sprint Board, Burndown Chart, Team Assignments]
    ]
    ]
  ]
]

== Tracking Metrics

- *Sprint Burndown Charts* — Tracking remaining story points daily to ensure sprint goals are on track.
- *Velocity* — Measuring story points completed per sprint to forecast capacity.
- *Board Columns:* Backlog $arrow.r$ To Do $arrow.r$ In Progress $arrow.r$ Testing $arrow.r$ Done


// ============================================================================
// SECTION 7: INDIVIDUAL REFLECTIVE EVALUATION (10 Marks)
// ============================================================================

= Individual Reflective Evaluation <reflection>

#text(fill: highlight, weight: "bold", size: 10pt)[
  Note: Each group member must write their own individual reflection (500--800 words). The sections below provide a template structure. Replace the placeholder text with your personal contribution.
]

== Personal Contribution

// ---- REPLACE THIS WITH YOUR INDIVIDUAL TEXT ----

_Describe the specific modules, diagrams, and tasks you personally worked on. Detail the challenges you faced and how you resolved them. For example:_

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 12pt,
  width: 100%,
)[
  #text(fill: muted, style: "italic", size: 10pt)[
    "I was responsible for designing the database schema and implementing the patient registration module. I created the ERD in StarUML and built the MySQL database with all tables and relationships. I also developed the PHP scripts for CRUD operations on patient data. The main challenge I encountered was managing the many-to-many relationship between Patients and Consultants, which I resolved by using the Appointments table as a junction table..."
  ]
]

== Cloud Technology Analysis

Evaluate the cloud technologies used for the design and implementation of the CSS. Compare AWS and Azure based on the following criteria:

#figure(
  table(
    columns: (auto, 1fr, 1fr, auto),
    [*Criteria*], [*AWS*], [*Azure*], [*Our Choice*],
    [Pricing Model], [Pay-as-you-go, complex calculator], [Similar, integrated cost management], [AWS / Azure],
    [Database Service], [RDS (MySQL, PostgreSQL)], [Azure SQL Database], [—],
    [Security], [IAM, KMS, WAF, CloudTrail], [Azure AD, Key Vault, Sentinel], [—],
    [Documentation], [Extensive, community-driven], [Good, Microsoft Learn], [—],
    [Learning Curve], [Steeper for beginners], [Easier for .NET developers], [—],
    [Free Tier], [12-month free tier, generous], [12-month free tier, comparable], [—],
  ),
  caption: [Comparison of AWS vs. Azure cloud platforms.],
) <tab-cloud-compare>

_Support your analysis with references to practical lab exercises conducted during the module (e.g., Week 5 AWS VPC lab, Week 7 Azure security lab)._

== Testing Conducted

Develop a test plan and document the results of testing carried out on the prototype:

#figure(
  table(
    columns: (auto, 1fr, 1fr, 1fr, auto),
    [*Test ID*], [*Test Case*], [*Expected Result*], [*Actual Result*], [*Status*],
    [T01], [Patient registration], [Account created, confirmation email sent], [As expected], [Pass],
    [T02], [Login with valid credentials], [Access granted to portal], [As expected], [Pass],
    [T03], [Login with invalid password], [Error message displayed], [As expected], [Pass],
    [T04], [Section 1 form submission], [Form saved to database], [As expected], [Pass],
    [T05], [Form validation — missing fields], [Error shown, submission blocked], [As expected], [Pass],
    [T06], [Concurrent appointment bookings], [No double-booking occurs], [As expected], [Pass],
    [T07], [SQL injection attempt], [Blocked, no database breach], [As expected], [Pass],
    [T08], [Password hash verification], [Passwords stored as bcrypt hashes], [As expected], [Pass],
    [T09], [Session timeout (30 min)], [User logged out automatically], [As expected], [Pass],
  ),
  caption: [Test plan with results for the CVD Clinic prototype.],
) <tab-tests>

== Learning Outcomes

_Reflect on the skills gained (technical and soft skills), what you would do differently, and how this project prepares you for industry practice._


// ============================================================================
// SECTION 8: GROUP CONCLUSION (10 Marks)
// ============================================================================

= Group Conclusion <conclusion>

== Summary of Achievements

This group coursework successfully delivered a comprehensive enterprise architecture solution for the CVD Clinic's patient record digitisation challenge. The following deliverables were completed:

- *Three BPMN process models* created using Bonita, covering patient admission, appointment booking, and form processing workflows.
- *A complete UML class diagram and ERD* designed in StarUML, identifying nine core classes and their relational database equivalents.
- *An Enterprise Cloud Architecture model* designed in Draw.io, specifying the on-premise and AWS cloud infrastructure with VPC, security, and GDPR compliance.
- *A working web portal prototype* with six functional screens (login, pre-visit form, staff dashboard, examination form, prescription generation, appointment booking), connected to a MySQL database backend.
- *Agile project management* via ScrumDesk across four sprints, with documented user stories, task boards, and burndown charts.

== Challenges and Solutions

#figure(
  table(
    columns: (1fr, 1fr),
    [*Challenge*], [*Solution*],
    [Database connection configuration across environments], [Used PDO with prepared statements and environment-specific configuration files],
    [Complex form validation with interdependent fields], [Implemented both client-side (JavaScript) and server-side (PHP) validation layers],
    [Team coordination across different schedules], [Regular standups via ScrumDesk; shared GitHub repository with branch-per-feature workflow],
    [Ensuring GDPR compliance in cloud architecture], [Restricted data residency to AWS eu-west-2 (London); implemented encryption at rest and in transit],
  ),
  caption: [Key challenges encountered and their resolutions.],
) <tab-challenges>

== Future Improvements

The current prototype establishes a solid foundation. The following enhancements are recommended for future development:

+ *Mobile Application* — Native iOS/Android app for patient self-service and appointment management.
+ *AI/ML Integration* — Predictive analytics for cardiovascular risk assessment using patient BMI, blood pressure, and historical metrics as inputs.
+ *Telemedicine* — Video consultation capability for remote follow-up appointments.
+ *NHS Integration* — API connectivity with NHS Spine for patient record interoperability.
+ *Wearable Device Integration* — Import real-time data from blood pressure monitors and fitness trackers.
+ *Automated Reporting* — Dashboard analytics for clinic management (patient throughput, appointment no-show rates).

== Final Reflection

The project demonstrated the practical application of enterprise architecture principles — from business process modelling through cloud infrastructure design to prototype implementation. The iterative Agile approach ensured continuous delivery and adaptation. Each team member contributed domain-specific expertise, and the collaborative workflow simulated real-world software development practices. The experience has strengthened the group's understanding of end-to-end system design and cloud-based deployment for healthcare information systems.


// ============================================================================
// SECTION 9: REFERENCES (4 + 4 Marks)
// ============================================================================

= References <references>

// Harvard Referencing Style — Minimum 8-10 references

+ Amazon Web Services (2025) _Amazon Web Services Documentation_. Available at: https://docs.aws.amazon.com/ (Accessed: 15 April 2026).

+ Erl, T., Puttini, R. and Mahmood, Z. (2013) _Cloud Computing: Concepts, Technology & Architecture_. Upper Saddle River, NJ: Prentice Hall.

+ Microsoft (2025) _Azure Documentation_. Available at: https://learn.microsoft.com/en-us/azure/ (Accessed: 15 April 2026).

+ Object Management Group (2014) _Business Process Model and Notation (BPMN) Version 2.0.2_. Available at: https://www.omg.org/spec/BPMN/2.0.2/ (Accessed: 10 April 2026).

+ Sommerville, I. (2016) _Software Engineering_. 10th edn. Boston: Pearson Education.

+ UK Government (2018) _Data Protection Act 2018_. Available at: https://www.legislation.gov.uk/ukpga/2018/12/contents/enacted (Accessed: 12 April 2026).

+ Schwaber, K. and Sutherland, J. (2020) _The Scrum Guide_. Available at: https://scrumguides.org/scrum-guide.html (Accessed: 14 April 2026).

+ NHS Digital (2024) _NHS Data Model and Dictionary_. Available at: https://www.datadictionary.nhs.uk/ (Accessed: 13 April 2026).

+ Fowler, M. (2004) _UML Distilled: A Brief Guide to the Standard Object Modeling Language_. 3rd edn. Boston: Addison-Wesley.

+ OWASP Foundation (2023) _OWASP Top Ten Web Application Security Risks_. Available at: https://owasp.org/www-project-top-ten/ (Accessed: 14 April 2026).


// ============================================================================
// APPENDICES
// ============================================================================

= Appendices <appendices>

== Appendix A: Full Database Schema

The complete SQL schema for all nine database tables is provided below. This extends the excerpts shown in @prototype.

```sql
-- Full SQL schema for CVD Clinic Patient Record System
-- See Task 5 for core tables; additional tables below:

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
    status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY (patientID) REFERENCES Patients(patientID),
    FOREIGN KEY (consultantID) REFERENCES Consultants(consultantID)
);

CREATE TABLE MedicalRecords (
    recordID VARCHAR(20) PRIMARY KEY,
    patientID VARCHAR(20),
    formID VARCHAR(20),
    vitalID VARCHAR(20),
    prescriptionID VARCHAR(20),
    createdDate DATE DEFAULT CURRENT_DATE,
    lastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);
```

== Appendix B: Additional Screenshots

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      \[Insert additional prototype screenshots, error handling screens, mobile views, etc.\]
    ]
  ]
]

== Appendix C: Test Evidence

#block(
  fill: light-bg,
  radius: 6pt,
  inset: 16pt,
  width: 100%,
)[
  #align(center)[
    #text(fill: muted, size: 10pt, style: "italic")[
      \[Insert screenshots of test execution results, browser console outputs, database query results\]
    ]
  ]
]
