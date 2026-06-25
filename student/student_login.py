from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main():
    root = Tk()
    root.title("Student Login")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="adbi@123",
        database="ocac"
    )
    cursor = con.cursor()

    def register():
        root.destroy()
        from student import student_register
        student_register.main()

    def back():
        root.destroy()
        from student import student_register
        student_register.main()

    def login_action():
        username = txt_username.get()

        if username == "":
            messagebox.showerror("Error", "Username is required!😟")
            return

        cursor.execute("SELECT name, student_id, status FROM students WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            name, student_id, status = result
            if status != "Accepted":
                messagebox.showerror("Access Denied", "Your account is pending admin approval.😟")
            else:
                messagebox.showinfo("Success", f"Welcome Student {name}!🤗")
                root.destroy()
                from student import studentdash_board
                studentdash_board.main(name, student_id)
        else:
            messagebox.showerror("Error", "Invalid Username or Password!😱")

    # BACKGROUND IMAGE (Student dedicated)
    bg = Image.open(r"images\student_login_reverse.png")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Stylistic transparent layout variables
    bg_transparent = "#d1d5ce" # Matching dominant color of student_registration.jpeg
    text_dark = "#1e293b"
    accent_teal = "#0d9488"

    # UI LABELS & ENTRIES DIRECTLY ON ROOT (Transparent layout)
    title_label = Label(root, text="STUDENT PORTAL LOGIN", fg="purple", bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=515, y=80)

    Label(root, text="Username", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=1000, y=200)
    txt_username = Entry(root, font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_username.place(x=1000, y=230, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=1000, y=300)
    txt_password = Entry(root, show="*", font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=1000, y=330, height=30)

    Button(root, text="← Back to Home", fg="white", bg="red", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=back).place(x=50, y=50, width=140, height=35)

    Button(root, text="LOGIN AS STUDENT", fg="white", bg=accent_teal, activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=login_action).place(x=1000, y=410, width=300, height=40)

    Label(root, text="Need account?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=950, y=520, width=180)
    Button(root, text="REGISTER HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=register).place(x=1150, y=520, width=140, height=30)

    root.mainloop()
