import os
import sys
import datetime
from tkinter import messagebox

# Path to the Firebase Service Account private key JSON
CRED_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firebase_credentials.json")

_db_client = None
_use_mock_db = False

# Local mock database for offline demo mode
_mock_db = {
    "colleges": {
        "GEC": {
            "college_id": "GEC",
            "college_name": "GEC",
            "password": "123",
            "principal": "Dr. Smith",
            "director": "Mr. Jones",
            "status": "Accepted"
        },
        "OCAC": {
            "college_id": "OCAC",
            "college_name": "OCAC",
            "password": "123",
            "principal": "Dr. Raut",
            "director": "Mr. Asit",
            "status": "Accepted"
        }
    },
    "counselors": {},
    "students": {},
    "payments": [],
    "student_feedback": [],
    "counselor_feedback": []
}

def get_db():
    """Initializes and returns the Firestore client instance. If invalid/missing, prompts for Offline Demo Mode."""
    global _db_client, _use_mock_db
    if _db_client is not None:
        return _db_client
    if _use_mock_db:
        return None

    # Check if credentials file exists and is not the placeholder
    file_exists = os.path.exists(CRED_PATH)
    is_placeholder = False
    if file_exists:
        try:
            with open(CRED_PATH, 'r') as f:
                content = f.read()
                if "REPLACE THE ENTIRE CONTENT" in content:
                    is_placeholder = True
        except Exception:
            pass

    if not file_exists or is_placeholder:
        return _init_mock_db_with_dialog(
            "Firebase Credentials Missing",
            "The Firebase Service Account JSON credentials file is missing or invalid.\n\n"
            "Would you like to run the application in Offline Demo Mode?\n"
            "(All features, forms, registrations, and downloads will work, but data won't be persistent.)"
        )

    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
        
        if not firebase_admin._apps:
            cred = credentials.Certificate(CRED_PATH)
            firebase_admin.initialize_app(cred)
            
        _db_client = firestore.client()
        return _db_client
    except ImportError:
        messagebox.showerror(
            "Dependencies Missing",
            "The 'firebase-admin' Python package is not installed.\n"
            "Please run: pip install firebase-admin"
        )
        sys.exit(1)
    except Exception as e:
        return _init_mock_db_with_dialog(
            "Firebase Connection Error",
            f"Could not connect to Firebase:\n{e}\n\n"
            "Would you like to run the application in Offline Demo Mode?\n"
            "(All features, forms, registrations, and downloads will work, but data won't be persistent.)"
        )

def _init_mock_db_with_dialog(title, message):
    global _use_mock_db
    ans = messagebox.askyesno(title, message)
    if ans:
        _use_mock_db = True
        return None
    else:
        sys.exit(1)


# Helper Functions for colleges collection
def add_college(college_id, data):
    db = get_db()
    data["status"] = data.get("status", "Pending")
    if _use_mock_db:
        _mock_db["colleges"][str(college_id)] = data.copy()
    else:
        db.collection("colleges").document(str(college_id)).set(data)

def get_college(college_id):
    db = get_db()
    if _use_mock_db:
        return _mock_db["colleges"].get(str(college_id))
    else:
        doc = db.collection("colleges").document(str(college_id)).get()
        return doc.to_dict() if doc.exists else None

def get_college_by_name(college_name):
    db = get_db()
    if _use_mock_db:
        for c in _mock_db["colleges"].values():
            if c.get("college_name") == college_name:
                return c
        return None
    else:
        docs = db.collection("colleges").where("college_name", "==", college_name).stream()
        for doc in docs:
            return doc.to_dict()
        return None

def get_all_colleges():
    db = get_db()
    if _use_mock_db:
        return list(_mock_db["colleges"].values())
    else:
        docs = db.collection("colleges").stream()
        return [doc.to_dict() for doc in docs]

def get_pending_colleges():
    db = get_db()
    if _use_mock_db:
        return [c for c in _mock_db["colleges"].values() if c.get("status") == "Pending"]
    else:
        docs = db.collection("colleges").where("status", "==", "Pending").stream()
        return [doc.to_dict() for doc in docs]

def get_approved_colleges():
    db = get_db()
    if _use_mock_db:
        return [c for c in _mock_db["colleges"].values() if c.get("status") == "Accepted"]
    else:
        docs = db.collection("colleges").where("status", "==", "Accepted").stream()
        return [doc.to_dict() for doc in docs]

def approve_college(college_id):
    db = get_db()
    if _use_mock_db:
        if str(college_id) in _mock_db["colleges"]:
            _mock_db["colleges"][str(college_id)]["status"] = "Accepted"
    else:
        db.collection("colleges").document(str(college_id)).update({"status": "Accepted"})

def delete_college(college_id):
    db = get_db()
    if _use_mock_db:
        _mock_db["colleges"].pop(str(college_id), None)
    else:
        db.collection("colleges").document(str(college_id)).delete()

def update_college_password(college_id, new_password):
    db = get_db()
    if _use_mock_db:
        if str(college_id) in _mock_db["colleges"]:
            _mock_db["colleges"][str(college_id)]["password"] = new_password
    else:
        db.collection("colleges").document(str(college_id)).update({"password": new_password})


# Helper Functions for counselors collection
def add_counselor(counselor_id, data):
    db = get_db()
    data["status"] = data.get("status", "Pending")
    if _use_mock_db:
        _mock_db["counselors"][str(counselor_id)] = data.copy()
    else:
        db.collection("counselors").document(str(counselor_id)).set(data)

def get_counselor(counselor_id):
    db = get_db()
    if _use_mock_db:
        return _mock_db["counselors"].get(str(counselor_id))
    else:
        doc = db.collection("counselors").document(str(counselor_id)).get()
        return doc.to_dict() if doc.exists else None

def get_counselor_by_username(username):
    db = get_db()
    if _use_mock_db:
        for c in _mock_db["counselors"].values():
            if c.get("username") == username:
                return c
        return None
    else:
        docs = db.collection("counselors").where("username", "==", username).stream()
        for doc in docs:
            return doc.to_dict()
        return None

def get_counselors_by_college(college_name, status=None):
    db = get_db()
    if _use_mock_db:
        res = []
        for c in _mock_db["counselors"].values():
            if c.get("college_name") == college_name:
                if status is None or c.get("status") == status:
                    res.append(c)
        return res
    else:
        query = db.collection("counselors").where("college_name", "==", college_name)
        if status is not None:
            query = query.where("status", "==", status)
        docs = query.stream()
        return [doc.to_dict() for doc in docs]

def approve_counselor(counselor_id):
    db = get_db()
    if _use_mock_db:
        if str(counselor_id) in _mock_db["counselors"]:
            _mock_db["counselors"][str(counselor_id)]["status"] = "Accepted"
    else:
        db.collection("counselors").document(str(counselor_id)).update({"status": "Accepted"})

def delete_counselor(counselor_id):
    db = get_db()
    if _use_mock_db:
        _mock_db["counselors"].pop(str(counselor_id), None)
    else:
        db.collection("counselors").document(str(counselor_id)).delete()

def update_counselor_password(counselor_id, new_password):
    db = get_db()
    if _use_mock_db:
        if str(counselor_id) in _mock_db["counselors"]:
            _mock_db["counselors"][str(counselor_id)]["password"] = new_password
    else:
        db.collection("counselors").document(str(counselor_id)).update({"password": new_password})


# Helper Functions for students collection
def add_student(student_id, data):
    db = get_db()
    data["status"] = data.get("status", "Pending")
    data["total_fee"] = int(data.get("total_fee", 100000))
    data["paid_amount"] = int(data.get("paid_amount", 0))
    data["pending_amount"] = int(data.get("pending_amount", 100000))
    if _use_mock_db:
        _mock_db["students"][str(student_id)] = data.copy()
    else:
        db.collection("students").document(str(student_id)).set(data)

def get_student(student_id):
    db = get_db()
    if _use_mock_db:
        return _mock_db["students"].get(str(student_id))
    else:
        doc = db.collection("students").document(str(student_id)).get()
        return doc.to_dict() if doc.exists else None

def get_student_by_username(username):
    db = get_db()
    if _use_mock_db:
        for s in _mock_db["students"].values():
            if s.get("username") == username:
                return s
        return None
    else:
        docs = db.collection("students").where("username", "==", username).stream()
        for doc in docs:
            return doc.to_dict()
        return None

def get_students_by_college(college_name, status=None, paid_status=None):
    db = get_db()
    if _use_mock_db:
        res = []
        for s in _mock_db["students"].values():
            if s.get("college_name") == college_name:
                if status is None or s.get("status") == status:
                    pending = int(s.get("pending_amount", 0))
                    if paid_status == "Fully Paid" and pending > 0:
                        continue
                    if paid_status == "Pending" and pending <= 0:
                        continue
                    res.append(s)
        return res
    else:
        query = db.collection("students").where("college_name", "==", college_name)
        if status is not None:
            query = query.where("status", "==", status)
        
        docs = query.stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            pending = int(data.get("pending_amount", 0))
            if paid_status == "Fully Paid" and pending > 0:
                continue
            if paid_status == "Pending" and pending <= 0:
                continue
            results.append(data)
        return results

def update_student(student_id, data):
    db = get_db()
    if _use_mock_db:
        if str(student_id) in _mock_db["students"]:
            for k, v in data.items():
                if k in ["total_fee", "paid_amount", "pending_amount"]:
                    _mock_db["students"][str(student_id)][k] = int(v)
                else:
                    _mock_db["students"][str(student_id)][k] = v
    else:
        if "total_fee" in data:
            data["total_fee"] = int(data["total_fee"])
        if "paid_amount" in data:
            data["paid_amount"] = int(data["paid_amount"])
        if "pending_amount" in data:
            data["pending_amount"] = int(data["pending_amount"])
        db.collection("students").document(str(student_id)).update(data)

def approve_student(student_id):
    db = get_db()
    if _use_mock_db:
        if str(student_id) in _mock_db["students"]:
            _mock_db["students"][str(student_id)]["status"] = "Accepted"
    else:
        db.collection("students").document(str(student_id)).update({"status": "Accepted"})

def delete_student(student_id):
    db = get_db()
    if _use_mock_db:
        _mock_db["students"].pop(str(student_id), None)
    else:
        db.collection("students").document(str(student_id)).delete()

def update_student_password(student_id, new_password):
    db = get_db()
    if _use_mock_db:
        if str(student_id) in _mock_db["students"]:
            _mock_db["students"][str(student_id)]["password"] = new_password
    else:
        db.collection("students").document(str(student_id)).update({"password": new_password})


# Helper Functions for payments collection
def add_payment(data):
    db = get_db()
    data["amount"] = int(data["amount"])
    if "payment_date" not in data:
        data["payment_date"] = datetime.datetime.now().isoformat()
        
    if _use_mock_db:
        import uuid
        doc_id = str(uuid.uuid4())
        data["payment_id"] = doc_id
        _mock_db["payments"].append(data.copy())
        
        student_id = data["student_id"]
        stud = get_student(student_id)
        if stud:
            new_paid = int(stud.get("paid_amount", 0)) + data["amount"]
            new_pending = int(stud.get("total_fee", 100000)) - new_paid
            update_student(student_id, {
                "paid_amount": new_paid,
                "pending_amount": new_pending
            })
        return doc_id
    else:
        doc_ref = db.collection("payments").document()
        doc_id = doc_ref.id
        data["payment_id"] = doc_id
        doc_ref.set(data)
        
        student_id = data["student_id"]
        stud = get_student(student_id)
        if stud:
            new_paid = int(stud.get("paid_amount", 0)) + data["amount"]
            new_pending = int(stud.get("total_fee", 100000)) - new_paid
            update_student(student_id, {
                "paid_amount": new_paid,
                "pending_amount": new_pending
            })
        return doc_id

def get_payments(student_id):
    db = get_db()
    if _use_mock_db:
        res = [p for p in _mock_db["payments"] if p.get("student_id") == str(student_id)]
        res.sort(key=lambda x: x.get("payment_date", ""), reverse=True)
        return res
    else:
        docs = db.collection("payments").where("student_id", "==", str(student_id)).stream()
        payments = [doc.to_dict() for doc in docs]
        payments.sort(key=lambda x: x.get("payment_date", ""), reverse=True)
        return payments

def get_payments_by_college(college_name, date_range=None, mode=None):
    db = get_db()
    if _use_mock_db:
        res = []
        now = datetime.datetime.now()
        if date_range == "1day":
            cutoff = now - datetime.timedelta(days=1)
        elif date_range == "7days":
            cutoff = now - datetime.timedelta(days=7)
        elif date_range == "30days":
            cutoff = now - datetime.timedelta(days=30)
        elif date_range == "1year":
            cutoff = now - datetime.timedelta(days=365)
        else:
            cutoff = None

        for p in _mock_db["payments"]:
            if mode is not None and mode != "Total" and p.get("mode") != mode:
                continue
            stud_id = p.get("student_id")
            stud = get_student(stud_id)
            if not stud or stud.get("college_name") != college_name:
                continue
            
            p_date_str = p.get("payment_date")
            if p_date_str and cutoff:
                try:
                    p_date = datetime.datetime.fromisoformat(p_date_str)
                    if p_date < cutoff:
                        continue
                except Exception:
                    pass
            res.append(p)
        return res
    else:
        query = db.collection("payments")
        if mode is not None and mode != "Total":
            query = query.where("mode", "==", mode)
            
        docs = query.stream()
        results = []
        now = datetime.datetime.now()
        if date_range == "1day":
            cutoff = now - datetime.timedelta(days=1)
        elif date_range == "7days":
            cutoff = now - datetime.timedelta(days=7)
        elif date_range == "30days":
            cutoff = now - datetime.timedelta(days=30)
        elif date_range == "1year":
            cutoff = now - datetime.timedelta(days=365)
        else:
            cutoff = None
            
        for doc in docs:
            data = doc.to_dict()
            stud_id = data.get("student_id")
            stud = get_student(stud_id)
            if not stud or stud.get("college_name") != college_name:
                continue
                
            p_date_str = data.get("payment_date")
            if p_date_str and cutoff:
                try:
                    p_date = datetime.datetime.fromisoformat(p_date_str)
                    if p_date < cutoff:
                        continue
                except Exception:
                    pass
                    
            results.append(data)
        return results


# Helper Functions for feedbacks
def add_student_feedback(data):
    db = get_db()
    if "created_at" not in data:
        data["created_at"] = datetime.datetime.now().isoformat()
    if _use_mock_db:
        import uuid
        data["feedback_id"] = str(uuid.uuid4())
        _mock_db["student_feedback"].append(data.copy())
    else:
        doc_ref = db.collection("student_feedback").document()
        data["feedback_id"] = doc_ref.id
        doc_ref.set(data)

def get_student_feedbacks(college_name):
    db = get_db()
    if _use_mock_db:
        res = []
        for fb in _mock_db["student_feedback"]:
            stud = get_student(fb.get("student_id"))
            if stud and stud.get("college_name") == college_name:
                res.append(fb)
        res.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return res
    else:
        docs = db.collection("student_feedback").stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            data["feedback_id"] = doc.id
            stud = get_student(data.get("student_id"))
            if stud and stud.get("college_name") == college_name:
                results.append(data)
        results.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return results

def delete_student_feedback(fb_id):
    db = get_db()
    if _use_mock_db:
        global _mock_db
        _mock_db["student_feedback"] = [f for f in _mock_db["student_feedback"] if f.get("feedback_id") != fb_id]
    else:
        db.collection("student_feedback").document(fb_id).delete()

def add_counselor_feedback(data):
    db = get_db()
    if "created_at" not in data:
        data["created_at"] = datetime.datetime.now().isoformat()
    if _use_mock_db:
        import uuid
        data["feedback_id"] = str(uuid.uuid4())
        _mock_db["counselor_feedback"].append(data.copy())
    else:
        doc_ref = db.collection("counselor_feedback").document()
        data["feedback_id"] = doc_ref.id
        doc_ref.set(data)

def get_counselor_feedbacks(college_name):
    db = get_db()
    if _use_mock_db:
        res = []
        for fb in _mock_db["counselor_feedback"]:
            coun = get_counselor(fb.get("counselor_id"))
            if coun and coun.get("college_name") == college_name:
                res.append(fb)
        res.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return res
    else:
        docs = db.collection("counselor_feedback").stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            data["feedback_id"] = doc.id
            coun = get_counselor(data.get("counselor_id"))
            if coun and coun.get("college_name") == college_name:
                results.append(data)
        results.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return results

def delete_counselor_feedback(fb_id):
    db = get_db()
    if _use_mock_db:
        global _mock_db
        _mock_db["counselor_feedback"] = [f for f in _mock_db["counselor_feedback"] if f.get("feedback_id") != fb_id]
    else:
        db.collection("counselor_feedback").document(fb_id).delete()
