from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import datetime
import db

def main():
    root = Tk()
    root.title("Student Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    def login():
        root.destroy()
        from student import student_login
        student_login.main()

    # BACKGROUND IMAGE (Student dedicated)
    bg = Image.open(r"images\student_registration.jpeg")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def registration():
        s_id = txt_id.get().strip()
        name = txt_name.get().strip()
        username = txt_username.get().strip()
        phone = txt_phone.get().strip()
        email = txt_email.get().strip()
        course = cb_course.get()
        year = cb_year.get()
        sem = txt_sem.get().strip()
        password = txt_password.get()
        college_name = cb_college.get()

        if s_id == "" or name == "" or username == "" or phone == "" or email == "" or course == "" or year == "" or sem == "" or password == "" or college_name == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        current_year = datetime.datetime.now().year
        valid_years = [str(current_year - i) for i in range(4)]
        if year not in valid_years:
            messagebox.showerror("Error", f"Academic Year must be one of the last 4 years: {', '.join(valid_years)}!😟")
            return

        if not s_id.isdigit() or all(c == '0' for c in s_id):
            messagebox.showerror("Error", "Invalid Student ID!😱")
            return

        if db.get_student(s_id):
            messagebox.showerror("Error", "Student ID already registered!😱")
            return

        if db.get_student_by_username(username):
            messagebox.showerror("Error", "Username already taken!😱")
            return

        if len(phone) != 10 or not phone.isdigit() or phone == "0000000000":
            messagebox.showerror("Error", "Invalid Phone Number!😱")
            return

        student_data = {
            "student_id": s_id,
            "name": name,
            "username": username,
            "phonenumber": phone,
            "emailid": email,
            "course": course,
            "academic_year": year,
            "semester": sem,
            "password": password,
            "college_name": college_name,
            "status": "Pending",
            "total_fee": 100000,
            "paid_amount": 0,
            "pending_amount": 100000
        }
        db.add_student(s_id, student_data)

        messagebox.showinfo("Success", "Registration submitted! College approval required to log in.🤗")
        login()

    # Stylistic transparent layout variables
    bg_transparent = "#d1d5ce" # Blends in with background
    text_dark = "#1e293b"
    accent_teal = "#0d9488"

    title_label = Label(root, text="STUDENT PORTAL REGISTRATION", fg="purple", bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=400, y=30)

    # Left Column Inputs
    Label(root, text="Student ID", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=50, y=100)
    txt_id = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_id.place(x=50, y=125, height=30)

    Label(root, text="Full Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=50, y=180)
    txt_name = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_name.place(x=50, y=205, height=30)

    Label(root, text="Username", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=50, y=260)
    txt_username = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_username.place(x=50, y=285, height=30)

    Label(root, text="Phone Number", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=50, y=340)
    txt_phone = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_phone.place(x=50, y=365, height=30)

    Label(root, text="Email ID", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=50, y=420)
    txt_email = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_email.place(x=50, y=445, height=30)

    # Right Column Inputs
    Label(root, text="Course", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=100)
    cb_course = ttk.Combobox(root, values=["Btech", "Bsc", "BCA", "BBA", "Diploma", "BSC nursing", "Mtech", "MBA", "MCA", "PHD"], font=("Arial", 11), state="readonly", width=30)
    cb_course.place(x=420, y=125, height=30)

    Label(root, text="Academic Year", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=180)
    current_year = datetime.datetime.now().year
    years_list = [str(current_year - i) for i in range(4)]
    cb_year = ttk.Combobox(root, values=years_list, font=("Arial", 11), state="readonly", width=30)
    cb_year.place(x=420, y=205, height=30)

    Label(root, text="Semester", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=260)
    txt_sem = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_sem.place(x=420, y=285, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=340)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=420, y=365, height=30)

    Label(root, text="Select College", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=420)
    approved_cols = db.get_approved_colleges()
    college_list = [col.get("college_name") for col in approved_cols]
    cb_college = ttk.Combobox(root, values=college_list, font=("Arial", 11), state="readonly", width=30)
    cb_college.place(x=420, y=445, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    btn_back = Button(root, text="← Back to Home", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=50, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_register = Button(root, text="REGISTER STUDENT", fg="white", bg=accent_teal, activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration)
    btn_register.place(x=200, y=530, width=300, height=45)
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#0f766e"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg=accent_teal))
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=200, y=610, width=150)
    
    btn_login = Button(root, text="LOGIN HERE", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=login)
    btn_login.place(x=370, y=610, width=120, height=30)
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#dc2626"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#ef4444"))

    root.mainloop()

if __name__ == "__main__":
    main()