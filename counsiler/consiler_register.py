from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import random
import db

def main():
    root = Tk()
    root.title("Counselor Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

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
        name = txt_name.get().strip()
        username = txt_username.get().strip()
        contact = txt_contact.get().strip()
        password = txt_password.get()
        college_name = cb_college.get()

        if c_id == "" or name == "" or username == "" or contact == "" or password == "" or college_name == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not c_id.isdigit() or all(c == '0' for c in c_id):
            messagebox.showerror("Error", "Invalid Counselor ID!😱")
            return

        if db.get_counselor(c_id):
            messagebox.showerror("Error", "Counselor ID already registered!😱")
            return

        if db.get_counselor_by_username(username):
            messagebox.showerror("Error", "Username already taken!😱")
            return

        if len(contact) != 10 or not contact.isdigit() or contact == "0000000000":
            messagebox.showerror("Error", "Invalid Contact Number!😱")
            return

        counselor_data = {
            "counselor_id": c_id,
            "name": name,
            "username": username,
            "contact": contact,
            "password": password,
            "college_name": college_name,
            "status": "Pending"
        }
        db.add_counselor(c_id, counselor_data)

        messagebox.showinfo("Success", "Registration submitted! College approval required to log in.🤗")
        login()

    def generate_unique_id():
        while True:
            new_id_val = str(random.randint(100, 9999))
            if not db.get_counselor(new_id_val):
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

    Label(root, text="Select College", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=260)
    
    # Dynamic list of approved colleges
    approved_cols = db.get_approved_colleges()
    college_list = [col.get("college_name") for col in approved_cols]
    
    cb_college = ttk.Combobox(root, values=college_list, font=("Arial", 11), state="readonly", width=30)
    cb_college.place(x=1070, y=285, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    btn_back = Button(root, text="← Back to Home", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=50, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_register = Button(root, text="REGISTER AS COUNSELOR", fg="white", bg=accent_purple, activebackground="#6d28d9", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration)
    btn_register.place(x=900, y=360, width=300, height=45)
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#6d28d9"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg=accent_purple))
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=900, y=440, width=150)
    
    btn_login = Button(root, text="LOGIN HERE", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=login)
    btn_login.place(x=1070, y=440, width=120, height=30)
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#dc2626"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#ef4444"))
    root.mainloop()

if __name__ == "__main__":
    main()