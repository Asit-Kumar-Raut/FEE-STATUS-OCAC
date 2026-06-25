from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
def main():
    root = Tk()
    root.title("Student Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="adbi@123",
        database="ocac"
    )
    cursor = con.cursor()

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
        s_id = txt_id.get()
        name = txt_name.get()
        username = txt_username.get()
        phone = txt_phone.get()
        email = txt_email.get()
        course = txt_course.get()
        year = txt_year.get()
        sem = txt_sem.get()
        password = txt_password.get()

        if s_id == "" or name == "" or username == "" or phone == "" or email == "" or course == "" or year == "" or sem == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not s_id.isdigit() or all(c == '0' for c in s_id):
            messagebox.showerror("Error", "Invalid Student ID!😱")
            return

        cursor.execute("SELECT * FROM students WHERE student_id = %s", (s_id,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Student ID already registered!😱")
            return

        cursor.execute("SELECT * FROM students WHERE username = %s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already taken!😱")
            return

        if len(phone) != 10 or not phone.isdigit() or phone == "0000000000":
            messagebox.showerror("Error", "Invalid Phone Number!😱")
            return

        sql = "INSERT INTO students(student_id, name, username, phonenumber, emailid, course, academic_year, semester, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'Pending')"
        cursor.execute(sql, (s_id, name, username, phone, email, course, year, sem))
        con.commit()

        messagebox.showinfo("Success", "Registration submitted! Admin approval required to log in.🤗")
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
    txt_course = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_course.place(x=420, y=125, height=30)

    Label(root, text="Academic Year", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=180)
    txt_year = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_year.place(x=420, y=205, height=30)

    Label(root, text="Semester", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=260)
    txt_sem = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_sem.place(x=420, y=285, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=420, y=340)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=420, y=365, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    Button(root, text="← Back to Home", fg="white", bg="red", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=back).place(x=50, y=50, width=140, height=35)

    Button(root, text="REGISTER STUDENT", fg="white", bg=accent_teal, activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=200, y=530, width=300, height=45)
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=200, y=610, width=150)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=login).place(x=370, y=610, width=120, height=30)

    root.mainloop()