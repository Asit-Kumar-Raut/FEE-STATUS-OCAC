from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Feedbacks")
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

    # Header
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="STUDENT SUBMITTED FEEDBACKS", fg="#1e293b", bg="white", font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="Student ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=40, y=140)
    Label(root, text="Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=150, y=140)
    Label(root, text="Feedback Message", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=280, y=140)
    Label(root, text="Submitted Date", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=950, y=140)

    # Divider line
    Frame(root, bg="#cbd5e1", height=2).place(x=20, y=170, width=1326)

    cursor.execute("SELECT student_id, name, feedback, created_at FROM student_feedback ORDER BY created_at DESC")
    feedbacks = cursor.fetchall()

    if not feedbacks:
        Label(root, text="No student feedbacks submitted yet.", fg="#64748b", bg="white", font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # Loop and display each row directly using a y coordinate
        y = 180
        for fb in feedbacks:
            sid, sname, msg, dt = fb

            Label(root, text=sid, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=40, y=y)
            Label(root, text=sname, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=150, y=y)
            
            # Wrap message content so it fits nicely
            lbl_msg = Label(root, text=msg, font=("Segoe UI", 9), fg="#1e293b", bg="white", justify=LEFT, anchor=W, wraplength=620)
            lbl_msg.place(x=280, y=y)

            Label(root, text=str(dt), font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=950, y=y)

            # Draw a sub-divider
            Frame(root, bg="#f1f5f9", height=1).place(x=20, y=y + 35, width=1326)

            y += 40

    root.mainloop()
