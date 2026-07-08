from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import db

def main():
    root = Tk()
    root.title("College Registration")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # BACKGROUND IMAGE
    bg = Image.open(r"images\admin_login_register.jpeg")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def login():
        root.destroy()
        from college import college_login
        college_login.main()

    def registration():
        college_id = txt_id.get()
        college_name = txt_name.get().strip()
        principal_name = txt_principal.get().strip()
        director_name = txt_director.get().strip()
        password = txt_password.get()

        if college_id == "" or college_name == "" or principal_name == "" or director_name == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        if not college_id.isdigit() or all(c == '0' for c in college_id):
            messagebox.showerror("Error", "Invalid College ID!😱")
            return

        # Check existing College ID in Firestore
        existing_id = db.get_college(college_id)
        if existing_id:
            messagebox.showerror("Error", "College ID already registered!😱")
            return

        # Check existing College Name
        existing_name = db.get_college_by_name(college_name)
        if existing_name:
            messagebox.showerror("Error", "College Name already registered!😱")
            return

        college_data = {
            "college_id": college_id,
            "college_name": college_name,
            "principal_name": principal_name,
            "director_name": director_name,
            "password": password,
            "status": "Pending"
        }

        db.add_college(college_id, college_data)
        messagebox.showinfo("Success", "College registered successfully! Wait for Admin approval.🤗")
        login()

    def generate_unique_id():
        while True:
            new_id_val = str(random.randint(100, 9999))
            if not db.get_college(new_id_val):
                return new_id_val

    # Stylistic transparent layout variables
    bg_transparent = "#71a0cf" # Blends with admin_login_register.jpeg
    text_dark = "#0f172a"
    accent_orange = "#ea580c"

    title_label = Label(root, text="COLLEGE PORTAL REGISTRATION", fg=text_dark, bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=450, y=30)

    # Left Column
    Label(root, text="College ID", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=100)
    txt_id = Entry(root, font=("Arial", 11), bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_id.place(x=720, y=125, width=170, height=30)
    
    txt_id.insert(0, generate_unique_id())
    txt_id.config(state="readonly")

    Label(root, text="College Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=180)
    txt_name = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_name.place(x=720, y=205, height=30)

    Label(root, text="Principal Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=720, y=260)
    txt_principal = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_principal.place(x=720, y=285, height=30)

    # Right Column
    Label(root, text="Director Name", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=100)
    txt_director = Entry(root, font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_director.place(x=1070, y=125, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 11, "bold")).place(x=1070, y=180)
    txt_password = Entry(root, show="*", font=("Arial", 11), width=32, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=1070, y=205, height=30)

    def back():
        root.destroy()
        import home
        home.main()

    btn_back = Button(root, text="← Back to Home", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=50, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_register = Button(root, text="REGISTER COLLEGE", fg="white", bg=accent_orange, activebackground="#c2410c", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=registration)
    btn_register.place(x=860, y=350, width=300, height=45)
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#c2410c"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg=accent_orange))
    
    Label(root, text="Already registered?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=850, y=420, width=150)
    
    btn_login = Button(root, text="LOGIN HERE", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=login)
    btn_login.place(x=1000, y=420, width=120, height=30)
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#dc2626"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#ef4444"))

    root.mainloop()

if __name__ == "__main__":
    main()
