from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import db

def main():
    root = Tk()
    root.title("College Login")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    def register():
        root.destroy()
        from college import college_register
        college_register.main()

    def back():
        root.destroy()
        import home
        home.main()

    def login_action():
        college_id = txt_id.get().strip()
        password = txt_password.get()

        if college_id == "" or password == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        college = db.get_college(college_id)
        if college:
            if college.get("password") == password:
                if college.get("status") == "Accepted":
                    college_name = college.get("college_name")
                    messagebox.showinfo("Success", f"Welcome back, {college_name}!🤗")
                    root.destroy()
                    from college import college_dashboard
                    college_dashboard.main(college_name, college_id)
                else:
                    messagebox.showerror("Pending Approval", "Your college registration is pending admin approval!😱")
            else:
                messagebox.showerror("Error", "Invalid Password!😱")
        else:
            messagebox.showerror("Error", "College ID not registered!😱")

    # BACKGROUND IMAGE
    bg = Image.open(r"images\logindashboardadmin.jpeg")
    bg_resized = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Stylistic transparent layout variables
    bg_transparent = "#71a0cf"
    text_dark = "#0f172a"
    accent_orange = "#ea580c"

    # UI LABELS & ENTRIES
    title_label = Label(root, text="COLLEGE PORTAL LOGIN", fg=text_dark, bg=bg_transparent, font=("Segoe UI", 24, "bold"))
    title_label.place(x=510, y=80)

    Label(root, text="College ID", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=200, y=200)
    txt_id = Entry(root, font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_id.place(x=200, y=230, height=30)

    Label(root, text="Password", fg=text_dark, bg=bg_transparent, font=("Arial", 12, "bold")).place(x=200, y=300)
    txt_password = Entry(root, show="*", font=("Arial", 12), width=30, bd=1, highlightthickness=1, highlightbackground="#94a3b8")
    txt_password.place(x=200, y=330, height=30)

    btn_back = Button(root, text="← Back", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=50, width=140, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#dc2626"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#ef4444"))

    btn_login = Button(root, text="LOGIN AS COLLEGE", fg="white", bg=accent_orange, activebackground="#c2410c", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=login_action)
    btn_login.place(x=200, y=410, width=300, height=40)
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#c2410c"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg=accent_orange))

    Label(root, text="No account?", fg=text_dark, bg=bg_transparent, font=("Helvetica", 11, "bold")).place(x=150, y=520, width=180)
    
    btn_register = Button(root, text="REGISTER HERE", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=register)
    btn_register.place(x=300, y=520, width=140, height=30)
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#dc2626"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg="#ef4444"))

    root.mainloop()

if __name__ == "__main__":
    main()
