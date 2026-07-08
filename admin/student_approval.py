from tkinter import *
from tkinter import messagebox
import db

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Management")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

    def logout_action():
        root.destroy()
        from college import college_login
        college_login.main()

    def back_action():
        root.destroy()
        from admin import student_approval_option
        student_approval_option.main(admin_name, admin_id)

    def accept_student(sid):
        db.approve_student(sid)
        messagebox.showinfo("Success", f"Student ID {sid} has been accepted successfully!🤗")
        root.destroy()
        main(admin_name, admin_id)

    def delete_student(sid):
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Student ID {sid}?")
        if ans:
            db.delete_student(sid)
            messagebox.showinfo("Success", f"Student ID {sid} has been deleted successfully!👍")
            root.destroy()
            main(admin_name, admin_id)

    # Header bar
    header_frame = Frame(root, bg="#78350f") # Deep amber header for College dashboard consistency
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🏛️ COLLEGE PROFILE: {admin_name} (ID: {admin_id})", fg="#fef3c7", bg="#78350f", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="STUDENTS REGISTRATION LIST", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=40, y=140)
    Label(root, text="Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=130, y=140)
    Label(root, text="Username", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=240, y=140)
    Label(root, text="Phone", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=350, y=140)
    Label(root, text="Email ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=460, y=140)
    Label(root, text="Course", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=640, y=140)
    Label(root, text="Year", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=730, y=140)
    Label(root, text="Sem", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=830, y=140)
    Label(root, text="Status", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=910, y=140)
    Label(root, text="Actions", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=1050, y=140)

    # Fetch pending students from Firestore specifically for this college (admin_name)
    students = db.get_students_by_college(admin_name, status="Pending")

    if not students:
        Label(root, text="No pending students found.", fg="#64748b", bg=bg_color, font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # Loop and display each row directly using a y coordinate
        y = 180
        for s in students:
            s_id = s.get("student_id")
            name = s.get("name")
            username = s.get("username")
            phone = s.get("phonenumber")
            email = s.get("emailid")
            course = s.get("course")
            year = s.get("academic_year")
            sem = s.get("semester")
            status = s.get("status")

            Label(root, text=s_id, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=40, y=y)
            Label(root, text=name, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=130, y=y)
            Label(root, text=username, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=240, y=y)
            Label(root, text=phone, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=350, y=y)
            Label(root, text=email, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=460, y=y)
            Label(root, text=course, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=640, y=y)
            Label(root, text=year, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=730, y=y)
            Label(root, text=sem, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=830, y=y)

            status_color = "#d97706" if status == "Pending" else "#059669"
            Label(root, text=status, font=("Segoe UI", 9, "bold"), fg=status_color, bg=bg_color).place(x=910, y=y)

            # Simple helper functions to trigger command for specific ID
            def make_accept_cmd(sid_val):
                return lambda: accept_student(sid_val)

            def make_delete_cmd(sid_val):
                return lambda: delete_student(sid_val)

            btn_accept = Button(root, text="Accept", fg="white", bg="#10b981", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_accept_cmd(s_id))
            btn_accept.place(x=1010, y=y, width=70, height=25)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(s_id))
            btn_delete.place(x=1090, y=y, width=70, height=25)

            y += 40

    root.mainloop()
