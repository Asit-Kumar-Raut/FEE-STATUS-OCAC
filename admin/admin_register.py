from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main():
    root = Tk()
    root.title("Admin Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # connection with sql
    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="ocac"
    )
    cursor = con.cursor()

    def login():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    # BACKGROUND IMAGE (Admin dedicated)
    bg = Image.open(r"images\admin_login_register.jpeg")
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

        # Check existing username
        cursor.execute("SELECT * FROM admins WHERE username = %s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already taken.😱")
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

        # Insert record
        sql = "INSERT INTO admins(admin_id, name, username, email, contact) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (admin_id, name, username, email, contact))
        con.commit()

        messagebox.showinfo("Success", "Admin registered successfully! Now you can login🤗")
        login()

    # Stylistic transparent layout variables
    bg_transparent = "#71a0cf" # Blends with admin_login_register.jpeg
    text_dark = "#0f172a"
    accent_blue = "#2563eb"

    title_label = Label(root, text="ADMIN PORTAL REGISTRATION", fg=text_dark, bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=30)

    # Left Column
    Label(root, text="Admin ID", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=100)
    txt_id = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_id.place(x=720, y=125, height=30)

    Label(root, text="Full Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=180)
    txt_name = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_name.place(x=720, y=205, height=30)

    Label(root, text="Username", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=260)
    txt_username = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_username.place(x=720, y=285, height=30)

    # Right Column
    Label(root, text="Email Address", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=100)
    txt_email = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_email.place(x=1070, y=125, height=30)

    Label(root, text="Contact Number", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=180)
    txt_contact = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_contact.place(x=1070, y=205, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=260)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=1070, y=285, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    Button(root, text="← Back to Home", fg="white", bg="red", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=back).place(x=50, y=50, width=140, height=35)

    Button(root, text="REGISTER AS ADMIN", fg="white", bg=accent_blue, font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=860, y=350, width=300, height=45)
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=850, y=420, width=150)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=login).place(x=1000, y=420, width=120, height=30)

    root.mainloop()
