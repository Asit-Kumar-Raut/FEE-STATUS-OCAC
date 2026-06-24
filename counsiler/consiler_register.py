from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
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
        from counsiler import counsiler_login
        counsiler_login.main()

    # BACKGROUND IMAGE (Counselor dedicated)
    bg = Image.open(r"images\counceler.jpeg")
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

        if c_id == "" or name == "" or username == "" or contact == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not c_id.isdigit() or all(c == '0' for c in c_id):
            messagebox.showerror("Error", "Invalid Counselor ID!😱")
            return

        cursor.execute("SELECT * FROM counselors WHERE counselor_id = %s", (c_id,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Counselor ID already registered!😱")
            return

        cursor.execute("SELECT * FROM counselors WHERE username = %s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already taken!😱")
            return

        if len(contact) != 10 or not contact.isdigit() or contact == "0000000000":
            messagebox.showerror("Error", "Invalid Contact Number!😱")
            return

        sql = "INSERT INTO counselors(counselor_id, name, username, contact, status) VALUES (%s,%s,%s,%s,'Pending')"
        cursor.execute(sql, (c_id, name, username, contact))
        con.commit()

        messagebox.showinfo("Success", "Registration submitted! Admin approval required to log in.🤗")
        login()

    import random

    def generate_unique_id():
        while True:
            new_id_val = str(random.randint(100, 9999))
            cursor.execute("SELECT * FROM counselors WHERE counselor_id = %s", (new_id_val,))
            if not cursor.fetchone():
                return new_id_val

    def regenerate_id():
        new_id_val = generate_unique_id()
        txt_id.config(state="normal")
        txt_id.delete(0, END)
        txt_id.insert(0, new_id_val)
        txt_id.config(state="readonly")

    # Stylistic transparent layout variables
    bg_transparent = "#7da9ad" # Blends with counceler.jpeg
    text_dark = "#0f172a"
    accent_purple = "#8b5cf6"

    title_label = Label(root, text="COUNSELOR PORTAL REGISTRATION", fg=text_dark, bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=30)

    # Left Column
    Label(root, text="Counselor ID", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=100)
    txt_id = Entry(root, font=("Arial", 11), bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_id.place(x=720, y=125, width=170, height=30)
    
    btn_gen = Button(root, text="🔄 Gen", fg="white", bg=accent_purple, font=("Arial", 9, "bold"), bd=0, cursor="hand2", command=regenerate_id)
    btn_gen.place(x=900, y=125, width=80, height=30)
    
    txt_id.insert(0, generate_unique_id())
    txt_id.config(state="readonly")

    Label(root, text="Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=180)
    txt_name = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_name.place(x=720, y=205, height=30)

    Label(root, text="Username", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=260)
    txt_username = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_username.place(x=720, y=285, height=30)

    # Right Column
    Label(root, text="Contact Number", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=100)
    txt_contact = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_contact.place(x=1070, y=125, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=180)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=1070, y=205, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    Button(root, text="← Back to Home", fg="white", bg="red", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=back).place(x=50, y=50, width=140, height=35)

    Button(root, text="REGISTER AS COUNSELOR", fg="white", bg=accent_purple, activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration).place(x=900, y=360, width=300, height=45)
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=900, y=440, width=150)
    Button(root, text="LOGIN HERE", fg="white", bg="red", font=("Arial", 11, "bold"), command=login).place(x=1070, y=440, width=120, height=30)
    root.mainloop()