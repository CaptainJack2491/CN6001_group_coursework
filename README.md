# CVD Clinic - Enterprise Information System

This repository contains the design, modeling, and documentation for the "Patients' Record for a CVD Clinic" (Case Study 4) as part of the CN6001/CN5023 Enterprise Architecture and Cloud Computing coursework.

## Project Structure

* **`bpmn/`**: Contains the Business Process Model and Notation (BPMN) diagrams and exported JPEGs detailing patient admission, appointment booking, and form processing.
* **`images/`**: Contains the finalized UML Class Diagram and Entity Relationship Diagram (ERD) mapping out the system architecture.
* **`architecture/`**: Contains the Enterprise Cloud Architecture model (DrawIO format) for deploying the portal on AWS/Azure.
* **`figures/`**: Contains intermediate or supplementary diagram definitions (e.g., Mermaid files).
* **`CN6001_Coursework_Report_Template.qmd`**: The main Quarto markdown file used to compile the final report.
* **`report.typ` / `report.pdf`**: Typst report files representing the finalized written submission.

## Diagrams Overview
The project heavily utilizes UML and ERD to model a robust two-part medical form system, handling patient details, appointments, vitals, consultant evaluations, and prescriptions. 

1. **Class Diagram (`images/CVD_class_diagram.svg`)**: Visualizes the system's object-oriented structure.
2. **ERD (`images/CVD_erd.svg`)**: Represents the logical database schema, properly normalized into 3NF.

## Coursework Objectives
1. Investigate, design, and model an Enterprise Architecture system using suitable CASE tools.
2. Develop a working prototype Web/Cloud portal linked to a database backend.
3. Conduct an evaluation of cloud portal technology and techniques, supported by literature.
