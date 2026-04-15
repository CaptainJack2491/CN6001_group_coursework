# CN6001 / CN5023 Groupwork Case Studies Breakdown

This document provides a detailed breakdown of all 12 case studies available for the Enterprise Architecture and Cloud Computing group assignment. Each case study is analyzed based on its core requirements, implementation complexity, database schema scope, and potential ideas for the mandatory "AI or ML components".

> [!NOTE]
> The assignment requires modeling business processes (BPMN), creating an ERD/Class Diagram, drawing Enterprise/Cloud Architecture models, and developing a prototype backend-driven software system with an AI/ML component.

---

## 🟢 Easy Implementation

These case studies have straightforward workflows (usually CRUD operations and basic approval systems). Their database requirements are simple, making them great if you want to focus heavily on the frontend/cloud design and getting a solid AI/ML use case integrated quickly.

### Case Study 7: University of London Absence System
* **Overview:** A student absence management portal where students submit absence forms, teachers approve/reject them, and the system handles notifications and warnings for excessive absences.
* **Database Scope:** Simple `(Students, Teachers, Absence Requests, Notifications)`.
* **AI/ML Potential (Easy):** A classification model that automatically flags suspicious absences based on historical student data, or a predictive model identifying "at-risk" students needing intervention based on absence frequency.

### Case Study 9: UEL e-Library Systems
* **Overview:** A standard library catalog system for borrowing and returning books, tracking due dates, and managing overdue fines.
* **Database Scope:** Simple `(Users, Books, Borrowing Records, Fines, Inventory)`.
* **AI/ML Potential (Very Easy):** A classic Book Recommendation System using collaborative filtering (based on what similar students borrowed) or predicting when a popular book is likely to be returned.

### Case Study 11: UEL Electronic Cafeteria Systems
* **Overview:** A digital menu and ordering system for the university cafeteria, handling inventory tracking, click-and-collect orders, and payments.
* **Database Scope:** Simple e-commerce structure `(Students/Staff, Menu Items, Orders, Payments)`.
* **AI/ML Potential (Moderate):** Demand forecasting to predict which meals will be most popular on certain days of the week to reduce food waste, or a recommendation engine for combo meals.

---

## 🟡 Medium Implementation

These case studies feature moderately complex database relationships and business workflows. They represent standard enterprise applications and offer a great balance of demonstrating architecture skills without being overwhelmingly difficult.

### Case Study 1: Kings Estate Agent - Property Management Information System
* **Overview:** A resource management system tracking assets (buildings, computers, cars) across UK branches. It assigns assets to staff, records market value over time, and manages maintenance jobs.
* **Database Scope:** Moderate `(Assets, Categories, Staff, Maintenance Jobs, External Companies, Appraisals)`. Includes historical tracking logs.
* **AI/ML Potential (Easy):** Predictive maintenance (predicting when an asset will fail based on its age) or predicting future property/hardware depreciation values based on historical market trends.

### Case Study 3: Programme Management System
* **Overview:** A system for a training company managing seminars and courses. It handles internal/external locations and varied pricing based on delegate counts (individual vs. company registrations).
* **Database Scope:** Moderate `(Courses, Staff, Locations, Companies, Delegates, Registrations, Invoices)`. Involves varied billing and registration types.
* **AI/ML Potential (Easy):** A dynamic pricing model that adjusts course fees based on current enrollment demand, or targeted course recommendations for companies.

### Case Study 5: State University Registration System
* **Overview:** A multi-step course registration portal. Students apply, lecturers check qualifications, admission officers verify details, and credentials are sent to the student.
* **Database Scope:** Moderate `(Students, Courses, Applications, Staff, Qualifications)`. Involves state machine logic for tracking application status.
* **AI/ML Potential (Moderate):** Automating initial CV/qualification reviews using NLP (Natural Language Processing) to suggest whether a candidate meets the prerequisites, assisting the lecturer's decision.

### Case Study 8: Hardware Request Management System
* **Overview:** Similar to Case Study 1, focused specifically on a university computing department assessing and maintaining hardware assets and processing staff hardware requests.
* **Database Scope:** Moderate `(Hardware Assets, Staff, Requests, Maintenance Logs)`.
* **AI/ML Potential (Easy):** Predicting hardware failure rates or lifecycle end dates to automatically trigger replacement purchase orders.

### Case Study 10: Diabetic Health Care Systems
* **Overview:** A patient-facing app/portal for tracking diabetic health data such as blood sugar levels, diet, and insulin intake.
* **Database Scope:** Moderate `(Patients, Time-series Health Logs, Doctors, Diets)`. Requires storing and querying frequent daily time-series data.
* **AI/ML Potential (Easy):** A predictive model that analyzes recent dietary inputs to alert a patient if they are likely to experience a dangerous blood sugar spike in the next few hours.

---

## 🔴 Hard Implementation

These case studies have complex workflows, involve concurrency issues, or require intricate relational database setups. They provide opportunities to earn top marks for technical excellence but are riskier given standard coursework time constraints.

### Case Study 4: Patients’ Record for a CVD (Cardiovascular) Clinic
* **Overview:** Managing complex, multi-section medical forms filled out by both patients and consultants. Includes booking queues, tracking medical metrics (BMI, Blood pressure), and processing prescriptions.
* **Database Scope:** Complex `(Patients, Consultants, Appointments, Medical Indicators, Diagnoses, Prescriptions)`. Medical records require highly normalized databases to ensure data integrity and privacy over time.
* **AI/ML Potential (High Impact):** Very strong ML use-case. Implementing an algorithm to predict cardiovascular risk (e.g., probability of a heart condition) using patient BMI, BP, and historical metrics as inputs.

### Case Study 2: Consultancy Management System
* **Overview:** A project management system handling project engineers, multiple work packages, varying staff charging rates, document deliverables (authored by multiple staff), and outsourcing logistics.
* **Database Scope:** Complex. High amount of many-to-many relationships such as Staff assigned to multiple Work Packages, and Documents co-authored by multiple Staff.
* **AI/ML Potential (Moderate):** AI-driven auto-categorization of project deliverables or a regression model estimating the risk of project budget overruns.

### Case Study 6: State Clinic Health Information System
* **Overview:** An administrative portal handling patient billing, physical room booking (open wards vs. private rooms), clinic hardware tracking, and the assignment of doctors and nurses to treatment rooms.
* **Database Scope:** Complex. It attempts to merge a bed booking system, an IT hardware tracking system, and a financial billing system into one.
* **AI/ML Potential (Moderate):** An optimal bed assignment algorithm or predicting daily patient queue volumes to optimize nurse shift scheduling.

### Case Study 12: Railway Electronic Booking Systems
* **Overview:** A public-facing web app for continuous real-time seat booking, journey scheduling, and electronic ticketing.
* **Database Scope:** Extremely Complex. Dealing with transaction concurrency (ensuring two concurrent users don't double-book the exact same seat simultaneously) is a notoriously difficult software engineering problem.
* **AI/ML Potential (Moderate):** Algorithmic dynamic ticket pricing based on demand forecasting, similar to airline fare pricing.
