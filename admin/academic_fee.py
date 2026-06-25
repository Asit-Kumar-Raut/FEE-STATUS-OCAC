from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox
from tkinter import ttk

def main(admin_name, admin_id):
    root = Tk()
    root.title("Academic Fee Control Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="adbi@123",
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

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_action():
        root.destroy()
        from admin import admin_dashboard
        admin_dashboard.main(admin_name, admin_id)

    def open_pending():
        root.destroy()
        from admin import admin_pending_students
        admin_pending_students.main(admin_name, admin_id)

    def open_full_paid():
        root.destroy()
        from admin import admin_full_paid_students
        admin_full_paid_students.main(admin_name, admin_id)

    def view_collection():
        option = cb_collection.get()
        mode_filter = cb_mode_filter.get()
        if option == "" or mode_filter == "":
            messagebox.showerror("Error", "Please select all options!😟")
            return
        
        if option == "1day collection":
            date_cond = "payment_date >= NOW() - INTERVAL 1 DAY"
        elif option == "last 7 days collection":
            date_cond = "payment_date >= NOW() - INTERVAL 7 DAY"
        elif option == "last 30 days":
            date_cond = "payment_date >= NOW() - INTERVAL 30 DAY"
        elif option == "full year":
            date_cond = "payment_date >= NOW() - INTERVAL 1 YEAR"
        else:
            return

        if mode_filter == "Online":
            query = f"SELECT SUM(amount) FROM payments WHERE {date_cond} AND mode = 'Online'"
        elif mode_filter == "Offline":
            query = f"SELECT SUM(amount) FROM payments WHERE {date_cond} AND mode = 'Offline'"
        else: # Total
            query = f"SELECT SUM(amount) FROM payments WHERE {date_cond}"
        
        cursor.execute(query)
        res = cursor.fetchone()[0]
        total = res if res is not None else 0
        messagebox.showinfo("Total Income", f"Collection for '{option}' ({mode_filter}):\n₹ {total:,} 🤗")

    def search_student():
        s_id = txt_search.get().strip()
        if s_id == "":
            messagebox.showerror("Error", "Please enter a Student ID to search!😟")
            return

        cursor.execute("SELECT student_id, name, course, semester FROM students WHERE student_id = %s AND status = 'Accepted'", (s_id,))
        student = cursor.fetchone()

        for widget in result_frame.winfo_children():
            widget.destroy()

        if student:
            sid, name, course, sem = student
            btn_result = Button(result_frame, text=f"👤 Student ID: {sid}\nName: {name}\nCourse: {course} ({sem})\n→ Click to Adjust Profile", 
                                fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", 
                                font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", justify=LEFT, padx=15, pady=15,
                                command=lambda: open_student_profile(sid))
            btn_result.pack(fill=X, pady=10)
        else:
            Label(result_frame, text="No approved student found with this ID!😟", fg="#ef4444", bg="white", font=("Segoe UI", 12, "bold"), anchor=W).pack(pady=15, fill=X)

    def open_student_profile(sid):
        root.destroy()
        from admin import admin_student_fee
        admin_student_fee.main(admin_name, admin_id, sid)

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

    title_label = Label(root, text="ACADEMIC FEE STATUS CONTROL", fg="#1e293b", bg=bg_color, font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    # Student Counts statistics
    cursor.execute("SELECT COUNT(*) FROM students WHERE status = 'Accepted'")
    total_stud = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM students WHERE pending_amount <= 0 AND status = 'Accepted'")
    full_stud = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM students WHERE pending_amount > 0 AND status = 'Accepted'")
    pending_stud = cursor.fetchone()[0]

    lbl_tot = Label(root, text=f"Total Student: {total_stud}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color)
    lbl_tot.place(x=100, y=145)

    lbl_full = Label(root, text=f"Full Paid: {full_stud}", font=("Segoe UI", 11, "bold"), fg="#0d9488", bg=bg_color)
    lbl_full.place(x=240, y=145)

    lbl_pend = Label(root, text=f"Pending Student: {pending_stud}", font=("Segoe UI", 11, "bold"), fg="#ef4444", bg=bg_color)
    lbl_pend.place(x=360, y=145)

    # LEFT SIDE: Simple Navigation Buttons
    lbl_nav_title = Label(root, text="STUDENT FEE CATEGORIES", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_nav_title.place(x=100, y=190)

    btn_pending = Button(root, text="⚠️ PENDING FEE STUDENTS", 
                         fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", 
                         font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_pending)
    btn_pending.place(x=100, y=240, width=400, height=65)
    btn_pending.bind("<Enter>", lambda e: btn_pending.config(bg="#7c3aed"))
    btn_pending.bind("<Leave>", lambda e: btn_pending.config(bg="#8b5cf6"))

    btn_full = Button(root, text="✅ FULLY PAID STUDENTS", 
                      fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", 
                      font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_full_paid)
    btn_full.place(x=100, y=340, width=400, height=65)
    btn_full.bind("<Enter>", lambda e: btn_full.config(bg="#0f766e"))
    btn_full.bind("<Leave>", lambda e: btn_full.config(bg="#0d9488"))

    # RIGHT SIDE: Search Bar section
    lbl_search_title = Label(root, text="SEARCH STUDENT BY ID", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_search_title.place(x=700, y=190)

    txt_search = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=700, y=240, width=300, height=35)

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=search_student)
    btn_search.place(x=1010, y=240, width=100, height=35)
    btn_search.bind("<Enter>", lambda e: btn_search.config(bg="#2563eb"))
    btn_search.bind("<Leave>", lambda e: btn_search.config(bg="#3b82f6"))

    # Search results container
    result_frame = Frame(root, bg="white")
    result_frame.place(x=700, y=290, width=410, height=300)

    lbl_coll_title = Label(root, text="COLLECTION REPORTS", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_coll_title.place(x=700, y=600)

    cb_collection = ttk.Combobox(root, values=["1day collection", "last 7 days collection", "last 30 days", "full year"], font=("Segoe UI", 11), state="readonly")
    cb_collection.place(x=700, y=640, width=160, height=35)
    cb_collection.set("1day collection")

    cb_mode_filter = ttk.Combobox(root, values=["Total", "Online", "Offline"], font=("Segoe UI", 11), state="readonly")
    cb_mode_filter.place(x=870, y=640, width=110, height=35)
    cb_mode_filter.set("Total")

    btn_view_coll = Button(root, text="View", fg="white", bg="#10b981", activebackground="#059669", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=view_collection)
    btn_view_coll.place(x=990, y=640, width=120, height=35)
    btn_view_coll.bind("<Enter>", lambda e: btn_view_coll.config(bg="#059669"))
    btn_view_coll.bind("<Leave>", lambda e: btn_view_coll.config(bg="#10b981"))

    root.mainloop()
