from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox
from tkinter import ttk

def main(admin_name, admin_id, student_id):
    root = Tk()
    root.title("Admin - Student Fee Profile Control")
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id VARCHAR(50),
            amount INT,
            mode VARCHAR(20),
            utr_number VARCHAR(100),
            payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()

    def get_student_data():
        cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, total_fee, paid_amount, pending_amount FROM students WHERE student_id = %s", (student_id,))
        return cursor.fetchone()

    student_details = get_student_data()
    s_id, s_name, username, phone, email, course, year, sem, total_fee, paid_amount, pending_amount = student_details

    cursor.execute("SELECT SUM(amount) FROM payments WHERE student_id = %s AND mode = 'Online'", (student_id,))
    res_online = cursor.fetchone()[0]
    online_paid = res_online if res_online is not None else 0

    cursor.execute("SELECT SUM(amount) FROM payments WHERE student_id = %s AND mode = 'Offline'", (student_id,))
    res_offline = cursor.fetchone()[0]
    offline_paid = res_offline if res_offline is not None else 0

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_action():
        root.destroy()
        from admin import academic_fee
        academic_fee.main(admin_name, admin_id)

    def add_payment():
        amt_str = txt_amount.get().strip()
        if amt_str == "":
            messagebox.showerror("Error", "Please enter a payment amount!😟")
            return
        
        if not amt_str.isdigit() or int(amt_str) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive number!😱")
            return

        added_amount = int(amt_str)

        mode = cb_mode.get()
        utr = ""
        if mode == "Online":
            utr = txt_utr.get().strip()
            if utr == "":
                messagebox.showerror("Error", "Please enter the UTR number for Online payment!😟")
                return
        
        cursor.execute("SELECT total_fee, paid_amount FROM students WHERE student_id = %s", (student_id,))
        t_fee, p_amt = cursor.fetchone()

        new_paid = p_amt + added_amount
        new_pending = t_fee - new_paid

        if new_paid > t_fee:
            messagebox.showerror("Error", f"Added amount ₹ {added_amount:,} exceeds the pending balance of ₹ {t_fee - p_amt:,}!😟")
            return

        cursor.execute("UPDATE students SET paid_amount = %s, pending_amount = %s WHERE student_id = %s", (new_paid, new_pending, student_id))
        cursor.execute("INSERT INTO payments (student_id, amount, mode, utr_number) VALUES (%s, %s, %s, %s)", (student_id, added_amount, mode, utr))
        con.commit()

        messagebox.showinfo("Success", f"Payment of ₹ {added_amount:,} registered successfully!🤗")
        root.destroy()
        main(admin_name, admin_id, student_id)

    def deduct_payment():
        amt_str = txt_amount.get().strip()
        if amt_str == "":
            messagebox.showerror("Error", "Please enter a deduction amount!😟")
            return
        
        if not amt_str.isdigit() or int(amt_str) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive number!😱")
            return

        deducted_amount = int(amt_str)
        
        cursor.execute("SELECT total_fee, paid_amount FROM students WHERE student_id = %s", (student_id,))
        t_fee, p_amt = cursor.fetchone()

        new_paid = p_amt - deducted_amount
        new_pending = t_fee - new_paid

        if new_paid < 0:
            messagebox.showerror("Error", f"Deduction amount ₹ {deducted_amount:,} exceeds current paid balance of ₹ {p_amt:,}!😟")
            return

        cursor.execute("UPDATE students SET paid_amount = %s, pending_amount = %s WHERE student_id = %s", (new_paid, new_pending, student_id))
        con.commit()

        messagebox.showinfo("Success", f"Fee payment reduced by ₹ {deducted_amount:,} successfully!👍")
        root.destroy()
        main(admin_name, admin_id, student_id)

    # Set background color
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", activebackground="#334155", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#334155"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#475569"))

    title_label = Label(root, text="ADMIN STUDENT FEE PROFILE CONTROL", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    title_label.place(x=430, y=80)

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
        ("Semester:", sem),
    ]

    y_pos = 230
    for label, val in details:
        Label(root, text=label, font=("Segoe UI", 11, "bold"), fg="#475569", bg=bg_color, width=15, anchor=W).place(x=150, y=y_pos)
        Label(root, text=val, font=("Segoe UI", 11), fg="#1e293b", bg=bg_color, anchor=W).place(x=300, y=y_pos)
        y_pos += 35

    # RIGHT DIVISION: Fee details & Add/Deduct Payment
    lbl_fee_title = Label(root, text="ACADEMIC FEE LEDGER CONTROL", font=("Segoe UI", 16, "bold"), fg="#0d9488", bg=bg_color)
    lbl_fee_title.place(x=750, y=180)

    # Fee summary labels
    Label(root, text="Total Sem Fee:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg=bg_color).place(x=750, y=230)
    Label(root, text=f"₹ {total_fee:,}", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg=bg_color).place(x=920, y=230)

    Label(root, text="Amount Paid:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg=bg_color).place(x=750, y=265)
    Label(root, text=f"₹ {paid_amount:,}", font=("Segoe UI", 12, "bold"), fg="#10b981", bg=bg_color).place(x=920, y=265)

    Label(root, text="  • Online Paid:", font=("Segoe UI", 10, "bold"), fg="#64748b", bg=bg_color).place(x=770, y=295)
    Label(root, text=f"₹ {online_paid:,}", font=("Segoe UI", 10, "bold"), fg="#475569", bg=bg_color).place(x=920, y=295)

    Label(root, text="  • Offline Paid:", font=("Segoe UI", 10, "bold"), fg="#64748b", bg=bg_color).place(x=770, y=325)
    Label(root, text=f"₹ {offline_paid:,}", font=("Segoe UI", 10, "bold"), fg="#475569", bg=bg_color).place(x=920, y=325)

    Label(root, text="Pending Bal:", font=("Segoe UI", 11, "bold"), fg="#64748b", bg=bg_color).place(x=750, y=360)
    Label(root, text=f"₹ {pending_amount:,}", font=("Segoe UI", 12, "bold"), fg="#ef4444", bg=bg_color).place(x=920, y=360)

    # Divider line
    Frame(root, bg="#cbd5e1", height=2).place(x=750, y=410, width=400)

    # Transaction Section
    Label(root, text="ADJUST SEMESTER FEE (AMOUNT IN ₹)", font=("Segoe UI", 12, "bold"), fg="#3b82f6", bg=bg_color).place(x=750, y=430)

    Label(root, text="Amount:", font=("Segoe UI", 10, "bold"), fg="#64748b", bg=bg_color).place(x=750, y=455)
    txt_amount = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_amount.place(x=750, y=480, width=150, height=35)

    Label(root, text="Mode:", font=("Segoe UI", 10, "bold"), fg="#64748b", bg=bg_color).place(x=920, y=455)
    cb_mode = ttk.Combobox(root, values=["Offline", "Online"], font=("Segoe UI", 11), state="readonly")
    cb_mode.place(x=920, y=480, width=150, height=35)
    cb_mode.set("Offline")

    lbl_utr = Label(root, text="UTR Number:", font=("Segoe UI", 10, "bold"), fg="#475569", bg=bg_color)
    txt_utr = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")

    btn_add = Button(root, text="➕ ADD PAYMENT", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=add_payment)
    btn_add.place(x=750, y=535, width=150, height=45)
    btn_add.bind("<Enter>", lambda e: btn_add.config(bg="#0f766e"))
    btn_add.bind("<Leave>", lambda e: btn_add.config(bg="#0d9488"))

    btn_deduct = Button(root, text="➖ DEDUCT PAYMENT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=deduct_payment)
    btn_deduct.place(x=920, y=535, width=150, height=45)
    btn_deduct.bind("<Enter>", lambda e: btn_deduct.config(bg="#dc2626"))
    btn_deduct.bind("<Leave>", lambda e: btn_deduct.config(bg="#ef4444"))

    def handle_mode_change(event):
        if cb_mode.get() == "Online":
            lbl_utr.place(x=750, y=525)
            txt_utr.place(x=750, y=550, width=320, height=35)
            btn_add.place(x=750, y=600, width=150, height=45)
            btn_deduct.place(x=920, y=600, width=150, height=45)
        else:
            lbl_utr.place_forget()
            txt_utr.place_forget()
            btn_add.place(x=750, y=535, width=150, height=45)
            btn_deduct.place(x=920, y=535, width=150, height=45)

    cb_mode.bind("<<ComboboxSelected>>", handle_mode_change)

    root.mainloop()
