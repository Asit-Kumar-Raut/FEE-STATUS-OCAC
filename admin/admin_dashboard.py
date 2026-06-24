from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Admin Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="ocac"
    )
    cursor = con.cursor()

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def show_counselors():
        root.destroy()
        from admin import counciler_approval
        counciler_approval.main(admin_name, admin_id)

    def show_students():
        root.destroy()
        from admin import student_approval
        student_approval.main(admin_name, admin_id)

    def show_academic_fee():
        root.destroy()
        from admin import academic_fee
        academic_fee.main(admin_name, admin_id)

    # Header section
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    # Title
    title_label = Label(root, text="ADMIN CONTROL DASHBOARD", fg="#1e293b", bg="white", font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=120)

    # 1st TILE: Counselor approvals (Purple Theme)
    btn_counselor = Button(root, text="COUNSELORS APPROVALS  →", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_counselors)
    btn_counselor.place(x=483, y=240, width=400, height=65)

    # 2nd TILE: Student management (Teal Theme)
    btn_student = Button(root, text="STUDENTS MANAGEMENT  →", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_students)
    btn_student.place(x=483, y=340, width=400, height=65)

    # 3rd TILE: Academic Fee control (Blue Theme)
    btn_fee = Button(root, text="ACADEMIC FEE CONTROL  →", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_academic_fee)
    btn_fee.place(x=483, y=440, width=400, height=65)

    root.mainloop()
