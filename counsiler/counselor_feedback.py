from tkinter import *
from tkinter import messagebox
import db

def main(counselor_name, counselor_id, student_id):
    root = Tk()
    root.title("Counselor Feedback to College")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eff6ff"
    root.config(bg=bg_color)

    def logout_action():
        root.destroy()
        from counsiler import counsiler_login
        counsiler_login.main()

    def back_action():
        root.destroy()
        if student_id != "":
            from counsiler import counciler_student
            counciler_student.main(counselor_name, counselor_id, student_id)
        else:
            from counsiler import counciler_dashboard
            counciler_dashboard.main(counselor_name, counselor_id)

    def submit_feedback():
        s_id = txt_sid.get().strip()
        message_text = txt_message.get("1.0", END).strip()

        if s_id == "":
            messagebox.showerror("Error", "Student ID is required!😟")
            return

        if message_text == "":
            messagebox.showerror("Error", "Notice content cannot be empty!😟")
            return

        feedback_data = {
            "counselor_id": counselor_id,
            "counselor_name": counselor_name,
            "student_id": s_id,
            "message": message_text
        }
        db.add_counselor_feedback(feedback_data)

        messagebox.showinfo("Success", "Notice sent to College successfully!🤗")
        back_action()

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_counselor = Label(header_frame, text=f"🎓 COUNSELOR PROFILE: {counselor_name} (ID: {counselor_id})", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_counselor.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)

    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    title_label = Label(root, text="SEND MISTAKE / ADJUSTMENT NOTICE TO COLLEGE", fg="#1e293b", bg=bg_color, font=("Segoe UI", 22, "bold"))
    title_label.place(x=350, y=80)

    # Form components
    Label(root, text="Report incorrect payment logs or student adjustments directly to the College below.", font=("Segoe UI", 12), fg="#475569", bg=bg_color).place(x=333, y=180)
    
    Label(root, text=f"Counselor ID: {counselor_id}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=333, y=220)
    
    Label(root, text="Student ID:", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color).place(x=550, y=220)
    txt_sid = Entry(root, font=("Segoe UI", 11), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_sid.place(x=650, y=218, width=120, height=26)
    if student_id != "":
        txt_sid.insert(0, student_id)
        txt_sid.config(state="readonly")

    Label(root, text="Enter description of mistake or correction required:", font=("Segoe UI", 11, "bold"), fg="#3b82f6", bg=bg_color).place(x=333, y=260)

    txt_message = Text(root, font=("Segoe UI", 11), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_message.place(x=333, y=290, width=700, height=250)

    btn_submit = Button(root, text="SEND NOTICE TO COLLEGE", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=submit_feedback)
    btn_submit.place(x=333, y=560, width=700, height=45)

    root.mainloop()
