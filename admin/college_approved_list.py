from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import db

def main(admin_name, admin_id):
    root = Tk()
    root.title("Approved Colleges")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_action():
        root.destroy()
        from admin import admin_dashboard
        admin_dashboard.main(admin_name, admin_id)

    def delete_college(cid):
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete College ID {cid}?")
        if ans:
            db.delete_college(cid)
            messagebox.showinfo("Success", f"College ID {cid} has been deleted successfully!👍")
            root.destroy()
            main(admin_name, admin_id)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="APPROVED COLLEGES LIST", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=520, y=80)

    # Table Column Headers
    Label(root, text="College ID", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=100, y=150)
    Label(root, text="College Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=250, y=150)
    Label(root, text="Principal Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=500, y=150)
    Label(root, text="Director Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=750, y=150)
    Label(root, text="Status", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=950, y=150)
    Label(root, text="Actions", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=1100, y=150)

    colleges = db.get_approved_colleges()

    if not colleges:
        Label(root, text="No approved colleges found.", fg="#64748b", bg=bg_color, font=("Segoe UI", 14, "bold")).place(x=520, y=280)
    else:
        # Loop and display each row directly
        y = 200
        for col in colleges:
            cid = col.get("college_id")
            cname = col.get("college_name")
            pname = col.get("principal_name")
            dname = col.get("director_name")
            status = col.get("status")

            Label(root, text=cid, font=("Segoe UI", 10), fg="#1e293b", bg=bg_color).place(x=100, y=y)
            Label(root, text=cname, font=("Segoe UI", 10), fg="#1e293b", bg=bg_color).place(x=250, y=y)
            Label(root, text=pname, font=("Segoe UI", 10), fg="#1e293b", bg=bg_color).place(x=500, y=y)
            Label(root, text=dname, font=("Segoe UI", 10), fg="#1e293b", bg=bg_color).place(x=750, y=y)

            Label(root, text=status, font=("Segoe UI", 10, "bold"), fg="#059669", bg=bg_color).place(x=950, y=y)

            def make_delete_cmd(id_val):
                return lambda: delete_college(id_val)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(cid))
            btn_delete.place(x=1100, y=y, width=70, height=25)

            y += 40

    root.mainloop()
