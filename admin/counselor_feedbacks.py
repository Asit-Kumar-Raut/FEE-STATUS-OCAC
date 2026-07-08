from tkinter import *
from tkinter import messagebox
import db

def main(admin_name, admin_id):
    root = Tk()
    root.title("Counselor Feedbacks / Notices")
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
        from college import college_dashboard
        college_dashboard.main(admin_name, admin_id)

    def delete_feedback(fb_id):
        ans = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this counselor notice?")
        if ans:
            db.delete_counselor_feedback(fb_id)
            messagebox.showinfo("Success", "Notice deleted successfully!🤗")
            root.destroy()
            main(admin_name, admin_id)

    def open_adjust_profile(sid):
        root.destroy()
        from admin import admin_student_fee
        admin_student_fee.main(admin_name, admin_id, sid)

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

    lbl_title = Label(root, text="COUNSELOR ADJUSTMENT NOTICES", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="Counselor ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=40, y=140)
    Label(root, text="Couns. Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=150, y=140)
    Label(root, text="Student ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=270, y=140)
    Label(root, text="Notice Message", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=380, y=140)
    Label(root, text="Submitted Date", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=900, y=140)
    Label(root, text="Actions", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=1120, y=140)

    # Divider line
    Frame(root, bg="#cbd5e1", height=2).place(x=20, y=170, width=1326)

    # Retrieve counselor feedbacks for this college
    feedbacks = db.get_counselor_feedbacks(admin_name)

    if not feedbacks:
        Label(root, text="No counselor feedback notices found.", fg="#64748b", bg=bg_color, font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        y = 180
        for fb in feedbacks:
            fb_id = fb.get("feedback_id")
            cid = fb.get("counselor_id")
            cname = fb.get("counselor_name")
            sid = fb.get("student_id")
            msg = fb.get("message")
            dt = fb.get("created_at", "")
            
            # Format timestamp
            if "T" in dt:
                dt = dt.replace("T", " ")[:16]

            Label(root, text=cid, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=40, y=y)
            Label(root, text=cname, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=150, y=y)
            Label(root, text=sid, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=270, y=y)
            
            lbl_msg = Label(root, text=msg, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color, justify=LEFT, anchor=W, wraplength=500)
            lbl_msg.place(x=380, y=y)

            Label(root, text=str(dt), font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=900, y=y)

            def make_adjust_cmd(sid_val):
                return lambda: open_adjust_profile(sid_val)

            def make_delete_cmd(id_val):
                return lambda: delete_feedback(id_val)

            btn_adjust = Button(root, text="Adjust Fee", fg="white", bg="#3b82f6", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_adjust_cmd(sid))
            btn_adjust.place(x=1100, y=y, width=70, height=25)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(fb_id))
            btn_delete.place(x=1180, y=y, width=70, height=25)

            Frame(root, bg="#f1f5f9", height=1).place(x=20, y=y + 35, width=1326)

            y += 40

    root.mainloop()
