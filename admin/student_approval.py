from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Management")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="AKASH12",
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

    def accept_student(sid):
        cursor.execute("UPDATE students SET status = 'Accepted' WHERE student_id = %s", (sid,))
        con.commit()
        messagebox.showinfo("Success", f"Student ID {sid} has been accepted successfully!🤗")
        root.destroy()
        main(admin_name, admin_id)

    def delete_student(sid):
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Student ID {sid}?")
        if ans:
            cursor.execute("DELETE FROM students WHERE student_id = %s", (sid,))
            con.commit()
            messagebox.showinfo("Success", f"Student ID {sid} has been deleted successfully!👍")
            root.destroy()
            main(admin_name, admin_id)

    # Header
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="STUDENTS REGISTRATION LIST", fg="#1e293b", bg="white", font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=40, y=140)
    Label(root, text="Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=130, y=140)
    Label(root, text="Username", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=240, y=140)
    Label(root, text="Phone", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=350, y=140)
    Label(root, text="Email ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=460, y=140)
    Label(root, text="Course", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=640, y=140)
    Label(root, text="Year", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=730, y=140)
    Label(root, text="Sem", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=830, y=140)
    Label(root, text="Status", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=910, y=140)
    Label(root, text="Actions", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg="white").place(x=1050, y=140)

    cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, status FROM students WHERE status = 'Pending'")
    students = cursor.fetchall()

    if not students:
        Label(root, text="No pending students found.", fg="#64748b", bg="white", font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # Loop and display each row directly using a y coordinate
        y = 180
        for s in students:
            s_id, name, username, phone, email, course, year, sem, status = s

            Label(root, text=s_id, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=40, y=y)
            Label(root, text=name, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=130, y=y)
            Label(root, text=username, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=240, y=y)
            Label(root, text=phone, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=350, y=y)
            Label(root, text=email, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=460, y=y)
            Label(root, text=course, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=640, y=y)
            Label(root, text=year, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=730, y=y)
            Label(root, text=sem, font=("Segoe UI", 9), fg="#1e293b", bg="white").place(x=830, y=y)

            status_color = "#d97706" if status == "Pending" else "#059669"
            Label(root, text=status, font=("Segoe UI", 9, "bold"), fg=status_color, bg="white").place(x=910, y=y)

            # Simple helper functions to trigger command for specific ID
            def make_accept_cmd(sid):
                def cmd():
                    accept_student(sid)
                return cmd

            def make_delete_cmd(sid):
                def cmd():
                    delete_student(sid)
                return cmd

            btn_accept = Button(root, text="Accept", fg="white", bg="#10b981", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_accept_cmd(s_id))
            btn_accept.place(x=1010, y=y, width=70, height=25)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(s_id))
            btn_delete.place(x=1090, y=y, width=70, height=25)

            y += 40

    root.mainloop()
