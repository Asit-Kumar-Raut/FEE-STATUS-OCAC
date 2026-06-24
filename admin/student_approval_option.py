from tkinter import *
from admin import student_approval
from admin import student_accepted_list
from admin import admin_dashboard

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Management Options")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    def pending():
        root.destroy()
        student_approval.main(admin_name, admin_id)

    def list_approved():
        root.destroy()
        student_accepted_list.main(admin_name, admin_id)

    def back():
        root.destroy()
        admin_dashboard.main(admin_name, admin_id)

    def logout():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    # Header section
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    Label(root, text="Student Management", fg="red", bg="white", font=("Helvetica", 26, "bold")).place(x=400, y=100)

    btn_pending = Button(root, text="Student Pending List", fg="white", bg="red", font=("Helvetica", 30), cursor="hand2", command=pending)
    btn_pending.place(x=400, y=250, width=500, height=70)

    btn_approved = Button(root, text="Student Approval List", fg="white", bg="red", font=("Helvetica", 30), cursor="hand2", command=list_approved)
    btn_approved.place(x=400, y=370, width=500, height=70)

    Button(root, text="← Back", fg="white", bg="#334155", font=("Arial", 11, "bold"), cursor="hand2", command=back).place(x=50, y=80, width=120, height=30)

    root.mainloop()
