from tkinter import *
from tkinter import messagebox
import db

def main(name, student_id):
    root = Tk()
    root.title("Student Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    student_details = db.get_student(student_id)
    if not student_details:
        messagebox.showerror("Error", "Student details not found!")
        root.destroy()
        return

    s_id = student_details.get("student_id", "")
    s_name = student_details.get("name", "")
    username = student_details.get("username", "")
    phone = student_details.get("phonenumber", "")
    email = student_details.get("emailid", "")
    course = student_details.get("course", "")
    year = student_details.get("academic_year", "")
    sem = student_details.get("semester", "")
    total_fee = student_details.get("total_fee", 100000)
    paid_amount = student_details.get("paid_amount", 0)
    pending_amount = student_details.get("pending_amount", 100000)

    # Query online/offline payments
    payments = db.get_payments(student_id)
    online_paid = sum(p.get("amount", 0) for p in payments if p.get("mode") == "Online")
    offline_paid = sum(p.get("amount", 0) for p in payments if p.get("mode") == "Offline")

    def logout_action():
        root.destroy()
        from student import student_login
        student_login.main()

    def change_password():
        root.destroy()
        from student import student_pasword_update
        student_pasword_update.main(name, student_id)

    def feedback_action():
        root.destroy()
        from student import student_feed_back
        student_feed_back.main(name, student_id)

    def view_receipts():
        root.destroy()
        from student import receipt
        receipt.main(student_id, role="student", caller_name=name)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_student = Label(header_frame, text=f"🎓 STUDENT PROFILE: {name} (ID: {student_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_student.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    title_label = Label(root, text="STUDENT FEE DASHBOARD", fg="#1e293b", bg=bg_color, font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    # LEFT DIVISION: Student Profile Details
    lbl_title = Label(root, text="REGISTRATION DETAILS", font=("Segoe UI", 16, "bold"), fg="#3b82f6", bg=bg_color)
    lbl_title.place(x=150, y=180)

    details = [ 
        ("Student ID:", s_id), 
        ("Full Name:", s_name),
        ("Username:", username),
        ("Phone Number:", phone),
        ("Email ID:", email),
        ("Course:", course),
        ("Academic Year:", year), 
        ("Semester:", sem)
    ]

    y_pos = 230
    for label, val in details:
        Label(root, text=label, font=("Segoe UI", 11, "bold"), fg="#475569", bg=bg_color, width=15, anchor=W).place(x=150, y=y_pos)
        Label(root, text=val, font=("Segoe UI", 11), fg="#1e293b", bg=bg_color, anchor=W).place(x=300, y=y_pos)
        y_pos += 35

    # FEEDBACK BUTTON
    btn_feedback = Button(root, text="📝 GIVE FEEDBACK / REPORT ISSUE", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=feedback_action)
    btn_feedback.place(x=150, y=530, width=320, height=45)
    btn_feedback.bind("<Enter>", lambda e: btn_feedback.config(bg="#7c3aed"))
    btn_feedback.bind("<Leave>", lambda e: btn_feedback.config(bg="#8b5cf6"))

    btn_receipts = Button(root, text="🧾 VIEW PAYMENT RECEIPTS", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=view_receipts)
    btn_receipts.place(x=750, y=530, width=320, height=45)
    btn_receipts.bind("<Enter>", lambda e: btn_receipts.config(bg="#0f766e"))
    btn_receipts.bind("<Leave>", lambda e: btn_receipts.config(bg="#0d9488"))

    # password update page
    btn_reset = Button(root, text="🔄 Reset Password", fg="white", bg="#7c3aed", activebackground="#6d28d9", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=change_password)
    btn_reset.place(x=30, y=690, width=140, height=40)
    btn_reset.bind("<Enter>", lambda e: btn_reset.config(bg="#6d28d9"))
    btn_reset.bind("<Leave>", lambda e: btn_reset.config(bg="#7c3aed"))

    # RIGHT DIVISION: Fee Status
    lbl_fee_title = Label(root, text="FEE STATUS SUMMARY", font=("Segoe UI", 16, "bold"), fg="#0d9488", bg=bg_color)
    lbl_fee_title.place(x=750, y=180)

    fee_items = [
        ("Total Academic Fee", f"₹ {total_fee:,}", "#1e293b", None),
        ("Total Amount Paid", f"₹ {paid_amount:,}", "#10b981", f"(Online: ₹ {online_paid:,} | Offline: ₹ {offline_paid:,})"),
        ("Total Pending Amount", f"₹ {pending_amount:,}", "#ef4444", None)
    ]

    y_pos_fee = 230
    for title, val, color, sub_text in fee_items:
        Label(root, text=title, font=("Segoe UI", 11, "bold"), fg="#64748b", bg=bg_color, anchor=W).place(x=750, y=y_pos_fee)
        Label(root, text=val, font=("Segoe UI", 20, "bold"), fg=color, bg=bg_color, anchor=W).place(x=750, y=y_pos_fee + 25)
        if sub_text:
            Label(root, text=sub_text, font=("Segoe UI", 10, "bold"), fg="#475569", bg=bg_color, anchor=W).place(x=750, y=y_pos_fee + 65)
            y_pos_fee += 105
        else:
            y_pos_fee += 80

    root.mainloop()

if __name__ == "__main__":
    main("Student Name", "1")
