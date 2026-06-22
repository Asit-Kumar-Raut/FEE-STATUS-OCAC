from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
import admin_login

def main():
    root = Tk()
    root.title("Admin Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # connection with sql
    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def login():
        root.destroy()
        admin_login.main()

    # BACKGROUND IMAGE
    bg = Image.open(r"images\Gemini_Generated_Image_5h883b5h883b5h88.png")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def registration():
        admin_id = txt_id.get()
        name = txt_name.get()
        username = txt_username.get()
        email = txt_email.get()
        contact = txt_contact.get()
        password = txt_password.get()

        if admin_id == "":
            messagebox.showerror("Error", "Admin ID is required😟")
            return
        elif name == "":
            messagebox.showerror("Error", "Name is required😫")
            return
        elif username == "":
            messagebox.showerror("Error", "Username is required😫")
            return
        elif email == "":
            messagebox.showerror("Error", "Email Address is required🥺")
            return
        elif contact == "":
            messagebox.showerror("Error", "Contact Number is required😣")
            return
        elif password == "":
            messagebox.showerror("Error", "Password is required🫣")
            return

        # ID validation
        valid_id_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        for char in admin_id:
            if char not in valid_id_digits:
                messagebox.showerror("Error", "Admin ID must contain numbers only.😱")
                return
        
        if all(c == '0' for c in admin_id):
            messagebox.showerror("Error", "Admin ID cannot be zero.😱")
            return

        # Check existing Admin ID
        cursor.execute("SELECT * FROM admins WHERE admin_id = %s", (admin_id,))
        if cursor.fetchone():
            messagebox.showerror("Error", "This Admin ID is already registered.😱")
            return

        # Contact validation
        if len(contact) != 10 or not contact.isdigit():
            messagebox.showerror("Error", "Contact number must be exactly 10 digits.😱")
            return
        if contact == "0000000000":
            messagebox.showerror("Error", "Contact number cannot be all zeros.😱")
            return

        cursor.execute("SELECT * FROM admins WHERE contact = %s", (contact,))
        if cursor.fetchone():
            messagebox.showerror("Error", "This contact number is already registered.😱")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long.😱")
            return

        # Insert record
        sql = "INSERT INTO admins(admin_id, name, username, email, contact, password) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (admin_id, name, username, email, contact, password))
        con.commit()

        messagebox.showinfo("Success", "Admin registered successfully! Now you can login🤗")
        login()

    # LABELS & ENTRIES
    title_label = Label(root, text="Admin Registration", fg="#1e293b", font=("Helvetica", 24, "bold"))
    title_label.place(x=515, y=40)

    Label(root, text="Admin ID", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=120)
    txt_id = Entry(root, font=("Arial", 11), width=35, bd=2)
    txt_id.place(x=533, y=145)

    Label(root, text="Full Name", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=195)
    txt_name = Entry(root, font=("Arial", 11), width=35, bd=2)
    txt_name.place(x=533, y=220)

    Label(root, text="Username", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=270)
    txt_username = Entry(root, font=("Arial", 11), width=35, bd=2)
    txt_username.place(x=533, y=295)

    Label(root, text="Email Address", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=345)
    txt_email = Entry(root, font=("Arial", 11), width=35, bd=2)
    txt_email.place(x=533, y=370)

    Label(root, text="Contact Number", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=420)
    txt_contact = Entry(root, font=("Arial", 11), width=35, bd=2)
    txt_contact.place(x=533, y=445)

    Label(root, text="Password", fg="#475569", font=("Arial", 11, "bold")).place(x=533, y=495)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=35, bd=2)
    txt_password.place(x=533, y=520)

    def back():
        root.destroy()
        import main
        main.main()

    Button(root, text="Back", fg="white", bg="gray", font=("Arial", 11, "bold"), command=back).place(x=50, y=650, width=120, height=30)

    Button(root, text="Register as Admin", fg="white", bg="#00d5ff", font=("Arial", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=533, y=580, width=285, height=40)
    
    Label(root, text="have an account->", fg="red", font=("Helvetica", 11, "bold")).place(x=500, y=650, width=150)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=login).place(x=660, y=650, width=120, height=30)

    root.mainloop()
