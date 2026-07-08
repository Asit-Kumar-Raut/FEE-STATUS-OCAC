from tkinter import *
from PIL import Image, ImageTk

def admin_loginpage():
    root.destroy()
    from admin import admin_login
    admin_login.main()

def college_registerpage():
    root.destroy()
    from college import college_register
    college_register.main()

def conciler_registerpage():
    root.destroy()
    from counsiler import consiler_register
    consiler_register.main()

def student_registerpage():
    root.destroy()
    from student import student_register
    student_register.main()

def main():
    global root
    root = Tk()
    root.title("Fee-Status-Manager - Home")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    bg = Image.open(r"images\home_college_background.jpeg")
    img = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(img)
    
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    card = Frame(root, bg="#0f172a", bd=1, highlightbackground="#1e293b", highlightthickness=1)
    card.place(x=443, y=140, width=480, height=480)

    Label(card, text="Role Selection", font=("Segoe UI", 15, "bold"), fg="#f8fafc", bg="#0f172a").pack(pady=(15, 3))
    Label(card, text="Please select your credential profile", font=("Segoe UI", 10), fg="#94a3b8", bg="#0f172a").pack(pady=(0, 15))

    btn_admin = Button(card, text="Admin→", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=admin_loginpage)
    btn_admin.pack(pady=8, ipady=10, fill=X, padx=40)
    btn_admin.bind("<Enter>", lambda e: btn_admin.config(bg="#2563eb"))
    btn_admin.bind("<Leave>", lambda e: btn_admin.config(bg="#3b82f6"))

    btn_college = Button(card, text="College→", fg="white", bg="#ea580c", activebackground="#c2410c", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=college_registerpage)
    btn_college.pack(pady=8, ipady=10, fill=X, padx=40)
    btn_college.bind("<Enter>", lambda e: btn_college.config(bg="#c2410c"))
    btn_college.bind("<Leave>", lambda e: btn_college.config(bg="#ea580c"))

    btn_counselor = Button(card, text="Counselor→", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=conciler_registerpage)
    btn_counselor.pack(pady=8, ipady=10, fill=X, padx=40)
    btn_counselor.bind("<Enter>", lambda e: btn_counselor.config(bg="#7c3aed"))
    btn_counselor.bind("<Leave>", lambda e: btn_counselor.config(bg="#8b5cf6"))

    btn_student = Button(card, text="Student→", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=student_registerpage)
    btn_student.pack(pady=8, ipady=10, fill=X, padx=40)
    btn_student.bind("<Enter>", lambda e: btn_student.config(bg="#0f766e"))
    btn_student.bind("<Leave>", lambda e: btn_student.config(bg="#0d9488"))

    team_text = "🌟 DEVELOPMENT TEAM\n• ASIT KUMAR RAUT (Team Leader)\n• BISHWA PRAKASH ROUT\n• AKASH KUMAR SWAIN\n• ADITYA KUMAR SAHOO"
    lbl_team = Label(root, text=team_text, fg="yellow", bg="#0f172a", font=("Segoe UI", 11, "bold"), justify=LEFT)
    lbl_team.place(x=1050, y=600)

    def back():
        root.destroy()
        import app
        app.main()
        
    def show_contact_info():
        from tkinter import messagebox
        messagebox.showinfo(
            "Contact Support",
            "📞 FOR ANY QUERIES OR SUPPORT, CONTACT:\n\n"
            "• +91 98612 16929\n"
            "• +91 89846 76600\n"
            "• +91 99384 21203\n"
            "• +91 98618 46536"
        )
        
    btn_back = Button(root, text="← Back", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=513, y=640, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_contact = Button(root, text="📞 Contact Support", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=show_contact_info)
    btn_contact.place(x=673, y=640, width=180, height=35)
    btn_contact.bind("<Enter>", lambda e: btn_contact.config(bg="#0f766e"))
    btn_contact.bind("<Leave>", lambda e: btn_contact.config(bg="#0d9488"))
    root.mainloop()

if __name__ == "__main__":
    main()

