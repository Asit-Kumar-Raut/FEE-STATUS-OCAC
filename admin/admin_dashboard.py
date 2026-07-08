from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Admin Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def show_college_approvals():
        root.destroy()
        from admin import college_approval
        college_approval.main(admin_name, admin_id)

    def show_approved_colleges():
        root.destroy()
        from admin import college_approved_list
        college_approved_list.main(admin_name, admin_id)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    # Title
    title_label = Label(root, text="ADMIN CONTROL DASHBOARD", fg="#1e293b", bg=bg_color, font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=180)

    # 1st TILE: College Approvals (Purple Theme)
    btn_pending = Button(root, text="PENDING COLLEGE APPROVALS  →", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_college_approvals)
    btn_pending.place(x=483, y=280, width=400, height=55)
    btn_pending.bind("<Enter>", lambda e: btn_pending.config(bg="#7c3aed"))
    btn_pending.bind("<Leave>", lambda e: btn_pending.config(bg="#8b5cf6"))

    # 2nd TILE: Approved Colleges List (Teal Theme)
    btn_approved = Button(root, text="APPROVED COLLEGES LIST  →", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_approved_colleges)
    btn_approved.place(x=483, y=370, width=400, height=55)
    btn_approved.bind("<Enter>", lambda e: btn_approved.config(bg="#0f766e"))
    btn_approved.bind("<Leave>", lambda e: btn_approved.config(bg="#0d9488"))

    root.mainloop()
