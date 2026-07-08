from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from admin import conselors_list
from admin import counselor_pending

def main(admin_name, admin_id):
    root = Tk()
    root.title("Counselor Management")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#f0f9ff"
    root.config(bg=bg_color)
    
    def pending():
        root.destroy()
        counselor_pending.main(admin_name, admin_id)

    def list_counselors():
        root.destroy()
        conselors_list.main(admin_name, admin_id)
        
    def back():
        root.destroy()
        from college import college_dashboard
        college_dashboard.main(admin_name, admin_id)

    def logout():
        root.destroy()
        from college import college_login
        college_login.main()

    header_frame = Frame(root, bg="#78350f") # Deep amber header for College dashboard consistency
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_admin = Label(header_frame, text=f"🏛️ COLLEGE PROFILE: {admin_name} (ID: {admin_id})", fg="#fef3c7", bg="#78350f", font=("Segoe UI", 12, "bold"))
    lbl_admin.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    Label(root, text="Counselor Management", fg="#78350f", bg=bg_color, font=("Segoe UI", 26, "bold")).place(x=400, y=100)
    
    btn_pending = Button(root, text="Counselor Pending List", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 20, "bold"), bd=0, cursor="hand2", command=pending)
    btn_pending.place(x=400, y=250, width=500, height=70)
    btn_pending.bind("<Enter>", lambda e: btn_pending.config(bg="#7c3aed"))
    btn_pending.bind("<Leave>", lambda e: btn_pending.config(bg="#8b5cf6"))

    btn_approved = Button(root, text="Approved Counselors List", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 20, "bold"), bd=0, cursor="hand2", command=list_counselors)
    btn_approved.place(x=400, y=370, width=500, height=70)
    btn_approved.bind("<Enter>", lambda e: btn_approved.config(bg="#0f766e"))
    btn_approved.bind("<Leave>", lambda e: btn_approved.config(bg="#0d9488"))

    btn_back = Button(root, text="← Back", fg="white", bg="#334155", activebackground="#1e293b", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=back)
    btn_back.place(x=50, y=80, width=120, height=30)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#1e293b"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#334155"))

    root.mainloop()
