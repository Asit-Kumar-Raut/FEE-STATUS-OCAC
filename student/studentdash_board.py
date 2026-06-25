from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(name, student_id):
    root = Tk()
    root.title("Student Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    # Query student details
    cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, total_fee, paid_amount, pending_amount FROM students WHERE student_id = %s", (student_id,))
    student_details = cursor.fetchone()

    s_id, s_name, username, phone, email, course, year, sem, total_fee, paid_amount, pending_amount = student_details

    # Query online/offline breakdown
    cursor.execute("SELECT SUM(amount) FROM payments WHERE student_id = %s AND mode = 'Online'", (student_id,))
    res_online = cursor.fetchone()[0]
    online_paid = res_online if res_online is not None else 0

    cursor.execute("SELECT SUM(amount) FROM payments WHERE student_id = %s AND mode = 'Offline'", (student_id,))
    res_offline = cursor.fetchone()[0]
    offline_paid = res_offline if res_offline is not None else 0

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

    details = [ ("Student ID:", s_id), ("Full Name:", s_name),("Username:", username),("Phone Number:", phone),("Email ID:", email),("Course:", course),("Academic Year:", year), ("Semester:", sem),]

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
