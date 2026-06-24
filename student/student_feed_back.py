from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(name, student_id):
    root = Tk()
    root.title("Student Feedback")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def logout_action():
        root.destroy()
        from student import student_login
        student_login.main()

    def back_action():
        root.destroy()
        from student import studentdash_board
        studentdash_board.main(name, student_id)

    def submit_feedback():
        feedback_text = txt_feedback.get("1.0", END).strip()

        if feedback_text == "":
            messagebox.showerror("Error", "Feedback content cannot be empty!😟")
            return

        sql = "INSERT INTO student_feedback (student_id, name, feedback) VALUES (%s, %s, %s)"
        cursor.execute(sql, (student_id, name, feedback_text))
        con.commit()

        messagebox.showinfo("Success", "Thank you! Your feedback has been submitted successfully.🤗")
        back_action()

    # Header Section
    lbl_student = Label(root, text=f"🎓 STUDENT PROFILE: {name} (ID: {student_id})", fg="#0d9488", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_student.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    title_label = Label(root, text="SUBMIT FEEDBACK / REPORT ISSUE", fg="#1e293b", bg="white", font=("Segoe UI", 24, "bold"))
    title_label.place(x=430, y=80)

    # Form components directly on root
    Label(root, text="We value your feedback. Let us know if you face any issues.", font=("Segoe UI", 12), fg="#475569", bg="white").place(x=333, y=180)
    
    Label(root, text=f"Student ID: {student_id}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=333, y=220)
    Label(root, text=f"Student Name: {name}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=550, y=220)

    Label(root, text="Enter your feedback or issue description:", font=("Segoe UI", 11, "bold"), fg="#3b82f6", bg="white").place(x=333, y=260)

    # Text Area for Feedback
    txt_feedback = Text(root, font=("Segoe UI", 11), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_feedback.place(x=333, y=290, width=700, height=250)

    btn_submit = Button(root, text="SUBMIT FEEDBACK", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=submit_feedback)
    btn_submit.place(x=333, y=560, width=700, height=45)

    root.mainloop()
