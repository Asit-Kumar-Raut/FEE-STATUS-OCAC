from tkinter import *
import mysql.connector as _mysql_connector
from tkinter import messagebox
from PIL import Image, ImageTk
from admin import admin_dashboard

# Database connection
con = _mysql_connector.connect(
    host="localhost",
    user="root",
    password="asit@0987",
    database="ocac"
)
cursor = con.cursor()

def main(admin_name="Admin User", admin_id="1"):
    root = Tk()
    root.title("password reset")
    root.geometry("768x600+0+0")
    root.resizable(False, False)

    bg_color = "#f0f9ff"
    root.config(bg=bg_color)

    def login():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_to_dashboard():
        root.destroy()
        admin_dashboard.main(admin_name, admin_id)

    def update():
        u = txt_username.get()
        uid = txt_userid.get()
        cp = txt_currentpassword.get()
        np = txt_newpassword.get()

        # Check for empty fields
        if u == "" or uid == "" or cp == "" or np == "":
            messagebox.showerror("Error", "All fields are required!😟")
            return

        # Check if the username, admin_id, and current password match
        sql = "SELECT * FROM admins WHERE username=%s AND admin_id=%s AND password=%s"
        values = (u, uid, cp)
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            # Update the password
            sql = "UPDATE admins SET password=%s WHERE username=%s AND admin_id=%s"
            values = (np, u, uid)
            cursor.execute(sql, values)
            con.commit()
            messagebox.showinfo("Success", "Password updated successfully! Please login again.🤗")
            login()  # Redirects to login page after successful reset
        else:
            # Show error and clear input fields if wrong credentials
            messagebox.showerror("Error", "Username, User ID, or Current Password is incorrect!😱")
            txt_username.delete(0, END)
            txt_userid.delete(0, END)
            txt_currentpassword.delete(0, END)
            txt_newpassword.delete(0, END)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=768, height=60)

    lbl_title = Label(header_frame, text="🔑 RESET ADMIN PASSWORD", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 13, "bold"))
    lbl_title.place(x=30, y=15)

    btn_back = Button(header_frame, text="← BACK", fg="white", bg="#475569", activebackground="#334155", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_to_dashboard)
    btn_back.place(x=650, y=12, width=90, height=35)

    title_sub = Label(root, text="Update login password for security", font=("Segoe UI", 11), fg="#475569", bg=bg_color)
    title_sub.place(x=220, y=100)

    Label(root, text="Username:", fg="#1e293b", bg=bg_color, font=("Segoe UI", 11, "bold")).place(x=220, y=160)
    Label(root, text="User ID:", fg="#1e293b", bg=bg_color, font=("Segoe UI", 11, "bold")).place(x=220, y=210)
    Label(root, text="Current Password:", fg="#1e293b", bg=bg_color, font=("Segoe UI", 11, "bold")).place(x=220, y=260)
    Label(root, text="New Password:", fg="#1e293b", bg=bg_color, font=("Segoe UI", 11, "bold")).place(x=220, y=310)

    # Entry Boxes
    txt_username = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_username.place(x=380, y=158, width=200, height=30)

    txt_userid = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_userid.place(x=380, y=208, width=200, height=30)

    txt_currentpassword = Entry(root, show="*", font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_currentpassword.place(x=380, y=258, width=200, height=30)

    txt_newpassword = Entry(root, show="*", font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_newpassword.place(x=380, y=308, width=200, height=30)

    # Submit Button
    btn = Button(root, text="UPDATE PASSWORD", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=update)
    btn.place(x=220, y=380, width=360, height=45)

    root.mainloop()