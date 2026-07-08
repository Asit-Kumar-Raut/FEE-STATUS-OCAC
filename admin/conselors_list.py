from tkinter import *
from tkinter import messagebox
import db

def main(admin_name, admin_id):
    root = Tk()
    root.title("Counselor Management")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    def logout_action():
        root.destroy()
        from college import college_login
        college_login.main()

    def back_action():
        root.destroy()
        from admin import counciler_approval
        counciler_approval.main(admin_name, admin_id)

    def delete_counselor(cid):
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Counselor ID {cid}?")
        if ans:
            db.delete_counselor(cid)
            messagebox.showinfo("Success", f"Counselor ID {cid} has been deleted successfully!👍")
            root.destroy()
            main(admin_name, admin_id)

    # Header bar
    header_frame = Frame(root, bg="#78350f") # Deep amber header for College dashboard consistency
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🏛️ COLLEGE PROFILE: {admin_name} (ID: {admin_id})", fg="#fef3c7", bg="#78350f", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", activebackground="#334155", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#334155"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#475569"))

    lbl_title = Label(root, text="APPROVED COUNSELORS LIST", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=40, y=140)
    Label(root, text="Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=130, y=140)
    Label(root, text="Username", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=240, y=140)
    Label(root, text="Contact", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=350, y=140)
    Label(root, text="Status", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=460, y=140)
    Label(root, text="Actions", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=570, y=140)

    # Fetch accepted counselors from Firestore specifically for this college (admin_name)
    counselors = db.get_counselors_by_college(admin_name, status="Accepted")

    if not counselors:
        Label(root, text="No approved counselors found.", fg="#64748b", bg=bg_color, font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # Loop and display each row directly using a y coordinate
        y = 180
        for c in counselors:
            c_id = c.get("counselor_id")
            name = c.get("name")
            username = c.get("username")
            contact = c.get("contact")
            status = c.get("status")

            Label(root, text=c_id, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=40, y=y)
            Label(root, text=name, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=130, y=y)
            Label(root, text=username, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=240, y=y)
            Label(root, text=contact, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=350, y=y)

            status_color = "#059669"
            Label(root, text=status, font=("Segoe UI", 9, "bold"), fg=status_color, bg=bg_color).place(x=460, y=y)

            def make_delete_cmd(cid):
                return lambda: delete_counselor(cid)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(c_id))
            btn_delete.place(x=570, y=y, width=70, height=25)
            btn_delete.bind("<Enter>", lambda e, b=btn_delete: b.config(bg="#dc2626"))
            btn_delete.bind("<Leave>", lambda e, b=btn_delete: b.config(bg="#ef4444"))

            y += 40

    root.mainloop()
