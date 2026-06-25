from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox
from PIL import Image, ImageTk
from admin import admin_dashboard

# Database connection
con = _mysql_connector.connect(
    host="localhost",
    user="root",
    password="adbi@123",
    database="ocac"
)
cursor = con.cursor()

def main(admin_name, admin_id):
    root = Tk()
    root.title("password reset")
    root.geometry("768x600+0+0")
    root.resizable(False, False)

    def login():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_to_dashboard():
        root.destroy()
        admin_dashboard.main(admin_name, admin_id)

    def update():
        u = txt_username.get()
        p = txt_password.get()
        np = txt_newpassword.get()

        # Check for empty fields
        if u == "" or p == "" or np == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        # Check if the current username and password exist
        sql = "SELECT * FROM admins WHERE username=%s AND password=%s"
        values = (u, p)
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            # Update the password
            sql = "UPDATE admins SET password=%s WHERE username=%s AND password=%s"
            values = (np, u, p)
            cursor.execute(sql, values)
            con.commit()
            messagebox.showinfo("Success", "Password updated successfully! Please login again.🤗")
            login()  # Redirects to login page after successful reset
        else:
            # Show error and clear input fields if wrong credentials
            messagebox.showerror("Error", "Username or current password is incorrect!😱")
            txt_username.delete(0, END)
            txt_password.delete(0, END)
            txt_newpassword.delete(0, END)

    # Background Image
    bg = Image.open(r"images\update_password.jpeg")
    bg_resized = bg.resize((768, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(bg_resized)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # --- Back Button (Top Left Corner) ---
    btn_back = Button(root, text="<--Back", fg="black", bg="white", font=("Helvetica", 12, "bold"), command=back_to_dashboard)
    btn_back.place(x=20, y=20)

   
    Label(root, text="Username:", fg="red", font=("Helvetica", 16)).place(x=240, y=250)
    Label(root, text="Password:", fg="red", font=("Helvetica", 16)).place(x=240, y=300)
    Label(root, text="New Pass:", fg="red", font=("Helvetica", 16)).place(x=240, y=350)

    # Entry Boxes
    txt_username = Entry(root, font=("Helvetica", 14), width=18)
    txt_username.place(x=380, y=252)

    txt_password = Entry(root, show="*", font=("Helvetica", 14), width=18)
    txt_password.place(x=380, y=302)

    txt_newpassword = Entry(root, show="*", font=("Helvetica", 14), width=18)
    txt_newpassword.place(x=380, y=352)

    # Submit Button
    btn = Button(root, text="Submit", fg="white", bg="red", font=("Helvetica", 14, "bold"), width=12, command=update)
    btn.place(x=320, y=430)

    root.mainloop()