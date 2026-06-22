from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
import student_login

def main():
    root = Tk()
    root.title("Student Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def login():
        root.destroy()
        student_login.main()

    bg = Image.open(r"images\Gemini_Generated_Image_5h883b5h883b5h88.png")
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

        if s_id == "" or name == "" or username == "" or phone == "" or email == "" or course == "" or year == "" or sem == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not s_id.isdigit() or all(c == '0' for c in s_id):
            messagebox.showerror("Error", "Invalid Student ID!😱")
            return

        cursor.execute("SELECT * FROM students WHERE student_id = %s", (s_id,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Student ID already registered!😱")
            return

        if len(phone) != 10 or not phone.isdigit() or phone == "0000000000":
            messagebox.showerror("Error", "Invalid Phone Number!😱")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters!😱")
            return

        sql = "INSERT INTO students(student_id, name, username, phonenumber, emailid, course, academic_year, semester, password, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'Pending')"
        cursor.execute(sql, (s_id, name, username, phone, email, course, year, sem, password))
        con.commit()

        messagebox.showinfo("Success", "Registration submitted! Admin approval required to log in.🤗")
        login()

    title_label = Label(root, text="Student Registration", fg="#1e293b", font=("Helvetica", 22, "bold"))
    title_label.place(x=515, y=20)

    # Left Column
    Label(root, text="Student ID", fg="#475569", font=("Arial", 11, "bold")).place(x=350, y=100)
    txt_id = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_id.place(x=350, y=125)

    Label(root, text="Full Name", fg="#475569", font=("Arial", 11, "bold")).place(x=350, y=180)
    txt_name = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_name.place(x=350, y=205)

    Label(root, text="Username", fg="#475569", font=("Arial", 11, "bold")).place(x=350, y=260)
    txt_username = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_username.place(x=350, y=285)

    Label(root, text="Phone Number", fg="#475569", font=("Arial", 11, "bold")).place(x=350, y=340)
    txt_phone = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_phone.place(x=350, y=365)

    Label(root, text="Email ID", fg="#475569", font=("Arial", 11, "bold")).place(x=350, y=420)
    txt_email = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_email.place(x=350, y=445)

    # Right Column
    Label(root, text="Course", fg="#475569", font=("Arial", 11, "bold")).place(x=700, y=100)
    txt_course = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_course.place(x=700, y=125)

    Label(root, text="Academic Year", fg="#475569", font=("Arial", 11, "bold")).place(x=700, y=180)
    txt_year = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_year.place(x=700, y=205)

    Label(root, text="Semester", fg="#475569", font=("Arial", 11, "bold")).place(x=700, y=260)
    txt_sem = Entry(root, font=("Arial", 11), width=30, bd=2)
    txt_sem.place(x=700, y=285)

    Label(root, text="Password", fg="#475569", font=("Arial", 11, "bold")).place(x=700, y=340)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=30, bd=2)
    txt_password.place(x=700, y=365)

    def back():
        root.destroy()
        import main
        main.main()

    Button(root, text="Back", fg="white", bg="gray", font=("Arial", 11, "bold"), command=back).place(x=50, y=610, width=120, height=30)

    Button(root, text="Register Student", fg="white", bg="#00d5ff", font=("Arial", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=515, y=530, width=300, height=45)
    
    Label(root, text="have an account->", fg="red", font=("Helvetica", 11, "bold")).place(x=500, y=610, width=150)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=login).place(x=660, y=610, width=120, height=30)

    root.mainloop()
