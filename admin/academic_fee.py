from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Academic Fee Control Dashboard")
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

    # Header
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    title_label = Label(root, text="ACADEMIC FEE STATUS CONTROL", fg="#1e293b", bg="white", font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    # LEFT SIDE: Simple Navigation Buttons
    lbl_nav_title = Label(root, text="STUDENT FEE CATEGORIES", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg="white")
    lbl_nav_title.place(x=100, y=190)

    btn_pending = Button(root, text="⚠️ PENDING FEE STUDENTS", 
                         fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", 
                         font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_pending)
    btn_pending.place(x=100, y=240, width=400, height=65)

    btn_full = Button(root, text="✅ FULLY PAID STUDENTS", 
                      fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", 
                      font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_full_paid)
    btn_full.place(x=100, y=340, width=400, height=65)

    # RIGHT SIDE: Search Bar section
    lbl_search_title = Label(root, text="SEARCH STUDENT BY ID", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg="white")
    lbl_search_title.place(x=700, y=190)

    txt_search = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=700, y=240, width=300, height=35)

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=search_student)
    btn_search.place(x=1010, y=240, width=100, height=35)

    # Search results container
    result_frame = Frame(root, bg="white")
    result_frame.place(x=700, y=290, width=410, height=300)

    root.mainloop()
