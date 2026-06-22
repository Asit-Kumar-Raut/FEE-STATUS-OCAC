from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
import counsiler_login

def main():
    root = Tk()
    root.title("Counselor Registration")
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
        counsiler_login.main()

    bg = Image.open(r"images\Gemini_Generated_Image_5h883b5h883b5h88.png")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def registration():
        c_id = txt_id.get()
        name = txt_name.get()
        username = txt_username.get()
        contact = txt_contact.get()
        password = txt_password.get()

        if c_id == "" or name == "" or username == "" or contact == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not c_id.isdigit() or all(c == '0' for c in c_id):
            messagebox.showerror("Error", "Invalid Counselor ID!😱")
            return

        cursor.execute("SELECT * FROM counselors WHERE counselor_id = %s", (c_id,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Counselor ID already registered!😱")
            return

        if len(contact) != 10 or not contact.isdigit() or contact == "0000000000":
            messagebox.showerror("Error", "Invalid Contact Number!😱")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters!😱")
            return

        sql = "INSERT INTO counselors(counselor_id, name, username, contact, password, status) VALUES (%s,%s,%s,%s,%s,'Pending')"
        cursor.execute(sql, (c_id, name, username, contact, password))
        con.commit()

        messagebox.showinfo("Success", "Registration submitted! Admin approval required to log in.🤗")
        login()

    title_label = Label(root, text="Counselor Registration", fg="#1e293b", font=("Helvetica", 24, "bold"))
    title_label.place(x=500, y=50)

    Label(root, text="Counselor ID", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=150)
    txt_id = Entry(root, font=("Arial", 12), width=30, bd=2)
    txt_id.place(x=533, y=180)

    Label(root, text="Name", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=240)
    txt_name = Entry(root, font=("Arial", 12), width=30, bd=2)
    txt_name.place(x=533, y=270)

    Label(root, text="Username", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=330)
    txt_username = Entry(root, font=("Arial", 12), width=30, bd=2)
    txt_username.place(x=533, y=360)

    Label(root, text="Contact", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=420)
    txt_contact = Entry(root, font=("Arial", 12), width=30, bd=2)
    txt_contact.place(x=533, y=450)

    Label(root, text="Password", fg="#475569", font=("Arial", 12, "bold")).place(x=533, y=510)
    txt_password = Entry(root, show="*", font=("Arial", 12), width=30, bd=2)
    txt_password.place(x=533, y=540)

    def back():
        root.destroy()
        import main
        main.main()

    Button(root, text="Back", fg="white", bg="gray", font=("Arial", 11, "bold"), command=back).place(x=50, y=680, width=120, height=30)

    Button(root, text="Register", fg="white", bg="#00d5ff", font=("Arial", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=533, y=610, width=300, height=40)
    
    Label(root, text="have an account->", fg="red", font=("Helvetica", 12, "bold")).place(x=515, y=680, width=200)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 12, "bold"), command=login).place(x=720, y=680)

    root.mainloop()