from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Student Feedbacks")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
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

    def back_action():
        root.destroy()
        from admin import admin_dashboard
        admin_dashboard.main(admin_name, admin_id)

    def delete_feedback(fb_id):
        ans = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student feedback?")
        if ans:
            cursor.execute("DELETE FROM student_feedback WHERE id = %s", (fb_id,))
            con.commit()
            messagebox.showinfo("Success", "Feedback deleted successfully!🤗")
            root.destroy()
            main(admin_name, admin_id)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
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

    lbl_title = Label(root, text="STUDENT SUBMITTED FEEDBACKS", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="Student ID", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=40, y=140)
    Label(root, text="Name", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=150, y=140)
    Label(root, text="Feedback Message", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=280, y=140)
    Label(root, text="Submitted Date", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=900, y=140)
    Label(root, text="Actions", font=("Segoe UI", 10, "bold"), fg="#1e293b", bg=bg_color).place(x=1150, y=140)

    # Divider line
    Frame(root, bg="#cbd5e1", height=2).place(x=20, y=170, width=1326)

    cursor.execute("SELECT id, student_id, name, feedback, created_at FROM student_feedback ORDER BY created_at DESC")
    feedbacks = cursor.fetchall()

    if not feedbacks:
        Label(root, text="No student feedbacks submitted yet.", fg="#64748b", bg=bg_color, font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # Loop and display each row directly using a y coordinate
        y = 180
        for fb in feedbacks:
            fb_id, sid, sname, msg, dt = fb

            Label(root, text=sid, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=40, y=y)
            Label(root, text=sname, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=150, y=y)
            
            # Wrap message content so it fits nicely
            lbl_msg = Label(root, text=msg, font=("Segoe UI", 9), fg="#1e293b", bg=bg_color, justify=LEFT, anchor=W, wraplength=600)
            lbl_msg.place(x=280, y=y)

            Label(root, text=str(dt), font=("Segoe UI", 9), fg="#1e293b", bg=bg_color).place(x=900, y=y)

            def make_delete_cmd(id_val):
                def cmd():
                    delete_feedback(id_val)
                return cmd

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(fb_id))
            btn_delete.place(x=1150, y=y, width=70, height=25)
            btn_delete.bind("<Enter>", lambda e, b=btn_delete: b.config(bg="#dc2626"))
            btn_delete.bind("<Leave>", lambda e, b=btn_delete: b.config(bg="#ef4444"))

            # Draw a sub-divider
            Frame(root, bg="#f1f5f9", height=1).place(x=20, y=y + 35, width=1326)

            y += 40

    root.mainloop()
