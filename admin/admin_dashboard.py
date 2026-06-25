from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Admin Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
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
        from admin import student_approval_option
        student_approval_option.main(admin_name, admin_id)

    def show_academic_fee():
        root.destroy()
        from admin import academic_fee
        academic_fee.main(admin_name, admin_id)

    def show_feedbacks():
        root.destroy()
        from admin import feedbackform_student
        feedbackform_student.main(admin_name, admin_id)

    def show_counselor_feedbacks():
        root.destroy()
        from admin import counselor_feedbacks
        counselor_feedbacks.main(admin_name, admin_id)

    def change_password():
        root.destroy()
        import admin.update_password_admin as update_password_admin
        update_password_admin.main(admin_name, admin_id)
    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    #password update page
    btn_reset = Button(root, text="🔄 Reset Password", fg="white", bg="#7c3aed", activebackground="#6d28d9", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=change_password)
    btn_reset.place(x=30, y=690, width=140, height=40)
    btn_reset.bind("<Enter>", lambda e: btn_reset.config(bg="#6d28d9"))
    btn_reset.bind("<Leave>", lambda e: btn_reset.config(bg="#7c3aed"))

    # Title
    title_label = Label(root, text="ADMIN CONTROL DASHBOARD", fg="#1e293b", bg=bg_color, font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=110)

    # 1st TILE: Counselor approvals (Purple Theme)
    btn_counselor = Button(root, text="COUNSELORS APPROVALS  →", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_counselors)
    btn_counselor.place(x=483, y=200, width=400, height=55)
    btn_counselor.bind("<Enter>", lambda e: btn_counselor.config(bg="#7c3aed"))
    btn_counselor.bind("<Leave>", lambda e: btn_counselor.config(bg="#8b5cf6"))

    # 2nd TILE: Student management (Teal Theme)
    btn_student = Button(root, text="STUDENTS MANAGEMENT  →", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_students)
    btn_student.place(x=483, y=270, width=400, height=55)
    btn_student.bind("<Enter>", lambda e: btn_student.config(bg="#0f766e"))
    btn_student.bind("<Leave>", lambda e: btn_student.config(bg="#0d9488"))

    # 3rd TILE: Academic Fee control (Blue Theme)
    btn_fee = Button(root, text="ACADEMIC FEE CONTROL  →", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_academic_fee)
    btn_fee.place(x=483, y=340, width=400, height=55)
    btn_fee.bind("<Enter>", lambda e: btn_fee.config(bg="#2563eb"))
    btn_fee.bind("<Leave>", lambda e: btn_fee.config(bg="#3b82f6"))

    # 4th TILE: Student Feedbacks (Orange Theme)
    btn_feedback = Button(root, text="STUDENT FEEDBACKS  →", fg="white", bg="#ea580c", activebackground="#c2410c", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_feedbacks)
    btn_feedback.place(x=483, y=410, width=400, height=55)
    btn_feedback.bind("<Enter>", lambda e: btn_feedback.config(bg="#c2410c"))
    btn_feedback.bind("<Leave>", lambda e: btn_feedback.config(bg="#ea580c"))

    # 5th TILE: Counselor Feedbacks (Red Theme)
    btn_counselor_feedback = Button(root, text="COUNSELOR FEEDBACKS  →", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_counselor_feedbacks)
    btn_counselor_feedback.place(x=483, y=480, width=400, height=55)
    btn_counselor_feedback.bind("<Enter>", lambda e: btn_counselor_feedback.config(bg="#dc2626"))
    btn_counselor_feedback.bind("<Leave>", lambda e: btn_counselor_feedback.config(bg="#ef4444"))

    root.mainloop()
