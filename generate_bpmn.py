#!/usr/bin/env python3
"""
Generate BPMN diagrams as SVG files for the CVD Clinic report.
Uses svgwrite to create proper BPMN notation with swim lanes.
"""

import svgwrite

# ============================================================================
# Theme constants
# ============================================================================
PRIMARY = "#1a1a2e"
ACCENT = "#0f3460"
HIGHLIGHT = "#e94560"
MUTED = "#6c757d"
LIGHT_BG = "#f8f9fa"
WHITE = "#ffffff"
LANE_COLORS = ["#eef2f7", "#f7f0ee", "#eef7f0"]  # Subtle lane backgrounds
TASK_FILL = "#ffffff"
TASK_STROKE = ACCENT
GATEWAY_FILL = "#fff8e1"
GATEWAY_STROKE = "#f57c00"
EVENT_START_FILL = "#e8f5e9"
EVENT_START_STROKE = "#388e3c"
EVENT_END_FILL = "#ffebee"
EVENT_END_STROKE = HIGHLIGHT
DATA_FILL = "#e3f2fd"
DATA_STROKE = "#1976d2"
SERVICE_FILL = "#f3e5f5"
SERVICE_STROKE = "#7b1fa2"

FONT = "Helvetica, Arial, sans-serif"
TASK_FONT_SIZE = 11
LABEL_FONT_SIZE = 10
LANE_LABEL_FONT_SIZE = 13
TITLE_FONT_SIZE = 16


def draw_start_event(dwg, cx, cy, label="", r=14):
    """Draw BPMN start event (thin green circle)."""
    dwg.add(
        dwg.circle(
            center=(cx, cy),
            r=r,
            fill=EVENT_START_FILL,
            stroke=EVENT_START_STROKE,
            stroke_width=2.5,
        )
    )
    # Play triangle inside
    pts = [(cx - 4, cy - 6), (cx - 4, cy + 6), (cx + 6, cy)]
    dwg.add(dwg.polygon(pts, fill=EVENT_START_STROKE, opacity=0.6))
    if label:
        dwg.add(
            dwg.text(
                label,
                insert=(cx, cy + r + 14),
                text_anchor="middle",
                font_size=LABEL_FONT_SIZE,
                font_family=FONT,
                fill=MUTED,
            )
        )


def draw_end_event(dwg, cx, cy, label="", r=14):
    """Draw BPMN end event (thick red circle)."""
    dwg.add(
        dwg.circle(
            center=(cx, cy),
            r=r,
            fill=EVENT_END_FILL,
            stroke=EVENT_END_STROKE,
            stroke_width=3.5,
        )
    )
    # Square stop inside
    s = 7
    dwg.add(
        dwg.rect(
            insert=(cx - s / 2, cy - s / 2),
            size=(s, s),
            fill=EVENT_END_STROKE,
            rx=1,
            ry=1,
            opacity=0.7,
        )
    )
    if label:
        dwg.add(
            dwg.text(
                label,
                insert=(cx, cy + r + 14),
                text_anchor="middle",
                font_size=LABEL_FONT_SIZE,
                font_family=FONT,
                fill=MUTED,
            )
        )


def draw_task(dwg, x, y, w, h, label, task_type="user"):
    """Draw BPMN task (rounded rectangle with icon)."""
    fill = TASK_FILL if task_type == "user" else SERVICE_FILL
    stroke = TASK_STROKE if task_type == "user" else SERVICE_STROKE

    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, h),
            rx=8,
            ry=8,
            fill=fill,
            stroke=stroke,
            stroke_width=2,
        )
    )

    # Icon for task type
    if task_type == "user":
        # Small person icon top-left
        ix, iy = x + 10, y + 10
        dwg.add(
            dwg.circle(center=(ix, iy), r=4, fill="none", stroke=ACCENT, stroke_width=1)
        )
        dwg.add(
            dwg.line(
                start=(ix, iy + 4), end=(ix, iy + 10), stroke=ACCENT, stroke_width=1
            )
        )
        dwg.add(
            dwg.line(
                start=(ix - 4, iy + 7),
                end=(ix + 4, iy + 7),
                stroke=ACCENT,
                stroke_width=1,
            )
        )
    elif task_type == "service":
        # Gear icon
        ix, iy = x + 12, y + 12
        dwg.add(
            dwg.circle(
                center=(ix, iy),
                r=5,
                fill="none",
                stroke=SERVICE_STROKE,
                stroke_width=1.5,
            )
        )
        dwg.add(dwg.circle(center=(ix, iy), r=2, fill=SERVICE_STROKE))

    # Wrap text
    lines = wrap_text(label, w - 20)
    total_h = len(lines) * 14
    start_y = y + (h - total_h) / 2 + 10
    for i, line in enumerate(lines):
        dwg.add(
            dwg.text(
                line,
                insert=(x + w / 2, start_y + i * 14),
                text_anchor="middle",
                font_size=TASK_FONT_SIZE,
                font_family=FONT,
                fill=PRIMARY,
                font_weight="500",
            )
        )
    return (
        x + w / 2,
        y,
        x + w / 2,
        y + h,
        x,
        y + h / 2,
        x + w,
        y + h / 2,
    )  # connection points


def draw_gateway(dwg, cx, cy, label="", gtype="exclusive", size=20):
    """Draw BPMN gateway (diamond)."""
    pts = [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)]
    dwg.add(dwg.polygon(pts, fill=GATEWAY_FILL, stroke=GATEWAY_STROKE, stroke_width=2))

    if gtype == "exclusive":
        # X inside
        s = 7
        dwg.add(
            dwg.line(
                start=(cx - s, cy - s),
                end=(cx + s, cy + s),
                stroke=GATEWAY_STROKE,
                stroke_width=2.5,
            )
        )
        dwg.add(
            dwg.line(
                start=(cx + s, cy - s),
                end=(cx - s, cy + s),
                stroke=GATEWAY_STROKE,
                stroke_width=2.5,
            )
        )
    elif gtype == "parallel":
        # + inside
        s = 8
        dwg.add(
            dwg.line(
                start=(cx - s, cy),
                end=(cx + s, cy),
                stroke=GATEWAY_STROKE,
                stroke_width=2.5,
            )
        )
        dwg.add(
            dwg.line(
                start=(cx, cy - s),
                end=(cx, cy + s),
                stroke=GATEWAY_STROKE,
                stroke_width=2.5,
            )
        )

    if label:
        dwg.add(
            dwg.text(
                label,
                insert=(cx, cy + size + 16),
                text_anchor="middle",
                font_size=LABEL_FONT_SIZE - 1,
                font_family=FONT,
                fill=MUTED,
                font_style="italic",
            )
        )


def draw_data_object(dwg, x, y, w=50, h=60, label=""):
    """Draw BPMN data object (document shape)."""
    fold = 10
    path_d = f"M{x},{y} L{x + w - fold},{y} L{x + w},{y + fold} L{x + w},{y + h} L{x},{y + h} Z"
    fold_d = f"M{x + w - fold},{y} L{x + w - fold},{y + fold} L{x + w},{y + fold}"
    dwg.add(dwg.path(d=path_d, fill=DATA_FILL, stroke=DATA_STROKE, stroke_width=1.5))
    dwg.add(dwg.path(d=fold_d, fill="none", stroke=DATA_STROKE, stroke_width=1.5))
    if label:
        lines = wrap_text(label, w + 10)
        for i, line in enumerate(lines):
            dwg.add(
                dwg.text(
                    line,
                    insert=(x + w / 2, y + h + 14 + i * 12),
                    text_anchor="middle",
                    font_size=9,
                    font_family=FONT,
                    fill=DATA_STROKE,
                )
            )


def draw_arrow(dwg, x1, y1, x2, y2, label="", dashed=False, color=MUTED):
    """Draw flow arrow with optional label."""
    marker = dwg.marker(
        insert=(6, 3), size=(8, 6), orient="auto", markerUnits="strokeWidth"
    )
    marker.add(dwg.polygon([(0, 0), (6, 3), (0, 6)], fill=color))
    dwg.defs.add(marker)

    dash = "6,3" if dashed else "none"
    line = dwg.line(
        start=(x1, y1),
        end=(x2, y2),
        stroke=color,
        stroke_width=1.5,
        stroke_dasharray=dash,
    )
    line["marker-end"] = marker.get_funciri()
    dwg.add(line)

    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # Background for label
        dwg.add(
            dwg.rect(
                insert=(mx - 25, my - 10),
                size=(50, 14),
                fill=WHITE,
                rx=3,
                ry=3,
                opacity=0.9,
            )
        )
        dwg.add(
            dwg.text(
                label,
                insert=(mx, my),
                text_anchor="middle",
                font_size=9,
                font_family=FONT,
                fill=GATEWAY_STROKE,
                font_weight="600",
            )
        )


def draw_polyline_arrow(dwg, points, label="", color=MUTED, dashed=False):
    """Draw a multi-segment arrow through a list of (x,y) points."""
    marker = dwg.marker(
        insert=(6, 3), size=(8, 6), orient="auto", markerUnits="strokeWidth"
    )
    marker.add(dwg.polygon([(0, 0), (6, 3), (0, 6)], fill=color))
    dwg.defs.add(marker)

    dash = "6,3" if dashed else "none"
    pl = dwg.polyline(
        points, fill="none", stroke=color, stroke_width=1.5, stroke_dasharray=dash
    )
    pl["marker-end"] = marker.get_funciri()
    dwg.add(pl)

    if label and len(points) >= 2:
        mx = (points[0][0] + points[-1][0]) / 2
        my = (points[0][1] + points[-1][1]) / 2
        dwg.add(
            dwg.text(
                label,
                insert=(mx + 5, my - 5),
                text_anchor="start",
                font_size=9,
                font_family=FONT,
                fill=GATEWAY_STROKE,
                font_weight="600",
            )
        )


def wrap_text(text, max_width, char_width=6.5):
    """Simple text wrapping."""
    words = text.split()
    lines = []
    current = ""
    max_chars = int(max_width / char_width)
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = current + " " + word if current else word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines if lines else [text]


def add_shadow_filter(dwg):
    """No-op — shadow applied via double-stroke effect instead."""
    pass  # shadows removed for svgwrite compatibility


def draw_swim_lane(dwg, x, y, w, h, label, color="#eef2f7"):
    """Draw a BPMN swim lane with label on the left."""
    # Lane background
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(w, h),
            fill=color,
            stroke=ACCENT,
            stroke_width=0.5,
            opacity=0.5,
        )
    )
    # Label area (rotated text on left)
    label_w = 35
    dwg.add(
        dwg.rect(
            insert=(x, y), size=(label_w, h), fill=ACCENT, stroke="none", opacity=0.12
        )
    )
    dwg.add(
        dwg.line(
            start=(x + label_w, y),
            end=(x + label_w, y + h),
            stroke=ACCENT,
            stroke_width=0.5,
            opacity=0.4,
        )
    )

    # Rotated label
    text_elem = dwg.text(
        label,
        insert=(x + label_w / 2, y + h / 2),
        text_anchor="middle",
        font_size=LANE_LABEL_FONT_SIZE,
        font_family=FONT,
        fill=ACCENT,
        font_weight="bold",
        transform=f"rotate(-90, {x + label_w / 2}, {y + h / 2})",
    )
    dwg.add(text_elem)


def draw_pool_header(dwg, x, y, w, label):
    """Draw pool header bar."""
    h = 30
    dwg.add(dwg.rect(insert=(x, y), size=(w, h), fill=ACCENT, rx=4, ry=4))
    dwg.add(
        dwg.text(
            label,
            insert=(x + w / 2, y + 20),
            text_anchor="middle",
            font_size=14,
            font_family=FONT,
            fill=WHITE,
            font_weight="bold",
        )
    )


# ============================================================================
# DIAGRAM 1: Patient Admission & Form Completion
# ============================================================================


def generate_bpmn_1():
    W, H = 1300, 820
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/bpmn-admission.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )
    add_shadow_filter(dwg)

    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "BPMN Diagram 1: Patient Admission & Form Completion Process",
            insert=(W / 2, 28),
            text_anchor="middle",
            font_size=TITLE_FONT_SIZE,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(100, 38), end=(W - 100, 38), stroke=HIGHLIGHT, stroke_width=1.5)
    )

    # Pool
    pool_y = 50
    pool_h = H - 240
    draw_pool_header(dwg, 10, pool_y, W - 20, "CVD Clinic — Patient Admission Process")

    # Swim lanes
    lane_x = 10
    lane_w = W - 20
    lane_start = pool_y + 35
    lane_h1 = 220  # Patient
    lane_h2 = 200  # Nurse/Admin
    lane_h3 = 240  # Consultant (reduced for legend clearance)

    draw_swim_lane(dwg, lane_x, lane_start, lane_w, lane_h1, "Patient", LANE_COLORS[0])
    draw_swim_lane(
        dwg,
        lane_x,
        lane_start + lane_h1,
        lane_w,
        lane_h2,
        "Nurse / Admin",
        LANE_COLORS[1],
    )
    draw_swim_lane(
        dwg,
        lane_x,
        lane_start + lane_h1 + lane_h2,
        lane_w,
        lane_h3,
        "Consultant",
        LANE_COLORS[2],
    )

    # Content offset (after lane label)
    cx = lane_x + 50

    # ---- PATIENT LANE ----
    py = lane_start + lane_h1 / 2  # vertical center of patient lane

    # Start event
    draw_start_event(dwg, cx + 20, py, "Arrive at\nClinic")

    # Task: Login/Register
    t1x = cx + 70
    draw_task(dwg, t1x, py - 25, 120, 50, "Login / Register on Portal")
    draw_arrow(dwg, cx + 34, py, t1x, py)

    # Task: Fill Section 1
    t2x = t1x + 150
    draw_task(dwg, t2x, py - 25, 130, 50, "Fill Section 1 Form")
    draw_arrow(dwg, t1x + 120, py, t2x, py)

    # Gateway: Form complete?
    gw1x = t2x + 165
    draw_gateway(dwg, gw1x, py, "Form\ncomplete?", "exclusive")
    draw_arrow(dwg, t2x + 130, py, gw1x - 20, py)

    # No path - loop back
    no_y = py - 60
    draw_polyline_arrow(
        dwg,
        [(gw1x, py - 20), (gw1x, no_y), (t2x + 65, no_y), (t2x + 65, py - 25)],
        "No",
        HIGHLIGHT,
    )

    # Yes path -> Submit
    t3x = gw1x + 50
    draw_task(dwg, t3x, py - 25, 110, 50, "Submit Form")
    draw_arrow(dwg, gw1x + 20, py, t3x, py, "Yes")

    # Task: Wait for vitals
    t4x = t3x + 140
    draw_task(dwg, t4x, py - 25, 120, 50, "Wait for Vital Signs Check")
    draw_arrow(dwg, t3x + 110, py, t4x, py)

    # Task: Consultation
    t5x = t4x + 150
    draw_task(dwg, t5x, py - 25, 120, 50, "Attend Consultation")
    draw_arrow(dwg, t4x + 120, py, t5x, py)

    # Task: Receive prescription
    t6x = t5x + 150
    draw_task(dwg, t6x, py - 25, 120, 50, "Receive Prescription")
    draw_arrow(dwg, t5x + 120, py, t6x, py)

    # End event
    draw_end_event(dwg, t6x + 150, py, "Process\nComplete")
    draw_arrow(dwg, t6x + 120, py, t6x + 136, py)

    # ---- NURSE LANE ----
    ny = lane_start + lane_h1 + lane_h2 / 2

    # Task: Verify identity
    n1x = cx + 70
    draw_task(dwg, n1x, ny - 25, 130, 50, "Verify Patient Identity")

    # Parallel gateway: Check vitals
    pgw = n1x + 165
    draw_gateway(dwg, pgw, ny, "", "parallel")
    draw_arrow(dwg, n1x + 130, ny, pgw - 20, ny)

    # Task: Check BP (upper)
    n2x = pgw + 45
    n2y_up = ny - 45
    draw_task(dwg, n2x, n2y_up - 20, 120, 40, "Check Blood Pressure")
    draw_arrow(dwg, pgw + 20, ny, n2x, n2y_up)

    # Task: Check BMI (lower)
    n2y_dn = ny + 15
    draw_task(dwg, n2x, n2y_dn, 120, 40, "Check BMI & Sugar")
    draw_arrow(dwg, pgw + 20, ny, n2x, n2y_dn + 20)

    # Merge parallel gateway
    pgw2 = n2x + 155
    draw_gateway(dwg, pgw2, ny, "", "parallel")
    draw_arrow(dwg, n2x + 120, n2y_up, pgw2 - 20, ny)
    draw_arrow(dwg, n2x + 120, n2y_dn + 20, pgw2 - 20, ny)

    # Task: Record vitals
    n3x = pgw2 + 45
    draw_task(dwg, n3x, ny - 25, 130, 50, "Record Vital Signs in System", "service")
    draw_arrow(dwg, pgw2 + 20, ny, n3x, ny)

    # Task: Escort to consultant
    n4x = n3x + 165
    draw_task(dwg, n4x, ny - 25, 130, 50, "Escort to Consultant")
    draw_arrow(dwg, n3x + 130, ny, n4x, ny)

    # Cross-lane arrows (dashed)
    # Submit form triggers nurse verify
    draw_polyline_arrow(
        dwg, [(t3x + 55, py + 25), (t3x + 55, ny - 25)], "", ACCENT, dashed=True
    )
    # Escort triggers patient consultation
    draw_polyline_arrow(
        dwg, [(t4x + 60, py + 25), (t4x + 60, ny - 25)], "", ACCENT, dashed=True
    )

    # ---- CONSULTANT LANE ----
    cy_lane = lane_start + lane_h1 + lane_h2 + lane_h3 / 2

    # Task: Review Section 1
    c1x = cx + 70
    draw_task(dwg, c1x, cy_lane - 55, 130, 50, "Review Section 1 (Patient Data)")

    # Task: Conduct Examination
    c2x = c1x + 165
    draw_task(dwg, c2x, cy_lane - 55, 130, 50, "Conduct CVD Examination")
    draw_arrow(dwg, c1x + 130, cy_lane - 30, c2x, cy_lane - 30)

    # Task: Complete Section 2
    c3x = c2x + 165
    draw_task(dwg, c3x, cy_lane - 55, 130, 50, "Complete Section 2 (Notes)")
    draw_arrow(dwg, c2x + 130, cy_lane - 30, c3x, cy_lane - 30)

    # Gateway: Diagnosis type
    dgw = c3x + 165
    draw_gateway(dwg, dgw, cy_lane - 30, "Diagnosis\nType?", "exclusive")
    draw_arrow(dwg, c3x + 130, cy_lane - 30, dgw - 20, cy_lane - 30)

    # Three diagnosis paths converging
    diag_y1 = cy_lane - 85
    diag_y2 = cy_lane - 30
    diag_y3 = cy_lane + 25

    dx = dgw + 55
    draw_task(dwg, dx, diag_y1 - 17, 130, 34, "Hypertension Plan")
    draw_task(dwg, dx, diag_y2 - 17, 130, 34, "Hypotension Plan")
    draw_task(dwg, dx, diag_y3 - 17, 130, 34, "Diabetes Plan")

    draw_arrow(dwg, dgw, cy_lane - 50, dx, diag_y1)
    draw_arrow(dwg, dgw + 20, cy_lane - 30, dx, diag_y2)
    draw_arrow(dwg, dgw, cy_lane - 10, dx, diag_y3)

    # Merge gateway
    mgw = dx + 165
    draw_gateway(dwg, mgw, cy_lane - 30, "", "exclusive")
    draw_arrow(dwg, dx + 130, diag_y1, mgw - 20, cy_lane - 30)
    draw_arrow(dwg, dx + 130, diag_y2, mgw - 20, cy_lane - 30)
    draw_arrow(dwg, dx + 130, diag_y3, mgw - 20, cy_lane - 30)

    # Task: Generate Prescription
    c5x = mgw + 45
    draw_task(dwg, c5x, cy_lane - 55, 120, 50, "Generate Prescription", "service")
    draw_arrow(dwg, mgw + 20, cy_lane - 30, c5x, cy_lane - 30)

    # Task: Save Record
    c6x = c5x + 150
    draw_task(dwg, c6x, cy_lane - 55, 120, 50, "Save Medical Record", "service")
    draw_arrow(dwg, c5x + 120, cy_lane - 30, c6x, cy_lane - 30)

    # Cross-lane link from nurse escort to consultant review
    draw_polyline_arrow(
        dwg,
        [
            (n4x + 65, ny + 25),
            (n4x + 65, cy_lane - 80),
            (c1x + 65, cy_lane - 80),
            (c1x + 65, cy_lane - 55),
        ],
        "",
        ACCENT,
        dashed=True,
    )

    # Data objects at bottom right
    draw_data_object(dwg, c6x + 50, cy_lane + 40, 50, 55, "Medical\nRecord")
    draw_polyline_arrow(
        dwg,
        [(c6x + 60, cy_lane - 5), (c6x + 75, cy_lane + 40)],
        "",
        DATA_STROKE,
        dashed=True,
    )

    # Legend
    leg_x, leg_y = 50, 720
    dwg.add(
        dwg.rect(
            insert=(leg_x - 10, leg_y - 15),
            size=(W - 80, 50),
            fill=WHITE,
            stroke=MUTED,
            stroke_width=0.5,
            rx=6,
        )
    )
    dwg.add(
        dwg.text(
            "Legend:",
            insert=(leg_x, leg_y + 5),
            font_size=10,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )

    items = [
        (leg_x + 60, "Start Event", EVENT_START_STROKE, "circle"),
        (leg_x + 180, "End Event", EVENT_END_STROKE, "circle"),
        (leg_x + 290, "User Task", ACCENT, "rect"),
        (leg_x + 400, "Service Task", SERVICE_STROKE, "rect_s"),
        (leg_x + 530, "Exclusive Gateway", GATEWAY_STROKE, "diamond"),
        (leg_x + 700, "Parallel Gateway", GATEWAY_STROKE, "diamond_p"),
        (leg_x + 870, "Data Object", DATA_STROKE, "doc"),
        (leg_x + 990, "Message Flow", ACCENT, "dashed"),
    ]
    for ix, lbl, col, shape in items:
        if shape == "circle":
            dwg.add(
                dwg.circle(
                    center=(ix, leg_y + 2), r=8, fill="none", stroke=col, stroke_width=2
                )
            )
        elif shape == "rect":
            dwg.add(
                dwg.rect(
                    insert=(ix - 10, leg_y - 6),
                    size=(20, 16),
                    rx=3,
                    fill=WHITE,
                    stroke=col,
                    stroke_width=1.5,
                )
            )
        elif shape == "rect_s":
            dwg.add(
                dwg.rect(
                    insert=(ix - 10, leg_y - 6),
                    size=(20, 16),
                    rx=3,
                    fill=SERVICE_FILL,
                    stroke=col,
                    stroke_width=1.5,
                )
            )
        elif shape == "diamond":
            s = 8
            dwg.add(
                dwg.polygon(
                    [
                        (ix, leg_y - 6),
                        (ix + s, leg_y + 2),
                        (ix, leg_y + 10),
                        (ix - s, leg_y + 2),
                    ],
                    fill=GATEWAY_FILL,
                    stroke=col,
                    stroke_width=1.5,
                )
            )
        elif shape == "diamond_p":
            s = 8
            dwg.add(
                dwg.polygon(
                    [
                        (ix, leg_y - 6),
                        (ix + s, leg_y + 2),
                        (ix, leg_y + 10),
                        (ix - s, leg_y + 2),
                    ],
                    fill=GATEWAY_FILL,
                    stroke=col,
                    stroke_width=1.5,
                )
            )
            dwg.add(
                dwg.line(
                    start=(ix - 4, leg_y + 2),
                    end=(ix + 4, leg_y + 2),
                    stroke=col,
                    stroke_width=1.5,
                )
            )
            dwg.add(
                dwg.line(
                    start=(ix, leg_y - 2),
                    end=(ix, leg_y + 6),
                    stroke=col,
                    stroke_width=1.5,
                )
            )
        elif shape == "doc":
            dwg.add(
                dwg.rect(
                    insert=(ix - 8, leg_y - 5),
                    size=(16, 18),
                    fill=DATA_FILL,
                    stroke=col,
                    stroke_width=1,
                )
            )
        elif shape == "dashed":
            dwg.add(
                dwg.line(
                    start=(ix - 12, leg_y + 2),
                    end=(ix + 12, leg_y + 2),
                    stroke=col,
                    stroke_width=1.5,
                    stroke_dasharray="4,3",
                )
            )
        dwg.add(
            dwg.text(
                lbl,
                insert=(ix + 16, leg_y + 6),
                font_size=9,
                font_family=FONT,
                fill=MUTED,
            )
        )

    dwg.save()
    print("  -> bpmn-admission.svg created")


# ============================================================================
# DIAGRAM 2: Appointment Booking Process
# ============================================================================


def generate_bpmn_2():
    W, H = 1200, 520
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/bpmn-booking.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )
    add_shadow_filter(dwg)

    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "BPMN Diagram 2: Appointment Booking Process",
            insert=(W / 2, 28),
            text_anchor="middle",
            font_size=TITLE_FONT_SIZE,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(150, 38), end=(W - 150, 38), stroke=HIGHLIGHT, stroke_width=1.5)
    )

    # Pool
    pool_y = 50
    pool_h = H - 40
    draw_pool_header(dwg, 10, pool_y, W - 20, "CVD Clinic — Appointment Booking")

    lane_x = 10
    lane_w = W - 20
    lane_start = pool_y + 35
    lane_h1 = 190  # Patient
    lane_h2 = 190  # Admin

    draw_swim_lane(dwg, lane_x, lane_start, lane_w, lane_h1, "Patient", LANE_COLORS[0])
    draw_swim_lane(
        dwg,
        lane_x,
        lane_start + lane_h1,
        lane_w,
        lane_h2,
        "Admin Staff",
        LANE_COLORS[1],
    )

    cx = lane_x + 50

    # ---- PATIENT LANE ----
    py = lane_start + lane_h1 / 2

    draw_start_event(dwg, cx + 20, py, "")

    t1x = cx + 65
    draw_task(dwg, t1x, py - 25, 130, 50, "Request Appointment Online")
    draw_arrow(dwg, cx + 34, py, t1x, py)

    # Gateway: preferred date available?
    gw1x = t1x + 200
    draw_gateway(dwg, gw1x, py, "Preferred date\navailable?", "exclusive")
    # arrow drawn after admin check

    # No -> select alternative (positioned LEFT of gateway for clean counter-flow)
    alt_y = py - 60
    t_alt_x = gw1x - 180
    draw_task(dwg, t_alt_x, alt_y - 17, 130, 34, "Select Alternative Date")
    draw_arrow(dwg, gw1x - 20, py, t_alt_x + 130, alt_y + 17, "No")
    # Loop back: task left edge -> down-left -> up to gateway left side
    draw_polyline_arrow(
        dwg,
        [
            (t_alt_x, alt_y + 17),
            (t_alt_x - 25, alt_y + 17),
            (t_alt_x - 25, py + 20),
            (gw1x - 20, py + 20),
        ],
        "",
        )

# Yes -> Confirm
    t2x = gw1x + 80
    draw_task(dwg, t2x, py - 25, 120, 50, "Confirm Appointment")
    draw_arrow(dwg, gw1x + 20, py, t2x, py, "Yes")

    # Receive confirmation
    t3x = t2x + 155
    draw_task(dwg, t3x, py - 25, 130, 50, "Receive Confirmation")
    draw_arrow(dwg, t2x + 120, py, t3x, py)

    # Complete pre-visit forms
    t4x = t3x + 165
    draw_task(dwg, t4x, py - 25, 130, 50, "Complete Pre-Visit Forms")
    draw_arrow(dwg, t3x + 130, py, t4x, py)

    # End event
    draw_end_event(dwg, t4x + 165, py, "")
    draw_arrow(dwg, t4x + 130, py, t4x + 151, py)

    # ---- ADMIN LANE ----
    ay = lane_start + lane_h1 + lane_h2 / 2

    # Task: Check schedule
    a1x = cx + 65
    draw_task(dwg, a1x, ay - 25, 140, 50, "Check Consultant Schedule")

    # Cross-lane from patient request to admin check
    draw_polyline_arrow(
        dwg, [(t1x + 65, py + 25), (t1x + 65, ay - 25)], "", ACCENT, dashed=True
    )

    # Send availability response back
    draw_polyline_arrow(
        dwg, [(a1x + 140, ay), (gw1x, ay), (gw1x, py + 20)], "", ACCENT, dashed=True
    )

    # Task: Block slot
    a2x = gw1x + 80
    draw_task(dwg, a2x, ay - 25, 120, 50, "Block Appointment Slot")

    # Cross-lane from confirm to block
    draw_polyline_arrow(
        dwg, [(t2x + 60, py + 25), (t2x + 60, ay - 25)], "", ACCENT, dashed=True
    )

    # Task: Send confirmation
    a3x = a2x + 155
    draw_task(dwg, a3x, ay - 25, 130, 50, "Send Confirmation Email / SMS", "service")
    draw_arrow(dwg, a2x + 120, ay, a3x, ay)

    # Cross-lane from send to receive
    draw_polyline_arrow(
        dwg, [(a3x + 65, ay - 25), (a3x + 65, py + 25)], "", ACCENT, dashed=True
    )

    # Task: Send form link
    a4x = a3x + 165
    draw_task(dwg, a4x, ay - 25, 130, 50, "Send Pre-Visit Form Link", "service")
    draw_arrow(dwg, a3x + 130, ay, a4x, ay)

    # Cross-lane to patient forms
    draw_polyline_arrow(
        dwg, [(a4x + 65, ay - 25), (a4x + 65, py + 25)], "", ACCENT, dashed=True
    )

    # Data objects
    draw_data_object(dwg, a4x + 30, ay + 40, 45, 50, "Form Link")

    # Legend (compact)
    leg_x, leg_y = 80, 600
    dwg.add(
        dwg.rect(
            insert=(leg_x - 10, leg_y - 12),
            size=(W - 160, 35),
            fill=WHITE,
            stroke=MUTED,
            stroke_width=0.5,
            rx=4,
        )
    )
    legend_items = [
        "Start/End Events",
        "User Tasks",
        "Service Tasks",
        "Exclusive Gateway",
        "Message Flow (dashed)",
    ]
    for i, item in enumerate(legend_items):
        dwg.add(
            dwg.text(
                f"• {item}",
                insert=(leg_x + i * 200, leg_y + 8),
                font_size=9,
                font_family=FONT,
                fill=MUTED,
            )
        )

    dwg.save()
    print("  -> bpmn-booking.svg created")


# ============================================================================
# DIAGRAM 3: Form Processing & Data Flow
# ============================================================================


def generate_bpmn_3():
    W, H = 1200, 600
    dwg = svgwrite.Drawing(
        "/Users/hardjoshi/Desktop/Code/CN6001_group_coursework/images/bpmn-dataflow.svg",
        size=(f"{W}px", f"{H}px"),
        viewBox=f"0 0 {W} {H}",
    )
    add_shadow_filter(dwg)

    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=WHITE))

    # Title
    dwg.add(
        dwg.text(
            "BPMN Diagram 3: Form Processing & Data Flow",
            insert=(W / 2, 28),
            text_anchor="middle",
            font_size=TITLE_FONT_SIZE,
            font_family=FONT,
            fill=PRIMARY,
            font_weight="bold",
        )
    )
    dwg.add(
        dwg.line(start=(150, 38), end=(W - 150, 38), stroke=HIGHLIGHT, stroke_width=1.5)
    )

    # Pool
    pool_y = 50
    pool_h = H - 150
    draw_pool_header(
        dwg, 10, pool_y, W - 20, "CVD Clinic — Form Processing & Data Flow"
    )

    lane_x = 10
    lane_w = W - 20
    lane_start = pool_y + 35
    lane_h1 = 155  # Patient
    lane_h2 = 155  # Nurse
    lane_h3 = 250  # Consultant (extended for data flow clarity)

    draw_swim_lane(dwg, lane_x, lane_start, lane_w, lane_h1, "Patient", LANE_COLORS[0])
    draw_swim_lane(
        dwg, lane_x, lane_start + lane_h1, lane_w, lane_h2, "Nurse", LANE_COLORS[1]
    )
    draw_swim_lane(
        dwg,
        lane_x,
        lane_start + lane_h1 + lane_h2,
        lane_w,
        lane_h3,
        "Consultant",
        LANE_COLORS[2],
    )

    cx_off = lane_x + 50

    # ---- PATIENT LANE ----
    py = lane_start + lane_h1 / 2

    draw_start_event(dwg, cx_off + 20, py, "")

    # Fill Section 1
    t1x = cx_off + 65
    draw_task(dwg, t1x, py - 25, 140, 50, "Fill Section 1: Personal Info, Symptoms")
    draw_arrow(dwg, cx_off + 34, py, t1x, py)

    # Gateway: Validation
    gw1 = t1x + 175
    draw_gateway(dwg, gw1, py, "Valid?", "exclusive")
    draw_arrow(dwg, t1x + 140, py, gw1 - 20, py)

    # No -> Fix errors
    fix_y = py - 50
    draw_polyline_arrow(
        dwg,
        [(gw1, py - 20), (gw1, fix_y), (t1x + 70, fix_y), (t1x + 70, py - 25)],
        "No",
        HIGHLIGHT,
    )

    # Yes -> Submit
    t2x = gw1 + 55
    draw_task(dwg, t2x, py - 25, 120, 50, "Submit Section 1", "service")
    draw_arrow(dwg, gw1 + 20, py, t2x, py, "Yes")

    # Data object: Section 1
    d1x = t2x + 140
    draw_data_object(dwg, d1x, py - 30, 55, 60, "Section 1\nData")
    draw_arrow(dwg, t2x + 120, py, d1x, py, "", dashed=True, color=DATA_STROKE)

    # Receive full record at end
    t_recv = d1x + 280
    draw_task(dwg, t_recv, py - 25, 140, 50, "Receive Complete Medical Record")

    draw_end_event(dwg, t_recv + 175, py, "")
    draw_arrow(dwg, t_recv + 140, py, t_recv + 161, py)

    # ---- NURSE LANE ----
    ny = lane_start + lane_h1 + lane_h2 / 2

    # Record Vitals
    n1x = cx_off + 65
    draw_task(dwg, n1x, ny - 25, 140, 50, "Record Vital Signs (BP, BMI, Sugar)")

    # Cross-lane from Section 1 submit
    draw_polyline_arrow(
        dwg,
        [
            (t2x + 60, py + 25),
            (t2x + 60, ny - 45),
            (n1x + 70, ny - 45),
            (n1x + 70, ny - 25),
        ],
        "",
        ACCENT,
        dashed=True,
    )

    # Service: Store vitals
    n2x = n1x + 175
    draw_task(dwg, n2x, ny - 25, 130, 50, "Store Vitals in System", "service")
    draw_arrow(dwg, n1x + 140, ny, n2x, ny)

    # Data object: Vital Signs
    d2x = n2x + 155
    draw_data_object(dwg, d2x, ny - 30, 55, 60, "Vital Signs\nData")
    draw_arrow(dwg, n2x + 130, ny, d2x, ny, "", dashed=True, color=DATA_STROKE)

    # ---- CONSULTANT LANE ----
    cy_l = lane_start + lane_h1 + lane_h2 + lane_h3 / 2

    # Review combined data
    c1x = cx_off + 65
    draw_task(dwg, c1x, cy_l - 30, 150, 55, "Review Section 1 + Vital Signs Data")

    # Data flows into consultant
    draw_polyline_arrow(
        dwg,
        [
            (d1x + 27, py + 30),
            (d1x + 27, cy_l - 60),
            (c1x + 75, cy_l - 60),
            (c1x + 75, cy_l - 30),
        ],
        "",
        DATA_STROKE,
        dashed=True,
    )
    draw_polyline_arrow(
        dwg,
        [
            (d2x + 27, ny + 30),
            (d2x + 27, cy_l - 70),
            (c1x + 100, cy_l - 70),
            (c1x + 100, cy_l - 30),
        ],
        "",
        DATA_STROKE,
        dashed=True,
    )

    # Conduct examination
    c2x = c1x + 185
    draw_task(dwg, c2x, cy_l - 25, 130, 50, "Conduct Examination")
    draw_arrow(dwg, c1x + 150, cy_l, c2x, cy_l)

    # Complete Section 2
    c3x = c2x + 165
    draw_task(dwg, c3x, cy_l - 25, 140, 50, "Complete Section 2: Diagnosis & Notes")
    draw_arrow(dwg, c2x + 130, cy_l, c3x, cy_l)

    # Data object: Section 2
    d3x = c3x + 165
    draw_data_object(dwg, d3x, cy_l - 30, 55, 60, "Section 2\nData")
    draw_arrow(dwg, c3x + 140, cy_l, d3x, cy_l, "", dashed=True, color=DATA_STROKE)

    # Merge Service: Compile Record
    c4x = d3x + 95
    draw_task(
        dwg, c4x, cy_l - 25, 140, 50, "Compile Complete Medical Record", "service"
    )
    draw_arrow(dwg, d3x + 55, cy_l, c4x, cy_l)

    # Data flows into compile
    draw_polyline_arrow(
        dwg,
        [
            (d1x + 55, py + 30),
            (d1x + 80, py + 50),
            (d1x + 80, cy_l + 60),
            (c4x + 70, cy_l + 60),
            (c4x + 70, cy_l + 25),
        ],
        "Section 1",
        DATA_STROKE,
        dashed=True,
    )
    draw_polyline_arrow(
        dwg,
        [
            (d2x + 55, ny + 30),
            (d2x + 80, ny + 50),
            (d2x + 80, cy_l + 70),
            (c4x + 100, cy_l + 70),
            (c4x + 100, cy_l + 25),
        ],
        "Vitals",
        DATA_STROKE,
        dashed=True,
    )

    # Generate Prescription
    c5x = c4x + 175
    draw_task(dwg, c5x, cy_l - 25, 130, 50, "Generate Prescription", "service")
    draw_arrow(dwg, c4x + 140, cy_l, c5x, cy_l)

    # Data object: Complete Record
    d4x = c4x + 40
    d4y = cy_l + 280  # Below all lanes to avoid overlap
    draw_data_object(dwg, d4x, d4y, 60, 50, "Complete\nMedical Record")
    draw_arrow(
        dwg, c4x + 70, cy_l - 25, d4x + 30, d4y + 50, "", dashed=True, color=DATA_STROKE
    )

    # Send record to patient
    draw_polyline_arrow(
        dwg,
        [
            (c5x + 65, cy_l - 25),
            (c5x + 65, py + 60),
            (t_recv + 70, py + 60),
            (t_recv + 70, py + 25),
        ],
        "",
        ACCENT,
        dashed=True,
    )

    # Data: Prescription
    d5x = c5x + 20
    d5y = cy_l + 40
    draw_data_object(dwg, d5x, d5y, 50, 50, "Prescription")
    draw_polyline_arrow(
        dwg, [(c5x + 65, cy_l + 25), (d5x + 25, d5y)], "", DATA_STROKE, dashed=True
    )

    dwg.save()
    print("  -> bpmn-dataflow.svg created")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("Generating BPMN diagrams...")
    generate_bpmn_1()
    generate_bpmn_2()
    generate_bpmn_3()
    print("Done! All 3 BPMN SVGs created in images/")
