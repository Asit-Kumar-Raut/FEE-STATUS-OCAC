from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as _mysql_connector
from tkinter import messagebox
#conection of python programme with mysql
from admin import conselors_list
from admin import counselor_pending
from admin import admin_dashboard

def main(admin_name, admin_id):
    root = Tk()
    root.title("Counselor Management")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)  # fixed window size
    
    def pending():
        root.destroy()
        counselor_pending.main(admin_name, admin_id)  # call function from counselor_pending.py

    def list():
        root.destroy()
        conselors_list.main(admin_name, admin_id)  # call function from conselors_list.py
        
    def back():
        root.destroy()
        admin_dashboard.main(admin_name, admin_id)

    bg = Image.open("images/admin approval.jpeg")
    background_photo = ImageTk.PhotoImage(bg)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0 ,relwidth=1,relheight=1)

    Label(root, text="Counselor Management", fg="red", font=("Helvetica", 26)).place(x=400, y=40)
    # submit button
    btn = Button(root, text="Counselor Pending List", fg="white", bg="red", font=("Helvetica", 30), command=pending)
    btn.place(x=400, y=250)

    btn = Button(root, text="Counselor Approval List", fg="white", bg="red", font=("Helvetica", 30), command=list)
    btn.place(x=400, y=350)

    Button(root, text="← Back", fg="white", bg="#334155", font=("Arial", 11, "bold"), command=back).place(x=50, y=40, width=120, height=30)

    root.mainloop()
