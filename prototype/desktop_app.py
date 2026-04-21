import customtkinter as ctk
import requests
import json
from datetime import datetime

# Configure Appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

API_BASE_URL = "http://127.0.0.1:5000/api"

class CVDDesktopApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CVD Clinic - Staff Terminal (AOA)")
        self.geometry("900x600")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="CVD Clinic\nAdmin/Consultant", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_refresh = ctk.CTkButton(self.sidebar_frame, text="Refresh Appointments", command=self.load_appointments)
        self.btn_refresh.grid(row=1, column=0, padx=20, pady=10)

        # Main Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Appointments Display
        self.label_appts = ctk.CTkLabel(self.main_frame, text="Scheduled Appointments", font=ctk.CTkFont(size=18, weight="bold"))
        self.label_appts.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")

        self.textbox_appts = ctk.CTkTextbox(self.main_frame, height=200)
        self.textbox_appts.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Action Area
        self.action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        self.action_frame.grid_columnconfigure((0, 1), weight=1)

        # Record Vitals (Nurse)
        self.vitals_frame = ctk.CTkFrame(self.action_frame)
        self.vitals_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        ctk.CTkLabel(self.vitals_frame, text="Record Vitals (Nurse)").pack(pady=10)
        self.entry_v_appt = ctk.CTkEntry(self.vitals_frame, placeholder_text="Appointment ID")
        self.entry_v_appt.pack(pady=5, padx=20, fill="x")
        self.entry_v_sys = ctk.CTkEntry(self.vitals_frame, placeholder_text="BP Systolic (e.g. 120)")
        self.entry_v_sys.pack(pady=5, padx=20, fill="x")
        self.entry_v_dia = ctk.CTkEntry(self.vitals_frame, placeholder_text="BP Diastolic (e.g. 80)")
        self.entry_v_dia.pack(pady=5, padx=20, fill="x")
        
        self.btn_submit_vitals = ctk.CTkButton(self.vitals_frame, text="Submit Vitals", command=self.dummy_submit)
        self.btn_submit_vitals.pack(pady=15)

        # Complete Form Section 2 (Consultant)
        self.sec2_frame = ctk.CTkFrame(self.action_frame)
        self.sec2_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        ctk.CTkLabel(self.sec2_frame, text="Complete Section Two (Consultant)").pack(pady=10)
        self.entry_s2_form = ctk.CTkEntry(self.sec2_frame, placeholder_text="Form ID")
        self.entry_s2_form.pack(pady=5, padx=20, fill="x")
        self.entry_s2_diag = ctk.CTkEntry(self.sec2_frame, placeholder_text="Diagnosis")
        self.entry_s2_diag.pack(pady=5, padx=20, fill="x")
        self.entry_s2_notes = ctk.CTkEntry(self.sec2_frame, placeholder_text="Clinical Notes")
        self.entry_s2_notes.pack(pady=5, padx=20, fill="x")
        
        self.btn_submit_sec2 = ctk.CTkButton(self.sec2_frame, text="Finalize Consultation", command=self.dummy_submit)
        self.btn_submit_sec2.pack(pady=15)

        # Load initial data
        self.load_appointments()

    def load_appointments(self):
        self.textbox_appts.delete("0.0", "end")
        try:
            response = requests.get(f"{API_BASE_URL}/appointments")
            if response.status_code == 200:
                appts = response.json()
                if not appts:
                    self.textbox_appts.insert("0.0", "No appointments found.")
                    return
                for a in appts:
                    text = f"ID: {a['appointmentID']} | Patient: {a['patientID']} | Date: {a['date']} | Status: {a['status']}\n"
                    self.textbox_appts.insert("end", text)
            else:
                self.textbox_appts.insert("0.0", "Failed to load from server.")
        except requests.exceptions.ConnectionError:
            self.textbox_appts.insert("0.0", "Error: Backend Server (Flask) is not running on port 5000.")

    def dummy_submit(self):
        # In a full implementation, this would POST to the Flask API
        dialog = ctk.CTkToplevel(self)
        dialog.title("Success")
        dialog.geometry("300x150")
        ctk.CTkLabel(dialog, text="Action submitted to Database via API!").pack(pady=40)
        ctk.CTkButton(dialog, text="OK", command=dialog.destroy).pack()

if __name__ == "__main__":
    app = CVDDesktopApp()
    app.mainloop()
