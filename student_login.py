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
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def register():
        root.destroy()
        import student_register
        student_register.main()

    def back():
        root.destroy()
        import student_register
        student_register.main()

    def login_action():
        username = txt_username.get()
        password = txt_password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        cursor.execute("SELECT name, status FROM students WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            name, status = result
            if status != "Accepted":
                messagebox.showerror("Access Denied", "Your account is pending admin approval.😟")
            else:
                messagebox.showinfo("Success", f"Welcome Student {name}!🤗")
                root.destroy()
        else:
            messagebox.showerror("Error", "Invalid Username or Password!😱")

    # BACKGROUND IMAGE
    bg = Image.open(r"images\Gemini_Generated_Image_5h883b5h883b5h88.png")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # UI LABELS & ENTRIES
    title_label = Label(root, text="Student Login", fg="#1e293b", font=("Helvetica", 24, "bold"))
    title_label.place(x=533, y=80)

    Label(root, text="Username", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=200)
    txt_username = Entry(root, font=("Arial", 12), width=30, bd=2)
    txt_username.place(x=533, y=230)

    Label(root, text="Password", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=300)
    txt_password = Entry(root, show="*", font=("Arial", 12), width=30, bd=2)
    txt_password.place(x=533, y=330)

    Button(root, text="Back", fg="white", bg="gray", font=("Arial", 11, "bold"), command=back).place(x=50, y=520, width=120, height=30)

    Button(root, text="Login", fg="white", bg="#00d5ff", font=("Arial", 12, "bold"), bd=0, cursor="hand2", command=login_action).place(x=533, y=410, width=300, height=40)

    Label(root, text="don't have an account->", fg="red", font=("Helvetica", 11, "bold")).place(x=500, y=520, width=180)
    Button(root, text="REGISTER HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=register).place(x=690, y=520, width=140, height=30)

    root.mainloop()
