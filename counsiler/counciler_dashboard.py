from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(counselor_name, counselor_id):
    root = Tk()
    root.title("Counselor Dashboard")
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


    def open_pending():
        root.destroy()
        from counsiler import pending_student
        pending_student.main(counselor_name, counselor_id)

    def open_full_paid():
        root.destroy()
        from counsiler import full_paid_student
        full_paid_student.main(counselor_name, counselor_id)

    def search_student():
        s_id = txt_search.get().strip()
        if s_id == "":
            messagebox.showerror("Error", "Please enter a Student ID to search!😟")
            return

        cursor.execute("SELECT student_id, name, course, semester FROM students WHERE student_id = %s", (s_id,))
        student = cursor.fetchone()

        for widget in result_frame.winfo_children():
            widget.destroy()

        if student:
            sid, name, course, sem = student
            btn_result = Button(result_frame, text=f"👤 Student ID: {sid}\nName: {name}\nCourse: {course} ({sem})\n→ Click to Open Profile", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", justify=LEFT, padx=15, pady=15, command=lambda: open_student_profile(sid))
            btn_result.pack(fill=X, pady=10)
        else:
            Label(result_frame, text="No student found with this ID!😟", fg="#ef4444", bg="white", font=("Segoe UI", 12, "bold"), anchor=W).pack(pady=15, fill=X)

    def open_student_profile(sid):
        root.destroy()
        from counsiler import counciler_student
        counciler_student.main(counselor_name, counselor_id, sid)

    lbl_counselor = Label(root, text=f" COUNSELOR PROFILE: {counselor_name} (ID: {counselor_id})", fg="#8b5cf6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_counselor.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)


    title_label = Label(root, text="COUNSELOR CONTROL DASHBOARD", fg="#1e293b", bg="white", font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    lbl_nav_title = Label(root, text="STUDENT CATEGORIES", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg="white")
    lbl_nav_title.place(x=100, y=190)

    btn_pending = Button(root, text="⚠️ PENDING FEE STUDENTS", 
                         fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", 
                         font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_pending)
    btn_pending.place(x=100, y=240, width=400, height=65)

    btn_full = Button(root, text="✅ FULLY PAID STUDENTS", 
                      fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", 
                      font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_full_paid)
                      
    btn_full.place(x=100, y=340, width=400, height=65)

    def feedback_action():
        root.destroy()
        from counsiler import counselor_feedback
        counselor_feedback.main(counselor_name, counselor_id, "")

    btn_feedback = Button(root, text="⚠️ REPORT MISTAKE / FEEDBACK", 
                          fg="white", bg="#ea580c", activebackground="#c2410c", activeforeground="white", 
                          font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=feedback_action)
    btn_feedback.place(x=100, y=440, width=400, height=65)

    lbl_search_title = Label(root, text="SEARCH STUDENT BY ID", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg="white")
    lbl_search_title.place(x=700, y=190)

    txt_search = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=700, y=240, width=300, height=35)

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=search_student)
    btn_search.place(x=1010, y=240, width=100, height=35)

    # Search results container
    result_frame = Frame(root, bg="white")
    result_frame.place(x=700, y=290, width=410, height=300)

    root.mainloop()
