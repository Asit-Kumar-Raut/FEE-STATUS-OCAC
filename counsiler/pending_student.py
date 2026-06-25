from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(counselor_name, counselor_id):
    root = Tk()
    root.title("Pending Fee Students")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="adbi@123",
        database="ocac"
    )
    cursor = con.cursor()

    def logout_action():
        root.destroy()
        from counsiler import counsiler_login
        counsiler_login.main()

    def back_action():
        root.destroy()
        from counsiler import counciler_dashboard
        counciler_dashboard.main(counselor_name, counselor_id)

    def open_student_profile(sid):
        root.destroy()
        from counsiler import counciler_student
        counciler_student.main(counselor_name, counselor_id, sid)

    # Header
    lbl_counselor = Label(root, text=f"🎓 COUNSELOR PROFILE: {counselor_name} (ID: {counselor_id})", fg="#8b5cf6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_counselor.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="PENDING FEE STUDENT LIST", fg="#1e293b", bg="white", font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Search Bar (placed between title and table)
    Label(root, text="Search Pending Student ID:", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=100, y=155)
    
    txt_search = Entry(root, font=("Segoe UI", 11), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=320, y=153, width=200, height=30)

    def search_action():
        s_id = txt_search.get().strip()
        if s_id == "":
            cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted'")
        else:
            cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted' AND student_id = %s", (s_id,))
        
        display_students(cursor.fetchall())

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=search_action)
    btn_search.place(x=530, y=152, width=90, height=32)

    # Table Container Frame
    table_frame = Frame(root, bg="white")
    table_frame.place(x=100, y=200, width=1166, height=490)

    # Table Column Headers
    Label(table_frame, text="ID", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=30, y=20)
    Label(table_frame, text="Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=150, y=20)
    Label(table_frame, text="Course", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=350, y=20)
    Label(table_frame, text="Total Fee", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=550, y=20)
    Label(table_frame, text="Paid Amount", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=700, y=20)
    Label(table_frame, text="Pending Amount", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=850, y=20)
    Label(table_frame, text="Actions", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=1020, y=20)

    # Divider line under header
    Frame(table_frame, bg="#e2e8f0", height=2).place(x=20, y=55, width=1126)

    # Keep track of active row labels to dynamically destroy/redraw them during searches
    row_widgets = []

    def display_students(student_list):
        for widget in row_widgets:
            widget.destroy()
        row_widgets.clear()

        if not student_list:
            lbl_empty = Label(table_frame, text="No pending students found!🤗", fg="#ef4444", bg="white", font=("Segoe UI", 14, "bold"))
            lbl_empty.place(x=420, y=150)
            row_widgets.append(lbl_empty)
        else:
            y = 70
            for s in student_list:
                s_id, name, course, t_fee, paid, pending = s

                l1 = Label(table_frame, text=s_id, font=("Segoe UI", 10), fg="#334155", bg="white")
                l1.place(x=30, y=y)
                l2 = Label(table_frame, text=name, font=("Segoe UI", 10), fg="#334155", bg="white")
                l2.place(x=150, y=y)
                l3 = Label(table_frame, text=course, font=("Segoe UI", 10), fg="#334155", bg="white")
                l3.place(x=350, y=y)
                l4 = Label(table_frame, text=f"₹ {t_fee:,}", font=("Segoe UI", 10), fg="#334155", bg="white")
                l4.place(x=550, y=y)
                l5 = Label(table_frame, text=f"₹ {paid:,}", font=("Segoe UI", 10, "bold"), fg="#10b981", bg="white")
                l5.place(x=700, y=y)
                l6 = Label(table_frame, text=f"₹ {pending:,}", font=("Segoe UI", 10, "bold"), fg="#ef4444", bg="white")
                l6.place(x=850, y=y)

                def make_view_cmd(sid_val):
                    def cmd():
                        open_student_profile(sid_val)
                    return cmd

                btn_view = Button(table_frame, text="View Profile", fg="white", bg="#3b82f6", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=make_view_cmd(s_id))
                btn_view.place(x=1020, y=y-3, width=100, height=26)

                row_widgets.extend([l1, l2, l3, l4, l5, l6, btn_view])
                y += 40

    # Initial load of all pending students
    cursor.execute("SELECT student_id, name, course, total_fee, paid_amount, pending_amount FROM students WHERE pending_amount > 0 AND status = 'Accepted'")
    display_students(cursor.fetchall())

    root.mainloop()
