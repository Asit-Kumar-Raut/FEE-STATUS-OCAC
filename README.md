# College Fee Status Management Portal 🎓💻

### 🔗 Live Web Portal: [https://college-fee-status.vercel.app/](https://college-fee-status.vercel.app/)

Welcome to the **College Fee Status Management Portal**! This is a secure, cloud-connected desktop application designed to streamline student fee management, counselor review workflows, college registration approvals, and administrative finance audits.

The application features a modern desktop user interface that communicates directly with a cloud database, enabling real-time validation and branded PDF receipt generation.

---

## 🌟 Key Features

*   **Secure Cloud Database Integration**: Integrated with Google Firebase Firestore for real-time data persistence and sync.
*   **Multi-Role Access Control**: 
    *   **Super Admin**: Credentials audit, approvals of colleges/counselors, and fee structures control.
    *   **College Portal**: Register college accounts, manage fee structures, and approve counselors.
    *   **Counselors**: Manage student records, verify payment status, and process feedback.
    *   **Students**: View payment schedules, submit feedback, and download receipts.
*   **Automated PDF Receipts**: High-quality transaction receipt generator compiled using ReportLab.
*   **Offline Demo Mode**: Graceful fall-back that allows all modules and features to run locally in-memory if Firebase connection credentials are missing.
*   **Secure Packaging**: Excludes large scientific packages (like PyTorch and TensorFlow) to compile into a compact standalone executable (`.exe`) in under 60 seconds.
*   **Setup Installer Wizard**: Packaged with Inno Setup to create a professional `FeeManagerSetup.exe` wizard that installs files and places a shortcut icon on the user's desktop.

---

## 🛠️ Technology Stack

*   **Frontend GUI**: Python Tkinter (custom responsive styling & window positioning)
*   **Backend Cloud**: Google Firebase Firestore (Python `firebase-admin` SDK)
*   **PDF Compiler**: ReportLab Canvas API
*   **App Compilation**: PyInstaller
*   **Setup Compiler**: Inno Setup 6

---


## 👥 Development Team

*   **Asit Kumar Raut** (Team Leader)
*   **Bishwa Prakash Rout**
*   **Akash Kumar Swain**
*   **Aditya Kumar Sahoo**

### 🎓 Guided by Mentor:
*   **Benumadhaba Ratha**


This project was developed for **OCAC** training purposes. All rights reserved.
