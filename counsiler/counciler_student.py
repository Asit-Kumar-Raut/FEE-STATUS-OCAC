from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(counselor_name, counselor_id, student_id):
    root = Tk()
    root.title("Counselor - Student Fee Profile")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def get_student_data():
        cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, total_fee, paid_amount, pending_amount FROM students WHERE student_id = %s", (student_id,))
        return cursor.fetchone()

    student_details = get_student_data()
    s_id, s_name, username, phone, email, course, year, sem, total_fee, paid_amount, pending_amount = student_details

    def logout_action():
        root.destroy()
        from counsiler import counsiler_login
        counsiler_login.main()

    def back_action():
        root.destroy()
        from counsiler import counciler_dashboard
        counciler_dashboard.main(counselor_name, counselor_id)

    def add_payment():
        amt_str = txt_amount.get().strip()
        if amt_str == "":
            messagebox.showerror("Error", "Please enter a payment amount!😟")
            return
        
        if not amt_str.isdigit() or int(amt_str) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive number!😱")
            return

        added_amount = int(amt_str)
        
        cursor.execute("SELECT total_fee, paid_amount FROM students WHERE student_id = %s", (student_id,))
        t_fee, p_amt = cursor.fetchone()

        new_paid = p_amt + added_amount
        
        # Validation check: total paid cannot exceed total fee (1,00,000)
        if new_paid > t_fee:
            messagebox.showerror("Error", f"Added amount ₹ {added_amount:,} exceeds the pending balance of ₹ {t_fee - p_amt:,}!😟")
            return

        new_pending = t_fee - new_paid

        # Update database
        cursor.execute("UPDATE students SET paid_amount = %s, pending_amount = %s WHERE student_id = %s", (new_paid, new_pending, student_id))
        con.commit()

        messagebox.showinfo("Success", f"Payment of ₹ {added_amount:,} registered successfully!🤗")
        
        root.destroy()
        main(counselor_name, counselor_id, student_id)

    # Header
    lbl_counselor = Label(root, text=f"🎓 COUNSELOR PROFILE: {counselor_name} (ID: {counselor_id})", fg="#8b5cf6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_counselor.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    title_label = Label(root, text="STUDENT FEE DETAILS & MANAGEMENT", fg="#1e293b", bg="white", font=("Segoe UI", 20, "bold"))
    title_label.place(x=430, y=80)

    # LEFT DIVISION: Student Profile Details
    lbl_title = Label(root, text="REGISTRATION DETAILS", font=("Segoe UI", 16, "bold"), fg="#3b82f6", bg="white")
    lbl_title.place(x=150, y=180)

    details = [ ("Student ID:", s_id), ("Full Name:", s_name), ("Username:", username), ("Phone Number:", phone), ("Email ID:", email), ("Course:", course),("Academic Year:", year),("Semester:", sem),]

    y_pos = 230
    for label, val in details:
        Label(root, text=label, font=("Segoe UI", 11, "bold"), fg="#475569", bg="white", width=15, anchor=W).place(x=150, y=y_pos)
        Label(root, text=val, font=("Segoe UI", 11), fg="#1e293b", bg="white", anchor=W).place(x=300, y=y_pos)
        y_pos += 35

    lbl_fee_title = Label(root, text="ACADEMIC FEE LEDGER", font=("Segoe UI", 16, "bold"), fg="#0d9488", bg="white")
    lbl_fee_title.place(x=750, y=180)

    Label(root, text="Total Sem Fee:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg="white").place(x=750, y=230)
    Label(root, text=f"₹ {total_fee:,}", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg="white").place(x=920, y=230)

    Label(root, text="Amount Paid:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg="white").place(x=750, y=265)
    Label(root, text=f"₹ {paid_amount:,}", font=("Segoe UI", 12, "bold"), fg="#10b981", bg="white").place(x=920, y=265)

    Label(root, text="Pending Bal:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg="white").place(x=750, y=300)
    Label(root, text=f"₹ {pending_amount:,}", font=("Segoe UI", 12, "bold"), fg="#ef4444", bg="white").place(x=920, y=300)

    Frame(root, bg="#e2e8f0", height=2).place(x=750, y=350, width=400)

    Label(root, text="ADD SEMESTER FEE ENTRY", font=("Segoe UI", 12, "bold"), fg="#3b82f6", bg="white").place(x=750, y=370)

    txt_amount = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_amount.place(x=750, y=410, width=320, height=35)

    btn_add = Button(root, text="➕ LOG ADDED PAYMENT", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=add_payment)
    btn_add.place(x=750, y=465, width=320, height=45)

    def feedback_action():
        root.destroy()
        from counsiler import counselor_feedback
        counselor_feedback.main(counselor_name, counselor_id, student_id)

    btn_feedback = Button(root, text="⚠️ REPORT ERROR / SEND NOTICE", fg="white", bg="#ea580c", activebackground="#c2410c", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=feedback_action)
    btn_feedback.place(x=750, y=525, width=320, height=45)

    root.mainloop()
