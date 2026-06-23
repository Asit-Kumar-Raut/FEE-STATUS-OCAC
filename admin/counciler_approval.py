from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox

def main(admin_name, admin_id):
    root = Tk()
    root.title("Counselor Approval")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    con = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="asit@0987",
        database="ocac"
    )
    cursor = con.cursor()

    def logout_action():
        root.destroy()
        from admin import admin_login
        admin_login.main()

    def back_action():
        root.destroy()
        from admin import admin_dashboard
        admin_dashboard.main(admin_name, admin_id)

    def accept_counselor(cid):
        cursor.execute("UPDATE counselors SET status = 'Accepted' WHERE counselor_id = %s", (cid,))
        con.commit()
        messagebox.showinfo("Success", f"Counselor ID {cid} has been accepted successfully!🤗")
        root.destroy()
        main(admin_name, admin_id)

    def delete_counselor(cid):
        ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Counselor ID {cid}?")
        if ans:
            cursor.execute("DELETE FROM counselors WHERE counselor_id = %s", (cid,))
            con.commit()
            messagebox.showinfo("Success", f"Counselor ID {cid} has been deleted successfully!👍")
            root.destroy()
            main(admin_name, admin_id)

    # Header section
    lbl_admin = Label(root, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg="#3b82f6", bg="white", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(root, text="LOG OUT", fg="white", bg="#ef4444", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1200, y=12, width=100, height=35)

    # Navigation & Title
    btn_back = Button(root, text="← BACK", fg="white", bg="#475569", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=30, y=80, width=100, height=35)

    lbl_title = Label(root, text="COUNSELORS REGISTRATION LIST", fg="#1e293b", bg="white", font=("Segoe UI", 20, "bold"))
    lbl_title.place(x=480, y=80)

    # Table Column Headers
    Label(root, text="Counselor ID", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=100, y=140)
    Label(root, text="Name", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=250, y=140)
    Label(root, text="Username", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=450, y=140)
    Label(root, text="Contact", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=650, y=140)
    Label(root, text="Status", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=850, y=140)
    Label(root, text="Actions", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=1050, y=140)

    cursor.execute("SELECT counselor_id, name, username, contact, status FROM counselors WHERE status = 'Pending'")
    counselors = cursor.fetchall()

    if not counselors:
        Label(root, text="No pending counselors found.", fg="#64748b", bg="white", font=("Segoe UI", 14, "bold")).place(x=500, y=250)
    else:
        # We loop and display each row directly using a y coordinate
        y = 180
        for c in counselors:
            c_id, name, username, contact, status = c

            Label(root, text=c_id, font=("Segoe UI", 10), fg="#1e293b", bg="white").place(x=100, y=y)
            Label(root, text=name, font=("Segoe UI", 10), fg="#1e293b", bg="white").place(x=250, y=y)
            Label(root, text=username, font=("Segoe UI", 10), fg="#1e293b", bg="white").place(x=450, y=y)
            Label(root, text=contact, font=("Segoe UI", 10), fg="#1e293b", bg="white").place(x=650, y=y)

            status_color = "#d97706" if status == "Pending" else "#059669"
            Label(root, text=status, font=("Segoe UI", 10, "bold"), fg=status_color, bg="white").place(x=850, y=y)

            # Simple helper functions to trigger command for specific ID
            def make_accept_cmd(cid):
                def cmd():
                    accept_counselor(cid)
                return cmd

            def make_delete_cmd(cid):
                def cmd():
                    delete_counselor(cid)
                return cmd

            btn_accept = Button(root, text="Accept", fg="white", bg="#10b981", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=make_accept_cmd(c_id))
            btn_accept.place(x=1020, y=y, width=80, height=28)

            btn_delete = Button(root, text="Delete", fg="white", bg="#ef4444", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=make_delete_cmd(c_id))
            btn_delete.place(x=1110, y=y, width=80, height=28)

            y += 40

    root.mainloop()
