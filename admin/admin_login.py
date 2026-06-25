from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main():
    root = Tk()
    root.title("Admin Login")
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
        from admin import admin_register
        admin_register.main()

    def back():
        root.destroy()
        from admin import admin_register
        admin_register.main()

    def login_action():
        username = txt_username.get()
        password = txt_password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        cursor.execute("SELECT name, admin_id FROM admins WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            admin_name = result[0]
            admin_id = result[1]
            messagebox.showinfo("Success", f"Welcome back, {admin_name}!🤗")
            root.destroy()
            from admin import admin_dashboard
            admin_dashboard.main(admin_name, admin_id)
        else:
            messagebox.showerror("Error", "Invalid Username or Password!😱")

    # BACKGROUND IMAGE (Admin dedicated)
    bg = Image.open(r"images\logindashboardadmin.jpeg")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Stylistic transparent layout variables
    bg_transparent = "#71a0cf" # Blends with admin_login_register.jpeg
    text_dark = "#0f172a"
    accent_blue = "#2563eb"

    # UI LABELS & ENTRIES DIRECTLY ON ROOT (Transparent layout)
    title_label = Label(root, text="ADMIN PORTAL LOGIN", fg=text_dark, bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=515, y=80)

    Label(root, text="Username", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=200, y=200)
    txt_username = Entry(root, font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_username.place(x=200, y=230, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=200, y=300)
    txt_password = Entry(root, show="*", font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=200, y=330, height=30)

    btn_back = Button(root, text="← Back", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=50, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_login = Button(root, text="LOGIN AS ADMIN", fg="white", bg=accent_blue, activebackground="#1d4ed8", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=login_action)
    btn_login.place(x=200, y=410, width=300, height=40)
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#1d4ed8"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg=accent_blue))

    Label(root, text="No account?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=150, y=520, width=180)
    
    btn_register = Button(root, text="REGISTER HERE", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=register)
    btn_register.place(x=300, y=520, width=140, height=30)
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#dc2626"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg="#ef4444"))

    root.mainloop()