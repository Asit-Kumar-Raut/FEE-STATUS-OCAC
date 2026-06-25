from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Pending Fee Students")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

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
        from admin import academic_fee
        academic_fee.main(admin_name, admin_id)

    def open_student_profile(sid):
        root.destroy()
        from admin import admin_student_fee
        admin_student_fee.main(admin_name, admin_id, sid)

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

    lbl_title = Label(root, text="PENDING FEE STUDENT LIST", fg="#1e293b", bg=bg_color, font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Search Bar
    Label(root, text="Search Pending Student ID:", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=100, y=155)
    
    txt_search = Entry(root, font=("Segoe UI", 11), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=320, y=153, width=200, height=30)

    def search_action():
        s_id = txt_search.get().strip()
        if s_id == "":
            cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted'")
        else:
            cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted' AND student_id = %s", (s_id,))
        
        display_students(cursor.fetchall())

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=search_action)
    btn_search.place(x=530, y=152, width=90, height=32)
    btn_search.bind("<Enter>", lambda e: btn_search.config(bg="#2563eb"))
    btn_search.bind("<Leave>", lambda e: btn_search.config(bg="#3b82f6"))

    # Table Container Frame
    table_frame = Frame(root, bg=bg_color)
    table_frame.place(x=100, y=200, width=1166, height=490)

    # Table Column Headers
    Label(table_frame, text="ID", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=30, y=20)
    Label(table_frame, text="Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=150, y=20)
    Label(table_frame, text="Course", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=350, y=20)
    Label(table_frame, text="Total Fee", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=550, y=20)
    Label(table_frame, text="Paid Amount", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=700, y=20)
    Label(table_frame, text="Pending Amount", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=850, y=20)
    Label(table_frame, text="Actions", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=1020, y=20)

    # Divider line under header
    Frame(table_frame, bg="#e2e8f0", height=2).place(x=20, y=55, width=1126)

    # List rows tracker
    row_widgets = []

    def display_students(student_list):
        for widget in row_widgets:
            widget.destroy()
        row_widgets.clear()

        if not student_list:
            lbl_empty = Label(table_frame, text="No pending students found!🤗", fg="#ef4444", bg=bg_color, font=("Segoe UI", 14, "bold"))
            lbl_empty.place(x=420, y=150)
            row_widgets.append(lbl_empty)
        else:
            y = 70
            for s in student_list:
                s_id, name, course, t_fee, paid, pending = s

                l1 = Label(table_frame, text=s_id, font=("Segoe UI", 10), fg="#334155", bg=bg_color)
                l1.place(x=30, y=y)
                l2 = Label(table_frame, text=name, font=("Segoe UI", 10), fg="#334155", bg=bg_color)
                l2.place(x=150, y=y)
                l3 = Label(table_frame, text=course, font=("Segoe UI", 10), fg="#334155", bg=bg_color)
                l3.place(x=350, y=y)
                l4 = Label(table_frame, text=f"₹ {t_fee:,}", font=("Segoe UI", 10), fg="#334155", bg=bg_color)
                l4.place(x=550, y=y)
                l5 = Label(table_frame, text=f"₹ {paid:,}", font=("Segoe UI", 10, "bold"), fg="#10b981", bg=bg_color)
                l5.place(x=700, y=y)
                l6 = Label(table_frame, text=f"₹ {pending:,}", font=("Segoe UI", 10, "bold"), fg="#ef4444", bg=bg_color)
                l6.place(x=850, y=y)

                def make_view_cmd(sid_val):
                    def cmd():
                        open_student_profile(sid_val)
                    return cmd

                btn_view = Button(table_frame, text="Adjust Fee", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=make_view_cmd(s_id))
                btn_view.place(x=1020, y=y-3, width=100, height=26)
                btn_view.bind("<Enter>", lambda e, b=btn_view: b.config(bg="#2563eb"))
                btn_view.bind("<Leave>", lambda e, b=btn_view: b.config(bg="#3b82f6"))

                row_widgets.extend([l1, l2, l3, l4, l5, l6, btn_view])
                y += 40

    # Initial load
    cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted'")
    display_students(cursor.fetchall())

    root.mainloop()
