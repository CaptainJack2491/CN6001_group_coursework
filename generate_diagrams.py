#!/usr/bin/env python3
"""
Generate Class Diagram and ERD as SVG files for the CVD Clinic report.
Class diagram: 9 UML classes with full attributes, operations, associations, cardinalities.
ERD: Converted from class diagram using UML-to-ERD principles.
"""

import svgwrite
import math

# ============================================================================
# Theme constants
# ============================================================================
PRIMARY = "#1a1a2e"
ACCENT = "#0f3460"
HIGHLIGHT = "#e94560"
MUTED = "#6c757d"
LIGHT_BG = "#f8f9fa"
WHITE = "#ffffff"
COMPARTMENT_BG = "#f0f4f8"
CLASS_FILL = "#ffffff"
CLASS_STROKE = ACCENT
INTERFACE_FILL = "#fff8e1"
INTERFACE_STROKE = "#f57c00"
ASSOC_COLOR = ACCENT
INH_COLOR = HIGHLIGHT
AGG_COLOR = "#2e7d32"
FONT = "Helvetica, Arial, sans-serif"

# CVD Clinic Classes
CLASSES = {
    "Patient": {
        "x": 30,
        "y": 40,
        "w": 210,
        "h": 220,
        "attrs": [
            "- patientID: String {PK}",
            "- firstName: String",
            "- lastName: String",
            "- dateOfBirth: Date",
            "- gender: String",
            "- phoneNumber: String",
            "- email: String",
            "- address: String",
            "- emergencyContact: String",
            "- nhsNumber: String {UK}",
        ],
        "ops": [
            "+ register(): void",
            "+ updateProfile(): void",
            "+ viewHistory(): MedicalRecord",
            "+ bookAppointment(): Appointment",
        ],
        "stereotype": None,
    },
    "MedicalForm": {
        "x": 300,
        "y": 40,
        "w": 210,
        "h": 175,
        "attrs": [
            "- formID: String {PK}",
            "- patientID: String {FK}",
            "- formType: String",
            "- dateCreated: Date",
            "- status: String",
        ],
        "ops": [
            "+ submitForm(): void",
            "+ editForm(): void",
            "+ validateForm(): Boolean",
        ],
        "stereotype": "<<abstract>>",
    },
    "SectionOne": {
        "x": 570,
        "y": 40,
        "w": 200,
        "h": 175,
        "attrs": [
            "- sectionOneID: String {PK}",
            "- formID: String {FK}",
            "- symptoms: String",
            "- currentMedications: String",
            "- allergies: String",
            "- familyHistory: String",
            "- lifestyleFactors: String",
        ],
        "ops": [
            "+ autoFillFromHistory(): void",
            "+ validateRequiredFields(): Boolean",
        ],
        "stereotype": None,
        "parent": ("MedicalForm", "1..1"),
        "label": "extends",
    },
    "SectionTwo": {
        "x": 830,
        "y": 40,
        "w": 200,
        "h": 175,
        "attrs": [
            "- sectionTwoID: String {PK}",
            "- formID: String {FK}",
            "- consultantID: String {FK}",
            "- clinicalNotes: String",
            "- diagnosis: String",
            "- severity: String",
        ],
        "ops": [
            "+ addClinicalNotes(): void",
            "+ setDiagnosis(): void",
        ],
        "stereotype": None,
        "parent": ("MedicalForm", "1..1"),
        "label": "extends",
    },
    "Consultant": {
        "x": 30,
        "y": 320,
        "w": 210,
        "h": 175,
        "attrs": [
            "- consultantID: String {PK}",
            "- name: String",
            "- specialization: String",
            "- licenseNumber: String",
            "- email: String",
            "- phone: String",
        ],
        "ops": [
            "+ examinePatient(): void",
            "+ completeSectionTwo(): void",
            "+ generatePrescription(): Prescription",
            "+ viewPatientHistory(): void",
        ],
        "stereotype": None,
    },
    "VitalSigns": {
        "x": 300,
        "y": 270,
        "w": 210,
        "h": 190,
        "attrs": [
            "- vitalID: String {PK}",
            "- patientID: String {FK}",
            "- recordedDate: DateTime",
            "- bpSystolic: Integer",
            "- bpDiastolic: Integer",
            "- bmi: Float",
            "- weight: Float",
            "- height: Float",
            "- bloodSugar: Float",
            "- heartRate: Integer",
        ],
        "ops": [
            "+ calculateBMI(): Float",
            "+ flagAbnormalValues(): void",
            "+ compareWithPrevious(): Boolean",
        ],
        "stereotype": None,
    },
    "Prescription": {
        "x": 570,
        "y": 270,
        "w": 200,
        "h": 185,
        "attrs": [
            "- prescriptionID: String {PK}",
            "- patientID: String {FK}",
            "- consultantID: String {FK}",
            "- issueDate: Date",
            "- medications: String",
            "- dosage: String",
            "- frequency: String",
            "- duration: String",
            "- instructions: String",
            "- status: String",
        ],
        "ops": [
            "+ generatePrescription(): void",
            "+ sendToPharmacy(): void",
            "+ emailToPatient(): void",
            "+ printPrescription(): void",
        ],
        "stereotype": None,
    },
    "Appointment": {
        "x": 830,
        "y": 270,
        "w": 200,
        "h": 185,
        "attrs": [
            "- appointmentID: String {PK}",
            "- patientID: String {FK}",
            "- consultantID: String {FK}",
            "- appointmentDate: DateTime",
            "- duration: Integer",
            "- type: String",
            "- status: String",
            "- roomNumber: String",
        ],
        "ops": [
            "+ scheduleAppointment(): void",
            "+ reschedule(): void",
            "+ cancel(): void",
            "+ sendReminder(): void",
        ],
        "stereotype": None,
    },
    "MedicalRecord": {
        "x": 430,
        "y": 520,
        "w": 230,
        "h": 140,
        "attrs": [
            "- recordID: String {PK}",
            "- patientID: String {FK}",
            "- formID: String {FK}",
            "- vitalID: String {FK}",
            "- prescriptionID: String {FK}",
            "- createdDate: Date",
            "- lastUpdated: Date",
        ],
        "ops": [
            "+ compileCompleteRecord(): void",
            "+ exportToPDF(): void",
            "+ shareWithSpecialist(): void",
        ],
        "stereotype": None,
    },
}

ASSOCIATIONS = [
    ("Patient", "MedicalForm", "1", "*", "has"),
    ("Patient", "VitalSigns", "1", "*", "records"),
    ("Patient", "Prescription", "1", "*", "receives"),
    ("Patient", "Appointment", "1", "*", "books"),
    ("Patient", "MedicalRecord", "1", "1", "has"),
    ("MedicalForm", "SectionOne", "1", "1", ""),
    ("MedicalForm", "SectionTwo", "1", "1", ""),
    ("Consultant", "SectionTwo", "1", "*", "completes"),
    ("Consultant", "Prescription", "1", "*", "issues"),
    ("Consultant", "Appointment", "1", "*", "conducts"),
    ("Appointment", "MedicalForm", "1", "1", "generates"),
    ("VitalSigns", "MedicalRecord", "*", "1", "part of"),
]


def draw_class(dwg, name, info):
    x, y, w, h = info["x"], info["y"], info["w"], info["h"]
    is_abstract = info.get("stereotype") == "<<abstract>>"

    fill = INTERFACE_FILL if is_abstract else CLASS_FILL
    stroke = INTERFACE_STROKE if is_abstract else CLASS_STROKE

    # Main box
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, h),
            rx=6,
            ry=6,
            fill=fill,
            stroke=stroke,
            stroke_width=2,
        )
    )

    # Header
    hdr_h = 32 if not is_abstract else 44
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, hdr_h),
            rx=6,
            ry=6,
            fill=ACCENT if not is_abstract else INTERFACE_STROKE,
        )
    )
    # Bottom cover for header (to flatten bottom corners of header)
    dwg.add(dwg.rect(insert=(x, y + hdr_h - 8), size=(w, 8), fill=fill))

    # Header text
    if is_abstract:
        dwg.add(
            dwg.text(
                info["stereotype"],
                insert=(x + w / 2, y + 14),
                text_anchor="middle",
                font_size=9,
                font_family=FONT,
                fill=WHITE,
                font_style="italic",
            )
        )
        dwg.add(
            dwg.text(
                name,
                insert=(x + w / 2, y + 28),
                text_anchor="middle",
                font_size=12,
                font_family=FONT,
                fill=WHITE,
                font_weight="bold",
            )
        )
    else:
        dwg.add(
            dwg.text(
                name,
                insert=(x + w / 2, y + 21),
                text_anchor="middle",
                font_size=13,
                font_family=FONT,
                fill=WHITE,
                font_weight="bold",
            )
        )

    # Separator lines
    attr_end_y = y + hdr_h + 14 * len(info["attrs"]) + 6
    dwg.add(
        dwg.line(
            start=(x, y + hdr_h), end=(x + w, y + hdr_h), stroke=stroke, stroke_width=1
        )
    )
    dwg.add(
        dwg.line(
            start=(x, attr_end_y),
            end=(x + w, attr_end_y),
            stroke=stroke,
            stroke_width=1,
        )
    )

    # Attributes
    for i, attr in enumerate(info["attrs"]):
        ty_y = y + hdr_h + 14 + i * 14
        dwg.add(
            dwg.text(
                attr,
                insert=(x + 10, ty_y),
                text_anchor="start",
                font_size=9.5,
                font_family=FONT,
                fill=PRIMARY,
            )
        )

    # Operations
    ops_start_y = attr_end_y + 8
    for i, op in enumerate(info["ops"]):
        op_y = ops_start_y + i * 14
        dwg.add(
            dwg.text(
                op,
                insert=(x + 10, op_y),
                text_anchor="start",
                font_size=9.5,
                font_family=FONT,
                fill=PRIMARY,
            )
        )

    # Inheritance arrow for subclasses
    if "parent" in info:
        parent_name, card = info["parent"]
        px = CLASSES[parent_name]["x"] + CLASSES[parent_name]["w"] / 2
        py = CLASSES[parent_name]["y"] + CLASSES[parent_name]["h"]
        cx = x + w / 2
        cy = y
        # Hollow triangle pointing to child
        tri_size = 10
        # Line from parent to triangle
        mid_y = (py + cy) / 2
        dwg.add(
            dwg.line(
                start=(px, py), end=(px, mid_y), stroke=INH_COLOR, stroke_width=1.5
            )
        )
        dwg.add(
            dwg.line(
                start=(px, mid_y), end=(cx, cy), stroke=INH_COLOR, stroke_width=1.5
            )
        )
        # Triangle at child
        dwg.add(
            dwg.polygon(
                [
                    (cx, cy),
                    (cx - tri_size / 2, cy + tri_size),
                    (cx + tri_size / 2, cy + tri_size),
                ],
                fill=WHITE,
                stroke=INH_COLOR,
                stroke_width=1.5,
            )
        )


def draw_association(dwg, from_name, to_name, from_card, to_card, label=""):
    f = CLASSES[from_name]
    t = CLASSES[to_name]

    fx1, fy1 = f["x"] + f["w"], f["y"] + f["h"] / 2
    fx2, fy2 = f["x"] + f["w"] / 2, f["y"] + f["h"]

    tx1, ty1 = t["x"], t["y"] + t["h"] / 2
    tx2, ty2 = t["x"] + t["w"] / 2, t["y"]

    # Simple heuristic: pick best connection points
    def dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    candidates_to = [(tx1, ty1), (tx2, ty2), (t["x"] + t["w"], t["y"] + t["h"] / 2)]
    best_to = min(candidates_to, key=lambda c: dist((fx1, fy1), c))

    # Draw line with arrow
    marker = dwg.marker(
        insert=(6, 3), size=(8, 6), orient="auto", markerUnits="strokeWidth"
    )
    marker.add(dwg.polygon([(0, 0), (6, 3), (0, 6)], fill=ASSOC_COLOR))
    dwg.defs.add(marker)

    # If cardinalities suggest "one" show solid dot, "many" show open diamond
    # For now use simple line
    dwg.add(
        dwg.line(
            start=(fx1, fy1),
            end=best_to,
            stroke=ASSOC_COLOR,
            stroke_width=1.5,
            marker_end=marker.get_funciri(),
        )
    )

    # Cardinality labels
    mid_x = (fx1 + best_to[0]) / 2
    mid_y = (fy1 + best_to[1]) / 2

    if from_card not in ("1", ""):
        dwg.add(
            dwg.text(
                from_card,
                insert=(fx1 - 20, fy1 - 5),
                text_anchor="middle",
                font_size=9,
                font_family=FONT,
                fill=HIGHLIGHT,
                font_weight="bold",
            )
        )
    if to_card not in ("*", "1", ""):
        dwg.add(
            dwg.text(
                to_card,
                insert=(best_to[0] + 12, best_to[1]),
                text_anchor="start",
                font_size=9,
                font_family=FONT,
                fill=HIGHLIGHT,
                font_weight="bold",
            )
        )

    if label:
        dwg.add(
            dwg.text(
                label,
                insert=(mid_x, mid_y - 6),
                text_anchor="middle",
                font_size=8.5,
                font_family=FONT,
                fill=ASSOC_COLOR,
                font_style="italic",
            )
        )


def generate_class_diagram():
    W, H = 1100, 720
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/class-diagram.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )

    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "Class Diagram — CVD Clinic Patient Record System",
            insert=(W / 2, 26),
            text_anchor="middle",
            font_size=16,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(80, 36), end=(W - 80, 36), stroke=HIGHLIGHT, stroke_width=1.5)
    )

    # Subtitle
    dwg.add(
        dwg.text(
            "Designed using StarUML  |  UML 2.5 Notation  |  9 Classes with full attributes and operations",
            insert=(W / 2, 52),
            text_anchor="middle",
            font_size=10,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # Draw all classes
    for name, info in CLASSES.items():
        draw_class(dwg, name, info)

    # Draw associations (skip ones already shown as inheritance)
    inh_pairs = {(v["parent"][0], k) for k, v in CLASSES.items() if "parent" in v}
    for from_name, to_name, from_card, to_card, label in ASSOCIATIONS:
        if (from_name, to_name) not in inh_pairs and (
            to_name,
            from_name,
        ) not in inh_pairs:
            draw_association(dwg, from_name, to_name, from_card, to_card, label)

    # Legend
    leg_y = H - 65
    dwg.add(
        dwg.rect(
            insert=(30, leg_y - 10),
            size=(W - 60, 55),
            fill=WHITE,
            stroke=MUTED,
            stroke_width=0.5,
            rx=6,
        )
    )
    dwg.add(
        dwg.text(
            "Legend:",
            insert=(45, leg_y + 5),
            font_size=10,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )

    legend_squares = [
        ("Class (entity)", CLASS_FILL, CLASS_STROKE),
        ("Abstract class", INTERFACE_FILL, INTERFACE_STROKE),
    ]
    legend_lines = [
        ("Association", ASSOC_COLOR),
        ("Inheritance", INH_COLOR),
    ]
    legend_text = [
        "PK = Primary Key",
        "FK = Foreign Key",
        "{UK} = Unique",
    ]

    lx = 120
    ly = leg_y + 2
    for lbl, fill, stroke in legend_squares:
        dwg.add(
            dwg.rect(
                insert=(lx, ly - 10),
                size=(18, 14),
                rx=2,
                fill=fill,
                stroke=stroke,
                stroke_width=1.5,
            )
        )
        dwg.add(
            dwg.text(
                lbl, insert=(lx + 24, ly + 4), font_size=9, font_family=FONT, fill=MUTED
            )
        )
        lx += 150

    for lbl, col in legend_lines:
        dwg.add(
            dwg.line(
                start=(lx, ly - 3), end=(lx + 18, ly - 3), stroke=col, stroke_width=2
            )
        )
        dwg.add(
            dwg.text(
                lbl, insert=(lx + 24, ly + 4), font_size=9, font_family=FONT, fill=MUTED
            )
        )
        lx += 150

    for lbl in legend_text:
        dwg.add(
            dwg.text(
                lbl, insert=(lx, ly + 4), font_size=9, font_family=FONT, fill=MUTED
            )
        )
        lx += 120

    dwg.save()
    print("  -> class-diagram.svg created")


# ============================================================================
# ERD GENERATION
# ============================================================================

ENTITIES = {
    "Patients": {
        "x": 50,
        "y": 60,
        "w": 200,
        "h": 175,
        "pk": ["patientID"],
        "fk": [],
        "attrs": [
            ("patientID", "VARCHAR(20)", True, False),
            ("firstName", "VARCHAR(50)", False, False),
            ("lastName", "VARCHAR(50)", False, False),
            ("dateOfBirth", "DATE", False, False),
            ("gender", "VARCHAR(10)", False, False),
            ("phone", "VARCHAR(20)", False, False),
            ("email", "VARCHAR(100)", False, True),
            ("address", "TEXT", False, False),
            ("nhsNumber", "VARCHAR(20)", False, True),
            ("registrationDate", "DATE", False, False),
        ],
    },
    "Consultants": {
        "x": 50,
        "y": 280,
        "w": 200,
        "h": 135,
        "pk": ["consultantID"],
        "fk": [],
        "attrs": [
            ("consultantID", "VARCHAR(20)", True, False),
            ("firstName", "VARCHAR(50)", False, False),
            ("lastName", "VARCHAR(50)", False, False),
            ("specialization", "VARCHAR(100)", False, False),
            ("licenseNumber", "VARCHAR(50)", False, False),
            ("email", "VARCHAR(100)", False, False),
            ("password_hash", "VARCHAR(255)", False, False),
            ("role", "VARCHAR(20)", False, False),
        ],
    },
    "MedicalForms": {
        "x": 310,
        "y": 60,
        "w": 200,
        "h": 135,
        "pk": ["formID"],
        "fk": [("patientID", "Patients")],
        "attrs": [
            ("formID", "VARCHAR(20)", True, False),
            ("patientID", "VARCHAR(20)", False, False),  # FK shown
            ("formType", "VARCHAR(50)", False, False),
            ("status", "VARCHAR(20)", False, False),
            ("createdDate", "TIMESTAMP", False, False),
        ],
    },
    "SectionOne": {
        "x": 570,
        "y": 60,
        "w": 200,
        "h": 160,
        "pk": ["sectionOneID"],
        "fk": [("formID", "MedicalForms")],
        "attrs": [
            ("sectionOneID", "VARCHAR(20)", True, False),
            ("formID", "VARCHAR(20)", False, False),
            ("symptoms", "TEXT", False, False),
            ("currentMedications", "TEXT", False, False),
            ("allergies", "TEXT", False, False),
            ("familyHistory", "TEXT", False, False),
            ("lifestyleSmoking", "VARCHAR(20)", False, False),
            ("lifestyleExercise", "VARCHAR(50)", False, False),
            ("submittedDate", "TIMESTAMP", False, False),
        ],
    },
    "SectionTwo": {
        "x": 830,
        "y": 60,
        "w": 200,
        "h": 160,
        "pk": ["sectionTwoID"],
        "fk": [("formID", "MedicalForms"), ("consultantID", "Consultants")],
        "attrs": [
            ("sectionTwoID", "VARCHAR(20)", True, False),
            ("formID", "VARCHAR(20)", False, False),
            ("consultantID", "VARCHAR(20)", False, False),
            ("clinicalNotes", "TEXT", False, False),
            ("diagnosis", "VARCHAR(200)", False, False),
            ("severity", "VARCHAR(20)", False, False),
            ("completedDate", "TIMESTAMP", False, False),
        ],
    },
    "VitalSigns": {
        "x": 310,
        "y": 240,
        "w": 200,
        "h": 175,
        "pk": ["vitalID"],
        "fk": [("patientID", "Patients")],
        "attrs": [
            ("vitalID", "VARCHAR(20)", True, False),
            ("patientID", "VARCHAR(20)", False, False),
            ("appointmentID", "VARCHAR(20)", False, False),
            ("bpSystolic", "INT", False, False),
            ("bpDiastolic", "INT", False, False),
            ("heartRate", "INT", False, False),
            ("weightKg", "DECIMAL(5,2)", False, False),
            ("heightCm", "DECIMAL(5,2)", False, False),
            ("bmi", "DECIMAL(4,2)", False, False),
            ("bloodSugar", "DECIMAL(5,2)", False, False),
            ("recordedBy", "VARCHAR(20)", False, False),
            ("recordedDate", "TIMESTAMP", False, False),
        ],
    },
    "Appointments": {
        "x": 830,
        "y": 280,
        "w": 200,
        "h": 175,
        "pk": ["appointmentID"],
        "fk": [("patientID", "Patients"), ("consultantID", "Consultants")],
        "attrs": [
            ("appointmentID", "VARCHAR(20)", True, False),
            ("patientID", "VARCHAR(20)", False, False),
            ("consultantID", "VARCHAR(20)", False, False),
            ("appointmentDate", "DATE", False, False),
            ("appointmentTime", "TIME", False, False),
            ("duration", "INT", False, False),
            ("type", "VARCHAR(50)", False, False),
            ("status", "VARCHAR(20)", False, False),
            ("roomNumber", "VARCHAR(10)", False, False),
        ],
    },
    "Prescriptions": {
        "x": 570,
        "y": 280,
        "w": 200,
        "h": 180,
        "pk": ["prescriptionID"],
        "fk": [("patientID", "Patients"), ("consultantID", "Consultants")],
        "attrs": [
            ("prescriptionID", "VARCHAR(20)", True, False),
            ("patientID", "VARCHAR(20)", False, False),
            ("consultantID", "VARCHAR(20)", False, False),
            ("formID", "VARCHAR(20)", False, False),
            ("issueDate", "DATE", False, False),
            ("medications", "TEXT", False, False),
            ("dosage", "TEXT", False, False),
            ("frequency", "TEXT", False, False),
            ("duration", "TEXT", False, False),
            ("instructions", "TEXT", False, False),
            ("status", "VARCHAR(20)", False, False),
        ],
    },
    "MedicalRecords": {
        "x": 390,
        "y": 470,
        "w": 200,
        "h": 140,
        "pk": ["recordID"],
        "fk": [("patientID", "Patients")],
        "attrs": [
            ("recordID", "VARCHAR(20)", True, False),
            ("patientID", "VARCHAR(20)", False, False),
            ("formID", "VARCHAR(20)", False, False),
            ("vitalID", "VARCHAR(20)", False, False),
            ("prescriptionID", "VARCHAR(20)", False, False),
            ("createdDate", "DATE", False, False),
            ("lastUpdated", "TIMESTAMP", False, False),
        ],
    },
}

RELATIONSHIPS = [
    ("Patients", "MedicalForms", "1", "*", "1:N"),
    ("Patients", "VitalSigns", "1", "*", "1:N"),
    ("Patients", "Appointments", "1", "*", "1:N"),
    ("Patients", "Prescriptions", "1", "*", "1:N"),
    ("Patients", "MedicalRecords", "1", "1", "1:1"),
    ("MedicalForms", "SectionOne", "1", "1", "1:1"),
    ("MedicalForms", "SectionTwo", "1", "1", "1:1"),
    ("MedicalForms", "Appointments", "1", "1", "1:1"),
    ("Consultants", "SectionTwo", "1", "*", "1:N"),
    ("Consultants", "Prescriptions", "1", "*", "1:N"),
    ("Consultants", "Appointments", "1", "*", "1:N"),
]


def draw_entity(dwg, name, info):
    x, y, w, h = info["x"], info["y"], info["w"], info["h"]
    attr_h = 18
    hdr_h = 30

    # Entity box
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, h),
            rx=6,
            ry=6,
            fill=CLASS_FILL,
            stroke=CLASS_STROKE,
            stroke_width=2,
        )
    )

    # Header
    dwg.add(dwg.rect(insert=(x, y), size=(w, hdr_h), rx=6, ry=6, fill=ACCENT))
    dwg.add(dwg.rect(insert=(x, y + hdr_h - 6), size=(w, 6), fill=CLASS_FILL))

    # Entity name
    dwg.add(
        dwg.text(
            name,
            insert=(x + w / 2, y + 20),
            text_anchor="middle",
            font_size=12,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )

    # Separator
    dwg.add(
        dwg.line(
            start=(x, y + hdr_h),
            end=(x + w, y + hdr_h),
            stroke=CLASS_STROKE,
            stroke_width=1,
        )
    )

    # Attributes
    for i, (attr, dtype, pk, uk) in enumerate(info["attrs"]):
        row_y = y + hdr_h + 4 + i * attr_h
        fk = any(attr == fkattr for fkattr, _ in info["fk"])

        # Alternate row shading
        if i % 2 == 0:
            dwg.add(
                dwg.rect(
                    insert=(x, row_y),
                    size=(w, attr_h),
                    fill=rgb("#f8f9fa"),
                    stroke="none",
                )
            )

        # Key indicator
        if pk:
            dwg.add(
                dwg.text(
                    "PK",
                    insert=(x + 4, row_y + 12),
                    text_anchor="start",
                    font_size=7.5,
                    font_family=FONT,
                    fill=HIGHLIGHT,
                    font_weight="bold",
                )
            )
            ax = x + 28
        elif fk:
            dwg.add(
                dwg.text(
                    "FK",
                    insert=(x + 4, row_y + 12),
                    text_anchor="start",
                    font_size=7.5,
                    font_family=FONT,
                    fill=INTERFACE_STROKE,
                    font_weight="bold",
                )
            )
            ax = x + 28
        else:
            ax = x + 10

        # Attribute name + type
        dwg.add(
            dwg.text(
                attr,
                insert=(ax, row_y + 12),
                text_anchor="start",
                font_size=9,
                font_family=FONT,
                fill=PRIMARY,
                font_weight="500",
            )
        )
        dwg.add(
            dwg.text(
                dtype,
                insert=(x + w - 6, row_y + 12),
                text_anchor="end",
                font_size=8,
                font_family=FONT,
                fill=MUTED,
                font_style="italic",
            )
        )

        # UK underline
        if uk and not pk:
            attr_text = attr
            dwg.add(
                dwg.line(
                    start=(ax, row_y + 14),
                    end=(ax + len(attr_text) * 5.5, row_y + 14),
                    stroke=MUTED,
                    stroke_width=0.8,
                )
            )


def rgb(hex_str):
    return hex_str


def draw_relationship_line(dwg, e1, r_type, e2):
    """Draw crow's foot notation between two entities."""
    e1info = ENTITIES[e1]
    e2info = ENTITIES[e2]

    # Find closest edges
    ex1 = e1info["x"] + e1info["w"]
    ey1 = e1info["y"] + e1info["h"] / 2
    ex2 = e2info["x"]
    ey2 = e2info["y"] + e2info["h"] / 2

    # Crow's foot notation: "1" side = single line, "*" side = crow's foot
    one_side = e1 if r_type[0] == "1" else e2
    many_side = e2 if r_type[0] == "1" else e1

    os_info = ENTITIES[one_side]
    ms_info = ENTITIES[many_side]

    ox = os_info["x"] + os_info["w"] if one_side == e1 else os_info["x"]
    oy = os_info["y"] + os_info["h"] / 2
    mx = ms_info["x"] if many_side == e1 else ms_info["x"] + ms_info["w"]
    my = ms_info["y"] + ms_info["h"] / 2

    # Determine if horizontal or vertical
    if abs(oy - my) < 30:
        # Horizontal connection
        mid_x = (ox + mx) / 2
        dwg.add(
            dwg.line(
                start=(ox, oy), end=(mid_x, oy), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )
        dwg.add(
            dwg.line(
                start=(mid_x, oy), end=(mx, my), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )

        # One side: single bar
        dwg.add(
            dwg.line(
                start=(ox, oy - 6),
                end=(ox, oy + 6),
                stroke=ASSOC_COLOR,
                stroke_width=2.5,
            )
        )

        # Many side: crow's foot
        dwg.add(
            dwg.line(
                start=(mx - 8, my - 7),
                end=(mx, my),
                stroke=ASSOC_COLOR,
                stroke_width=1.5,
            )
        )
        dwg.add(
            dwg.line(
                start=(mx - 8, my + 7),
                end=(mx, my),
                stroke=ASSOC_COLOR,
                stroke_width=1.5,
            )
        )
        dwg.add(
            dwg.line(
                start=(mx - 10, my), end=(mx, my), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )
    else:
        # Vertical connection
        mid_y = (oy + my) / 2
        dwg.add(
            dwg.line(
                start=(ox, oy), end=(ox, mid_y), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )
        dwg.add(
            dwg.line(
                start=(ox, mid_y), end=(mx, my), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )

        # One side
        dwg.add(
            dwg.line(
                start=(ox - 6, oy),
                end=(ox + 6, oy),
                stroke=ASSOC_COLOR,
                stroke_width=2.5,
            )
        )

        # Many side
        dwg.add(
            dwg.line(
                start=(mx, my - 8), end=(mx, my), stroke=ASSOC_COLOR, stroke_width=1.5
            )
        )
        dwg.add(
            dwg.line(
                start=(mx - 7, my - 8),
                end=(mx, my),
                stroke=ASSOC_COLOR,
                stroke_width=1.5,
            )
        )
        dwg.add(
            dwg.line(
                start=(mx + 7, my - 8),
                end=(mx, my),
                stroke=ASSOC_COLOR,
                stroke_width=1.5,
            )
        )

        # 1:1 dashed line for vertical
        if r_type == "1:1":
            dwg.add(
                dwg.line(
                    start=(ox - 6, oy),
                    end=(ox + 6, oy),
                    stroke=ASSOC_COLOR,
                    stroke_width=2.5,
                )
            )

    # Label
    lx = (ox + mx) / 2
    ly = (oy + my) / 2
    dwg.add(
        dwg.rect(
            insert=(lx - 28, ly - 10), size=(56, 16), fill=WHITE, stroke=WHITE, rx=3
        )
    )
    dwg.add(
        dwg.text(
            r_type,
            insert=(lx, ly + 4),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill=HIGHLIGHT,
            font_weight="bold",
        )
    )


def generate_erd():
    W, H = 1100, 660
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/erd.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )

    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "Entity Relationship Diagram (ERD) — CVD Clinic Patient Record System",
            insert=(W / 2, 26),
            text_anchor="middle",
            font_size=15,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(60, 36), end=(W - 60, 36), stroke=HIGHLIGHT, stroke_width=1.5)
    )
    dwg.add(
        dwg.text(
            "Converted from Class Diagram using UML-to-ERD principles  |  MySQL notation  |  Crow's foot notation",
            insert=(W / 2, 52),
            text_anchor="middle",
            font_size=10,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # Draw all entities
    for name, info in ENTITIES.items():
        draw_entity(dwg, name, info)

    # Draw relationships
    for e1, e2, c1, c2, rtype in RELATIONSHIPS:
        draw_relationship_line(dwg, e1, rtype, e2)

    # UML-to-ERD conversion notes
    notes_x = 50
    notes_y = H - 60
    dwg.add(
        dwg.rect(
            insert=(notes_x - 10, notes_y - 15),
            size=(W - 80, 50),
            fill=rgb("#f8f9fa"),
            stroke=MUTED,
            stroke_width=0.5,
            rx=5,
        )
    )
    dwg.add(
        dwg.text(
            "UML-to-ERD Conversion Notes:",
            insert=(notes_x, notes_y + 2),
            font_size=10,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    notes = [
        "Class $arrow.r$ Entity table  |  Attribute $arrow.r$ Column",
        "Primary Key (PK) preserved  |  Association $arrow.r$ Foreign Key (FK)",
        "1:1 association $arrow.r$ shared PK or FK  |  1:N association $arrow.r$ FK in 'many' entity",
        "Abstract class $arrow.r$ Regular entity (MedicalForm)  |  Composition $arrow.r$ Strong entity",
    ]
    for i, note in enumerate(notes):
        dwg.add(
            dwg.text(
                note,
                insert=(notes_x, notes_y + 18 + i * 13),
                font_size=9,
                font_family=FONT,
                fill=MUTED,
            )
        )

    # Legend
    leg_y = H - 75
    items = [
        ("Primary Key (PK)", HIGHLIGHT, "text_bold"),
        ("Foreign Key (FK)", INTERFACE_STROKE, "text_bold"),
        ("Unique (UK)", MUTED, "underline"),
        ("1:N Relationship", ASSOC_COLOR, "crow"),
        ("1:1 Relationship", ASSOC_COLOR, "one"),
    ]
    dwg.add(
        dwg.text(
            "Legend:",
            insert=(W - 380, notes_y + 2),
            font_size=10,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    for i, (lbl, col, shape) in enumerate(items):
        ix = W - 300 + i * 115
        ly = notes_y + 2
        if shape == "text_bold":
            dwg.add(
                dwg.text(
                    lbl,
                    insert=(ix, ly),
                    font_size=8.5,
                    font_family=FONT,
                    fill=col,
                    font_weight="bold",
                )
            )
        elif shape == "underline":
            dwg.add(
                dwg.text(
                    lbl, insert=(ix, ly), font_size=8.5, font_family=FONT, fill=col
                )
            )
            dwg.add(
                dwg.line(
                    start=(ix, ly + 3),
                    end=(ix + 60, ly + 3),
                    stroke=col,
                    stroke_width=0.8,
                )
            )
        elif shape == "crow":
            dwg.add(
                dwg.line(
                    start=(ix, ly + 2),
                    end=(ix + 14, ly + 2),
                    stroke=col,
                    stroke_width=1.5,
                )
            )
            dwg.add(
                dwg.line(
                    start=(ix + 10, ly - 4),
                    end=(ix + 14, ly + 2),
                    stroke=col,
                    stroke_width=1.5,
                )
            )
            dwg.add(
                dwg.line(
                    start=(ix + 10, ly + 8),
                    end=(ix + 14, ly + 2),
                    stroke=col,
                    stroke_width=1.5,
                )
            )
            dwg.add(
                dwg.text(
                    lbl,
                    insert=(ix + 20, ly + 5),
                    font_size=8,
                    font_family=FONT,
                    fill=MUTED,
                )
            )
        elif shape == "one":
            dwg.add(
                dwg.line(
                    start=(ix, ly - 4), end=(ix, ly + 8), stroke=col, stroke_width=2.5
                )
            )
            dwg.add(
                dwg.text(
                    lbl,
                    insert=(ix + 10, ly + 5),
                    font_size=8,
                    font_family=FONT,
                    fill=MUTED,
                )
            )

    dwg.save()
    print("  -> erd.svg created")


if __name__ == "__main__":
    print("Generating Class Diagram and ERD...")
    generate_class_diagram()
    generate_erd()
    print("Done!")


# ============================================================================
# CLOUD ARCHITECTURE (ECA) DIAGRAM
# ============================================================================


def draw_box(
    dwg,
    x,
    y,
    w,
    h,
    label,
    fill=CLASS_FILL,
    stroke=CLASS_STROKE,
    text_color=PRIMARY,
    sublabel="",
):
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, h),
            rx=4,
            ry=4,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    if sublabel:
        dwg.add(
            dwg.text(
                label,
                insert=(x + w / 2, y + h / 2 - 6),
                text_anchor="middle",
                font_size=9,
                font_family=FONT,
                fill=text_color,
                font_weight="bold",
            )
        )
        dwg.add(
            dwg.text(
                sublabel,
                insert=(x + w / 2, y + h / 2 + 8),
                text_anchor="middle",
                font_size=8,
                font_family=FONT,
                fill=text_color,
            )
        )
    else:
        dwg.add(
            dwg.text(
                label,
                insert=(x + w / 2, y + h / 2 + 3),
                text_anchor="middle",
                font_size=9,
                font_family=FONT,
                fill=text_color,
                font_weight="bold",
            )
        )


def draw_aws_architecture():
    W, H = 1100, 700
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/eca-diagram.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )
    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "Enterprise Cloud Architecture (ECA) — CVD Clinic Patient Record System",
            insert=(W / 2, 26),
            text_anchor="middle",
            font_size=15,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(60, 36), end=(W - 60, 36), stroke=HIGHLIGHT, stroke_width=1.5)
    )
    dwg.add(
        dwg.text(
            "AWS Cloud Architecture  |  VPC with Public, Private (App), and Database Subnets  |  GDPR-compliant",
            insert=(W / 2, 52),
            text_anchor="middle",
            font_size=10,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # ===== ON-PREMISE (Clinic) =====
    on_x, on_y, on_w, on_h = 30, 70, 180, 500
    dwg.add(
        dwg.rect(
            insert=(on_x, on_y),
            size=(on_w, on_h),
            rx=8,
            ry=8,
            fill=rgb("#f0f4f8"),
            stroke=ACCENT,
            stroke_width=2,
        )
    )
    dwg.add(
        dwg.rect(
            insert=(on_x, on_y), size=(on_w, 30), rx=8, ry=0, fill=ACCENT, stroke=ACCENT
        )
    )
    dwg.add(
        dwg.rect(insert=(on_x, on_y + on_h - 8), size=(on_w, 8), fill=rgb("#f0f4f8"))
    )
    dwg.add(
        dwg.text(
            "On-Premise (Clinic)",
            insert=(on_x + on_w / 2, on_y + 20),
            text_anchor="middle",
            font_size=11,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )

    # VPN tunnel
    vpn_x = on_x + on_w + 10
    vpn_y = on_y + on_h / 2 - 40
    dwg.add(
        dwg.rect(
            insert=(vpn_x, vpn_y),
            size=(60, 80),
            rx=6,
            fill=rgb("#fff3e0"),
            stroke="#e65100",
            stroke_width=2,
        )
    )
    dwg.add(
        dwg.text(
            "VPN\nGateway",
            insert=(vpn_x + 30, vpn_y + 40),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#e65100",
            font_weight="bold",
        )
    )
    # Arrow from clinic to VPN
    dwg.add(
        dwg.line(
            start=(on_x + on_w, on_y + on_h / 2),
            end=(vpn_x, vpn_y + 40),
            stroke=ACCENT,
            stroke_width=2,
        )
    )
    # Arrow from VPN to AWS
    dwg.add(
        dwg.line(
            start=(vpn_x + 60, vpn_y + 40),
            end=(vpn_x + 120, vpn_y + 40),
            stroke=ACCENT,
            stroke_width=2,
        )
    )

    # ===== AWS VPC =====
    vpc_x = vpn_x + 130
    vpc_y = on_y
    vpc_w = W - vpc_x - 30
    vpc_h = on_h

    dwg.add(
        dwg.rect(
            insert=(vpc_x, vpc_y),
            size=(vpc_w, vpc_h),
            rx=8,
            ry=8,
            fill=rgb("#f3e5f5"),
            stroke="#7b1fa2",
            stroke_width=2,
        )
    )
    dwg.add(
        dwg.rect(insert=(vpc_x, vpc_y), size=(vpc_w, 30), rx=8, ry=0, fill="#7b1fa2")
    )
    dwg.add(
        dwg.rect(
            insert=(vpc_x, vpc_y + vpc_h - 8), size=(vpc_w, 8), fill=rgb("#f3e5f5")
        )
    )
    dwg.add(
        dwg.text(
            "AWS Cloud (eu-west-2, London Region)",
            insert=(vpc_x + vpc_w / 2, vpc_y + 20),
            text_anchor="middle",
            font_size=11,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.text(
            "VPC: cvd-clinic-vpc (10.0.0.0/16)",
            insert=(vpc_x + vpc_w / 2, vpc_y + 46),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#7b1fa2",
            font_style="italic",
        )
    )

    # Internet Gateway
    igw_x = vpc_x + 30
    igw_y = vpc_y + 55
    dwg.add(
        dwg.rect(
            insert=(igw_x, igw_y),
            size=(100, 35),
            rx=4,
            fill=rgb("#e3f2fd"),
            stroke="#1565c0",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.text(
            "Internet Gateway",
            insert=(igw_x + 50, igw_y + 22),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#1565c0",
            font_weight="bold",
        )
    )

    # Arrow from VPN to IGW
    dwg.add(
        dwg.line(
            start=(vpn_x + 60, vpn_y + 40),
            end=(igw_x + 50, igw_y + 35),
            stroke=ACCENT,
            stroke_width=1.5,
        )
    )

    # ===== PUBLIC SUBNET 1 — Patient Portal =====
    pub1_x = vpc_x + 30
    pub1_y = igw_y + 55
    pub1_w = 180
    pub1_h = 100
    dwg.add(
        dwg.rect(
            insert=(pub1_x, pub1_y),
            size=(pub1_w, pub1_h),
            rx=6,
            fill=rgb("#e8f5e9"),
            stroke="#2e7d32",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.rect(insert=(pub1_x, pub1_y), size=(pub1_w, 24), rx=6, ry=0, fill="#2e7d32")
    )
    dwg.add(
        dwg.text(
            "Public Subnet 1 (Web Tier)",
            insert=(pub1_x + pub1_w / 2, pub1_y + 16),
            text_anchor="middle",
            font_size=8.5,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )
    draw_box(
        dwg,
        pub1_x + 25,
        pub1_y + 35,
        pub1_w - 50,
        30,
        "Patient Portal",
        rgb("#e8f5e9"),
        "#2e7d32",
        PRIMARY,
        "EC2 Instance",
    )
    dwg.add(
        dwg.text(
            "Security Group: Allow HTTPS (443)",
            insert=(pub1_x + pub1_w / 2, pub1_y + 80),
            text_anchor="middle",
            font_size=7.5,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # ===== PUBLIC SUBNET 2 — Staff Portal =====
    pub2_x = vpc_x + 30
    pub2_y = pub1_y + pub1_h + 20
    dwg.add(
        dwg.rect(
            insert=(pub2_x, pub2_y),
            size=(pub1_w, pub1_h),
            rx=6,
            fill=rgb("#e8f5e9"),
            stroke="#2e7d32",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.rect(insert=(pub2_x, pub2_y), size=(pub1_w, 24), rx=6, ry=0, fill="#2e7d32")
    )
    dwg.add(
        dwg.text(
            "Public Subnet 2 (Web Tier)",
            insert=(pub2_x + pub1_w / 2, pub2_y + 16),
            text_anchor="middle",
            font_size=8.5,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )
    draw_box(
        dwg,
        pub2_x + 25,
        pub2_y + 35,
        pub1_w - 50,
        30,
        "Staff Portal",
        rgb("#e8f5e9"),
        "#2e7d32",
        PRIMARY,
        "EC2 Instance",
    )
    dwg.add(
        dwg.text(
            "Security Group: Internal only (VPC)",
            insert=(pub2_x + pub1_w / 2, pub2_y + 80),
            text_anchor="middle",
            font_size=7.5,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # ===== LOAD BALANCER =====
    lb_x = vpc_x + 240
    lb_y = (pub1_y + pub2_y) / 2 + 20
    dwg.add(
        dwg.rect(
            insert=(lb_x, lb_y),
            size=(80, 70),
            rx=6,
            fill=rgb("#fff8e1"),
            stroke="#f57c00",
            stroke_width=2,
        )
    )
    dwg.add(
        dwg.text(
            "Application\nLoad Balancer",
            insert=(lb_x + 40, lb_y + 35),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#f57c00",
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.text(
            "SSL Termination",
            insert=(lb_x + 40, lb_y + 55),
            text_anchor="middle",
            font_size=7.5,
            font_family=FONT,
            fill=MUTED,
        )
    )

    # Arrows: IGW -> LB -> Public subnets
    dwg.add(
        dwg.line(
            start=(igw_x + 50, igw_y + 35),
            end=(lb_x + 40, lb_y),
            stroke="#f57c00",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.line(
            start=(lb_x + 40, lb_y + 70),
            end=(pub1_x + pub1_w / 2, pub1_y + pub1_h),
            stroke="#f57c00",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.line(
            start=(lb_x + 40, lb_y + 70),
            end=(pub2_x + pub1_w / 2, pub2_y),
            stroke="#f57c00",
            stroke_width=1.5,
        )
    )

    # ===== PRIVATE SUBNET 1 — App Tier =====
    priv1_x = vpc_x + 350
    priv1_y = pub1_y
    priv1_w = 180
    priv1_h = 100
    dwg.add(
        dwg.rect(
            insert=(priv1_x, priv1_y),
            size=(priv1_w, priv1_h),
            rx=6,
            fill=rgb("#fff3e0"),
            stroke="#e65100",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.rect(
            insert=(priv1_x, priv1_y), size=(priv1_w, 24), rx=6, ry=0, fill="#e65100"
        )
    )
    dwg.add(
        dwg.text(
            "Private Subnet 1 (App Tier)",
            insert=(priv1_x + priv1_w / 2, priv1_y + 16),
            text_anchor="middle",
            font_size=8.5,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )
    draw_box(
        dwg,
        priv1_x + 15,
        priv1_y + 35,
        priv1_w - 30,
        30,
        "App Server",
        rgb("#fff3e0"),
        "#e65100",
        PRIMARY,
        "EC2 (Node.js/PHP)",
    )
    dwg.add(
        dwg.text(
            "Business Logic, Form Validation, APIs",
            insert=(priv1_x + priv1_w / 2, priv1_y + 80),
            text_anchor="middle",
            font_size=7.5,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # ===== PRIVATE SUBNET 2 — Database Tier =====
    priv2_x = vpc_x + 350
    priv2_y = pub2_y
    dwg.add(
        dwg.rect(
            insert=(priv2_x, priv2_y),
            size=(priv1_w, pub1_h),
            rx=6,
            fill=rgb("#fce4ec"),
            stroke=HIGHLIGHT,
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.rect(
            insert=(priv2_x, priv2_y), size=(priv1_w, 24), rx=6, ry=0, fill=HIGHLIGHT
        )
    )
    dwg.add(
        dwg.text(
            "Private Subnet 2 (DB Tier)",
            insert=(priv2_x + priv1_w / 2, priv2_y + 16),
            text_anchor="middle",
            font_size=8.5,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )

    # RDS MySQL
    draw_box(
        dwg,
        priv2_x + 15,
        priv2_y + 35,
        150,
        30,
        "RDS MySQL",
        rgb("#fce4ec"),
        HIGHLIGHT,
        PRIMARY,
        "Multi-AZ",
    )
    # Table icons
    dwg.add(
        dwg.text(
            "Patients | MedicalForms | Prescriptions",
            insert=(priv2_x + priv1_w / 2, priv2_y + 80),
            text_anchor="middle",
            font_size=8,
            font_family=FONT,
            fill=PRIMARY,
        )
    )
    dwg.add(
        dwg.text(
            "KMS Encrypted  |  Daily Snapshots to S3",
            insert=(priv2_x + priv1_w / 2, priv2_y + 95),
            text_anchor="middle",
            font_size=7.5,
            font_family=FONT,
            fill=MUTED,
            font_style="italic",
        )
    )

    # ===== MANAGEMENT SUBNET — Bastion Host =====
    mgmt_x = vpc_x + 30
    mgmt_y = priv2_y + pub1_h + 20
    dwg.add(
        dwg.rect(
            insert=(mgmt_x, mgmt_y),
            size=(180, 70),
            rx=6,
            fill=rgb("#f3e5f5"),
            stroke="#7b1fa2",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.rect(insert=(mgmt_x, mgmt_y), size=(180, 22), rx=6, ry=0, fill="#7b1fa2")
    )
    dwg.add(
        dwg.text(
            "Management Subnet",
            insert=(mgmt_x + 90, mgmt_y + 14),
            text_anchor="middle",
            font_size=8.5,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )
    draw_box(
        dwg,
        mgmt_x + 40,
        mgmt_y + 30,
        100,
        30,
        "Bastion Host",
        rgb("#f3e5f5"),
        "#7b1fa2",
        PRIMARY,
        "SSH Admin Access",
    )

    # ===== S3 BACKUP =====
    s3_x = vpc_x + 560
    s3_y = vpc_y + 100
    dwg.add(
        dwg.rect(
            insert=(s3_x, s3_y),
            size=(120, 60),
            rx=6,
            fill=rgb("#e1f5fe"),
            stroke="#0277bd",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.text(
            "Amazon S3",
            insert=(s3_x + 60, s3_y + 20),
            text_anchor="middle",
            font_size=10,
            font_family=FONT,
            fill="#0277bd",
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.text(
            "DB Backups\n& Exports",
            insert=(s3_x + 60, s3_y + 42),
            text_anchor="middle",
            font_size=8,
            font_family=FONT,
            fill=PRIMARY,
        )
    )

    # ===== ARROW CONNECTIONS (App -> DB) =====
    # LB -> App
    dwg.add(
        dwg.line(
            start=(lb_x + 80, lb_y + 35),
            end=(priv1_x, priv1_y + 50),
            stroke="#e65100",
            stroke_width=1.5,
        )
    )
    # App -> DB
    dwg.add(
        dwg.line(
            start=(priv1_x + priv1_w, priv1_y + 50),
            end=(priv2_x, priv2_y + 50),
            stroke=HIGHLIGHT,
            stroke_width=1.5,
        )
    )
    # DB -> S3
    dwg.add(
        dwg.line(
            start=(priv2_x + priv1_w, priv2_y + 50),
            end=(s3_x, s3_y + 30),
            stroke="#0277bd",
            stroke_width=1.5,
        )
    )

    # ===== WAF & SECURITY =====
    waf_x = vpc_x + 240
    waf_y = vpc_y + 60
    dwg.add(
        dwg.rect(
            insert=(waf_x, waf_y),
            size=(80, 35),
            rx=4,
            fill=rgb("#ffebee"),
            stroke=HIGHLIGHT,
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.text(
            "AWS WAF",
            insert=(waf_x + 40, waf_y + 22),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill=HIGHLIGHT,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(
            start=(igw_x + 100, igw_y + 17),
            end=(waf_x, waf_y + 17),
            stroke=HIGHLIGHT,
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.line(
            start=(waf_x + 80, waf_y + 17),
            end=(lb_x, lb_y + 20),
            stroke=HIGHLIGHT,
            stroke_width=1.5,
        )
    )

    # CloudWatch
    cw_x = vpc_x + 560
    cw_y = s3_y + 80
    dwg.add(
        dwg.rect(
            insert=(cw_x, cw_y),
            size=(120, 55),
            rx=6,
            fill=rgb("#e8f5e9"),
            stroke="#2e7d32",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.text(
            "Amazon CloudWatch",
            insert=(cw_x + 60, cw_y + 18),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#2e7d32",
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.text(
            "Monitoring\n& Logging",
            insert=(cw_x + 60, cw_y + 38),
            text_anchor="middle",
            font_size=8,
            font_family=FONT,
            fill=PRIMARY,
        )
    )

    # ===== IAM / SECURITY NOTES =====
    sec_x = vpc_x + 560
    sec_y = cw_y + 75
    dwg.add(
        dwg.rect(
            insert=(sec_x, sec_y),
            size=(120, 120),
            rx=6,
            fill=rgb("#fff8e1"),
            stroke="#f57c00",
            stroke_width=1.5,
        )
    )
    dwg.add(
        dwg.text(
            "Security & IAM",
            insert=(sec_x + 60, sec_y + 18),
            text_anchor="middle",
            font_size=9,
            font_family=FONT,
            fill="#f57c00",
            font_weight="bold",
        )
    )
    sec_items = [
        "IAM Roles (RBAC)",
        "KMS Encryption",
        "CloudTrail Audit",
        "GDPR Compliant",
        "TLS 1.3 in Transit",
    ]
    for i, item in enumerate(sec_items):
        dwg.add(
            dwg.text(
                f"• {item}",
                insert=(sec_x + 8, sec_y + 34 + i * 16),
                text_anchor="start",
                font_size=8,
                font_family=FONT,
                fill=PRIMARY,
            )
        )

    # ===== LEGEND =====
    leg_y = H - 55
    dwg.add(
        dwg.rect(
            insert=(30, leg_y - 10),
            size=(W - 60, 45),
            fill=WHITE,
            stroke=MUTED,
            stroke_width=0.5,
            rx=5,
        )
    )
    dwg.add(
        dwg.text(
            "Legend:",
            insert=(45, leg_y + 3),
            font_size=10,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )

    leg_items = [
        ("AWS Managed Service", rgb("#e3f2fd"), "#0277bd", "rect"),
        ("EC2 Compute Instance", rgb("#e8f5e9"), "#2e7d32", "rect"),
        ("Encrypted Storage", rgb("#fce4ec"), HIGHLIGHT, "rect"),
        ("VPN / Secure Tunnel", rgb("#fff3e0"), "#e65100", "rect"),
        ("Internet-facing", rgb("#e3f2fd"), "#1565c0", "arrow"),
        ("Internal VPC Flow", rgb("#f3e5f5"), "#7b1fa2", "arrow"),
    ]
    lx = 120
    for lbl, fill, stroke, shape in leg_items:
        if shape == "rect":
            dwg.add(
                dwg.rect(
                    insert=(lx, leg_y - 6),
                    size=(16, 14),
                    rx=2,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=1.5,
                )
            )
        elif shape == "arrow":
            dwg.add(
                dwg.line(
                    start=(lx, leg_y + 1),
                    end=(lx + 16, leg_y + 1),
                    stroke=stroke,
                    stroke_width=2,
                )
            )
        dwg.add(
            dwg.text(
                lbl,
                insert=(lx + 22, leg_y + 4),
                font_size=8.5,
                font_family=FONT,
                fill=MUTED,
            )
        )
        lx += 160

    dwg.save()
    print("  -> eca-diagram.svg created")


if __name__ == "__main__":
    pass  # already run above
