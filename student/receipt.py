import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as _mysql_connector

def main(student_id="101", role="student", caller_name="Caller Name", caller_id="1"):
    root = Tk()
    root.title("Fee Payment Receipts")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    bg_color = "#f8fafc"
    root.config(bg=bg_color)

    # Database connection
    try:
        con = _mysql_connector.connect(
            host="localhost",
            user="root",
            password="asit@0987",
            database="ocac"
        )
        cursor = con.cursor()
    except _mysql_connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Failed to connect to MySQL database.\nError: {err}")
        root.destroy()
        return

    # Fetch student info
    cursor.execute("SELECT name, course, semester, total_fee, paid_amount, pending_amount FROM students WHERE student_id = %s", (student_id,))
    student_info = cursor.fetchone()

    if not student_info:
        messagebox.showerror("Error", f"Student with ID {student_id} not found!")
        root.destroy()
        return

    s_name, course, semester, total_fee, paid_amount, pending_amount = student_info

    def back_action():
        root.destroy()
        if role == "student":
            from student import studentdash_board
            studentdash_board.main(s_name, student_id)
        elif role == "admin":
            from admin import admin_student_fee
            admin_student_fee.main(caller_name, caller_id, student_id)
        elif role == "counselor":
            from counsiler import counciler_student
            counciler_student.main(caller_name, caller_id, student_id)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_title = Label(header_frame, text="🧾 FEE PAYMENT RECEIPTS", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 14, "bold"))
    lbl_title.place(x=30, y=15)

    btn_back = Button(header_frame, text="← BACK", fg="white", bg="#475569", activebackground="#334155", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=1230, y=12, width=100, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#334155"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#475569"))

    # Student details card
    details_card = Frame(root, bg="white", bd=1, relief=SOLID, highlightthickness=0)
    details_card.place(x=50, y=90, width=1266, height=100)

    # Decorate borders
    border_left = Frame(details_card, bg="#3b82f6", width=5)
    border_left.pack(side=LEFT, fill=Y)

    Label(details_card, text=f"Student Name: {s_name}", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg="white").place(x=20, y=20)
    Label(details_card, text=f"Student ID: {student_id}", font=("Segoe UI", 11), fg="#475569", bg="white").place(x=20, y=55)

    Label(details_card, text=f"Course: {course}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=400, y=20)
    Label(details_card, text=f"Semester: {semester}", font=("Segoe UI", 11), fg="#475569", bg="white").place(x=400, y=55)

    Label(details_card, text=f"Total Fee: ₹ {total_fee:,}", font=("Segoe UI", 11, "bold"), fg="#0d9488", bg="white").place(x=800, y=20)
    Label(details_card, text=f"Paid Amount: ₹ {paid_amount:,}   |   Pending Amount: ₹ {pending_amount:,}", font=("Segoe UI", 11), fg="#e11d48", bg="white").place(x=800, y=55)

    # Payments table label
    lbl_table = Label(root, text="PAYMENT HISTORY LOG", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg=bg_color)
    lbl_table.place(x=50, y=215)

    # Frame for Treeview & scrollbar
    table_frame = Frame(root, bg="white", bd=1, relief=SOLID)
    table_frame.place(x=50, y=245, width=1266, height=440)

    # Create Treeview table
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="#0f172a",
                    rowheight=35,
                    fieldbackground="white",
                    font=("Segoe UI", 10))
    style.map("Treeview", background=[("selected", "#dbeafe")], foreground=[("selected", "#1e40af")])
    style.configure("Treeview.Heading",
                    background="#f1f5f9",
                    foreground="#475569",
                    font=("Segoe UI", 10, "bold"),
                    rowheight=35)

    cols = ("Payment ID", "Amount Paid", "Payment Mode", "UTR Number", "Date & Time")
    tree = ttk.Treeview(table_frame, columns=cols, show="headings", style="Treeview")
    
    # Define widths & alignments
    tree.column("Payment ID", width=100, anchor=CENTER)
    tree.column("Amount Paid", width=200, anchor=E)
    tree.column("Payment Mode", width=150, anchor=CENTER)
    tree.column("UTR Number", width=250, anchor=W)
    tree.column("Date & Time", width=300, anchor=CENTER)

    # Headings
    for col in cols:
        tree.heading(col, text=col)

    # Add Scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Fetch payment logs from database
    cursor.execute("SELECT payment_id, amount, mode, utr_number, payment_date FROM payments WHERE student_id = %s ORDER BY payment_date DESC", (student_id,))
    payments = cursor.fetchall()

    if not payments:
        tree.insert("", "end", values=("N/A", "₹ 0", "No Payments", "-", "No history found"))
    else:
        for p in payments:
            pid, amount, mode, utr, p_date = p
            utr_display = utr if utr else "-"
            # Format currency and date string
            amt_str = f"₹ {amount:,}"
            tree.insert("", "end", values=(pid, amt_str, mode, utr_display, p_date))

    root.mainloop()
