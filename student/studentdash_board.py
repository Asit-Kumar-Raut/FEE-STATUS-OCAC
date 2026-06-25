from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(name, student_id):
    root = Tk()
    root.title("Student Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="adbi@123",
        database="ocac"
    )
    cursor = con.cursor()

    # Query student details
    cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, total_fee, paid_amount, pending_amount FROM students WHERE student_id = %s", (student_id,))
    student_details = cursor.fetchone()

    s_id, s_name, username, phone, email, course, year, sem, total_fee, paid_amount, pending_amount = student_details

    def logout_action():
        root.destroy()
        from student import student_login
        student_login.main()

  

    def feedback_action():
        root.destroy()
        from student import student_feed_back
        student_feed_back.main(name, student_id)

    # Header Section
    lbl_student = Label(root, text=f"🎓 STUDENT PROFILE: {name} (ID: {student_id})", fg="#0d9488", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_student.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    title_label = Label(root, text="STUDENT FEE DASHBOARD", fg="#1e293b", bg="white", font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    # LEFT DIVISION: Student Profile Details
    lbl_title = Label(root, text="REGISTRATION DETAILS", font=("Segoe UI", 16, "bold"), fg="#3b82f6", bg="white")
    lbl_title.place(x=150, y=180)

    details = [ ("Student ID:", s_id), ("Full Name:", s_name),("Username:", username),("Phone Number:", phone),("Email ID:", email),("Course:", course),("Academic Year:", year), ("Semester:", sem),]

    y_pos = 230
    for label, val in details:
        Label(root, text=label, font=("Segoe UI", 11, "bold"), fg="#475569", bg="white", width=15, anchor=W).place(x=150, y=y_pos)
        Label(root, text=val, font=("Segoe UI", 11), fg="#1e293b", bg="white", anchor=W).place(x=300, y=y_pos)
        y_pos += 35

    # FEEDBACK BUTTON
    btn_feedback = Button(root, text="📝 GIVE FEEDBACK / REPORT ISSUE", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=feedback_action)
    btn_feedback.place(x=150, y=530, width=320, height=45)

    # RIGHT DIVISION: Fee Status
    lbl_fee_title = Label(root, text="FEE STATUS SUMMARY", font=("Segoe UI", 16, "bold"), fg="#0d9488", bg="white")
    lbl_fee_title.place(x=750, y=180)

    fee_items = [("Total Academic Fee", f"₹ {total_fee:,}", "#1e293b"),("Total Amount Paid", f"₹ {paid_amount:,}", "#10b981"),("Total Pending Amount", f"₹ {pending_amount:,}", "#ef4444") ]

    y_pos_fee = 230
    for title, val, color in fee_items:
        Label(root, text=title, font=("Segoe UI", 11, "bold"), fg="#64748b", bg="white", anchor=W).place(x=750, y=y_pos_fee)
        Label(root, text=val, font=("Segoe UI", 20, "bold"), fg=color, bg="white", anchor=W).place(x=750, y=y_pos_fee + 25)
        y_pos_fee += 80

    root.mainloop()

if __name__ == "__main__":
    main("Student Name", "1")
