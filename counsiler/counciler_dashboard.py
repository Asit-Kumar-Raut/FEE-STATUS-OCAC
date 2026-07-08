from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db

def main(counselor_name, counselor_id):
    root = Tk()
    root.title("Counselor Dashboard")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    bg_color = "#eef2ff"
    root.config(bg=bg_color)

    # Decorative background accent elements
    left_bar = Frame(root, bg="#6366f1")  # Beautiful Indigo left bar
    left_bar.place(x=0, y=60, width=12, height=708)
    
    top_accent = Frame(root, bg="#6366f1")  # Top accent line below the header
    top_accent.place(x=0, y=60, width=1366, height=4)

    # Resolve counselor's college
    coun_details = db.get_counselor(counselor_id)
    college_name = coun_details.get("college_name", "") if coun_details else ""

    def logout_action():
        root.destroy()
        from counsiler import counsiler_login
        counsiler_login.main()

    def open_pending():
        root.destroy()
        from counsiler import pending_student
        pending_student.main(counselor_name, counselor_id)

    def open_full_paid():
        root.destroy()
        from counsiler import full_paid_student
        full_paid_student.main(counselor_name, counselor_id)

    def change_password():
        root.destroy()
        from counsiler import counciler_password_upadte
        counciler_password_upadte.main(counselor_name, counselor_id)

    def view_collection():
        option = cb_collection.get()
        mode_filter = cb_mode_filter.get()
        if option == "" or mode_filter == "":
            messagebox.showerror("Error", "Please select all options!😟")
            return
        
        date_range = None
        if option == "1day collection":
            date_range = "1day"
        elif option == "last 7 days collection":
            date_range = "7days"
        elif option == "last 30 days":
            date_range = "30days"
        elif option == "full year":
            date_range = "1year"

        mode = None
        if mode_filter == "Online":
            mode = "Online"
        elif mode_filter == "Offline":
            mode = "Offline"

        payments = db.get_payments_by_college(college_name, date_range=date_range, mode=mode)
        total = sum(p.get("amount", 0) for p in payments)
        messagebox.showinfo("Total Income", f"Collection for '{option}' ({mode_filter}):\n₹ {total:,} 🤗")

    def search_student():
        s_id = txt_search.get().strip()
        if s_id == "":
            messagebox.showerror("Error", "Please enter a Student ID to search!😟")
            return

        student = db.get_student(s_id)

        for widget in result_frame.winfo_children():
            widget.destroy()

        if student and student.get("college_name") == college_name:
            sid = student.get("student_id")
            name = student.get("name")
            course = student.get("course")
            sem = student.get("semester")
            
            btn_result = Button(result_frame, text=f"👤 Student ID: {sid}\nName: {name}\nCourse: {course} ({sem})\n→ Click to Open Profile", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", justify=LEFT, padx=15, pady=15, command=lambda: open_student_profile(sid))
            btn_result.pack(fill=X, pady=10)
        else:
            Label(result_frame, text="No student found with this ID!😟", fg="#ef4444", bg="white", font=("Segoe UI", 12, "bold"), anchor=W).pack(pady=15, fill=X)

    def open_student_profile(sid):
        root.destroy()
        from counsiler import counciler_student
        counciler_student.main(counselor_name, counselor_id, sid)

    # Header bar
    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_counselor = Label(header_frame, text=f"🎓 COUNSELOR PROFILE: {counselor_name} (ID: {counselor_id}) | College: {college_name}", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 12, "bold"))
    lbl_counselor.place(x=30, y=15)

    btn_logout = Button(header_frame, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
    btn_logout.place(x=1230, y=12, width=100, height=35)
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#dc2626"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#ef4444"))

    title_label = Label(root, text="COUNSELOR CONTROL DASHBOARD", fg="#4f46e5", bg=bg_color, font=("Segoe UI", 24, "bold"))
    title_label.place(x=480, y=80)

    title_accent = Frame(root, bg="#818cf8")
    title_accent.place(x=480, y=128, width=540, height=3)

    # Fetch stats filtered by college
    total_stud = len(db.get_students_by_college(college_name, status="Accepted"))
    full_stud = len(db.get_students_by_college(college_name, status="Accepted", paid_status="Fully Paid"))
    pending_stud = len(db.get_students_by_college(college_name, status="Accepted", paid_status="Pending"))

    lbl_tot = Label(root, text=f"Total Student: {total_stud}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg=bg_color)
    lbl_tot.place(x=100, y=145)

    lbl_full = Label(root, text=f"Full Paid: {full_stud}", font=("Segoe UI", 11, "bold"), fg="#0d9488", bg=bg_color)
    lbl_full.place(x=240, y=145)

    lbl_pend = Label(root, text=f"Pending Student: {pending_stud}", font=("Segoe UI", 11, "bold"), fg="#ef4444", bg=bg_color)
    lbl_pend.place(x=360, y=145)

    lbl_nav_title = Label(root, text="STUDENT CATEGORIES", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_nav_title.place(x=100, y=190)

    btn_pending = Button(root, text="⚠️ PENDING FEE STUDENTS", 
                         fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", 
                         font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_pending)
    btn_pending.place(x=100, y=240, width=400, height=65)
    btn_pending.bind("<Enter>", lambda e: btn_pending.config(bg="#7c3aed"))
    btn_pending.bind("<Leave>", lambda e: btn_pending.config(bg="#8b5cf6"))

    btn_full = Button(root, text="✅ FULLY PAID STUDENTS", 
                      fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", 
                      font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=open_full_paid)
                      
    btn_full.place(x=100, y=340, width=400, height=65)
    btn_full.bind("<Enter>", lambda e: btn_full.config(bg="#0f766e"))
    btn_full.bind("<Leave>", lambda e: btn_full.config(bg="#0d9488"))

    def feedback_action():
        root.destroy()
        from counsiler import counselor_feedback
        counselor_feedback.main(counselor_name, counselor_id, "")

    btn_feedback = Button(root, text="⚠️ REPORT MISTAKE / FEEDBACK", 
                          fg="white", bg="#ea580c", activebackground="#c2410c", activeforeground="white", 
                          font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=feedback_action)
    btn_feedback.place(x=100, y=440, width=400, height=65)
    btn_feedback.bind("<Enter>", lambda e: btn_feedback.config(bg="#c2410c"))
    btn_feedback.bind("<Leave>", lambda e: btn_feedback.config(bg="#ea580c"))

    lbl_search_title = Label(root, text="SEARCH STUDENT BY ID", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_search_title.place(x=700, y=190)

    txt_search = Entry(root, font=("Segoe UI", 12), bd=1, highlightthickness=1, highlightbackground="#cbd5e1", bg="white", fg="#1e293b", insertbackground="black")
    txt_search.place(x=700, y=240, width=300, height=35)

    btn_search = Button(root, text="🔍 Search", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=search_student)
    btn_search.place(x=1010, y=240, width=100, height=35)
    btn_search.bind("<Enter>", lambda e: btn_search.config(bg="#2563eb"))
    btn_search.bind("<Leave>", lambda e: btn_search.config(bg="#3b82f6"))

     #password update page
    btn_reset = Button(root, text="🔄 Reset Password", fg="white", bg="#7c3aed", activebackground="#6d28d9", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=change_password)
    btn_reset.place(x=30, y=690, width=140, height=40)
    btn_reset.bind("<Enter>", lambda e: btn_reset.config(bg="#6d28d9"))
    btn_reset.bind("<Leave>", lambda e: btn_reset.config(bg="#7c3aed"))
    
    # Search results container
    result_frame = Frame(root, bg="white")
    result_frame.place(x=700, y=290, width=410, height=300)

    lbl_coll_title = Label(root, text="COLLECTION REPORTS", font=("Segoe UI", 14, "bold"), fg="#1e293b", bg=bg_color)
    lbl_coll_title.place(x=700, y=600)

    cb_collection = ttk.Combobox(root, values=["1day collection", "last 7 days collection", "last 30 days", "full year"], font=("Segoe UI", 11), state="readonly")
    cb_collection.place(x=700, y=640, width=160, height=35)
    cb_collection.set("1day collection")

    cb_mode_filter = ttk.Combobox(root, values=["Total", "Online", "Offline"], font=("Segoe UI", 11), state="readonly")
    cb_mode_filter.place(x=870, y=640, width=110, height=35)
    cb_mode_filter.set("Total")

    btn_view_coll = Button(root, text="View", fg="white", bg="#10b981", activebackground="#059669", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=view_collection)
    btn_view_coll.place(x=990, y=640, width=120, height=35)
    btn_view_coll.bind("<Enter>", lambda e: btn_view_coll.config(bg="#059669"))
    btn_view_coll.bind("<Leave>", lambda e: btn_view_coll.config(bg="#10b981"))

    root.mainloop()
