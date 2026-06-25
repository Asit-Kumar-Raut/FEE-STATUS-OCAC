from tkinter import *
from admin import student_approval
from admin import student_accepted_list
from admin import admin_dashboard

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Management Options")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

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

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    Label(root, text="Student Management", fg="red", bg=bg_color, font=("Helvetica", 26, "bold")).place(x=400, y=100)

    btn_pending = Button(root, text="Student Pending List", fg="white", bg="red", activebackground="#b91c1c", activeforeground="white", font=("Helvetica", 30), cursor="hand2", command=pending)
    btn_pending.place(x=400, y=250, width=500, height=70)
    btn_pending.bind("<Enter>", lambda e: btn_pending.config(bg="#b91c1c"))
    btn_pending.bind("<Leave>", lambda e: btn_pending.config(bg="red"))

    btn_approved = Button(root, text="Student Approval List", fg="white", bg="red", activebackground="#b91c1c", activeforeground="white", font=("Helvetica", 30), cursor="hand2", command=list_approved)
    btn_approved.place(x=400, y=370, width=500, height=70)
    btn_approved.bind("<Enter>", lambda e: btn_approved.config(bg="#b91c1c"))
    btn_approved.bind("<Leave>", lambda e: btn_approved.config(bg="red"))

    btn_back = Button(root, text="← Back", fg="white", bg="#334155", activebackground="#1e293b", activeforeground="white", font=("Arial", 11, "bold"), cursor="hand2", command=back)
    btn_back.place(x=50, y=80, width=120, height=30)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#1e293b"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#334155"))

    root.mainloop()
