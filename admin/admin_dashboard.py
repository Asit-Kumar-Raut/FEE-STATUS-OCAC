# from tkinter import *
# from PIL import Image, ImageTk
# import mysql.connector as _mysql_connector
# from tkinter import messagebox

# def main(admin_name, admin_id):
#     root = Tk()
#     root.title("Admin Dashboard")
#     root.geometry("1366x768+0+0")
#     root.resizable(False, False)
#     root.config(bg="white") # Solid White background

#     con = _mysql_connector.connect(
#         host="localhost",
#         user="root",
#         password="AKASH12",
#         database="ocac"
#     )
#     cursor = con.cursor()

#     current_widgets = []

#     def clear_screen():
#         for widget in current_widgets:
#             widget.destroy()
#         current_widgets.clear()

#     def logout_action():
#         root.destroy()
#         from admin import admin_login
#         admin_login.main()

#     def accept_counselor(cid):
#         cursor.execute("UPDATE counselors SET status = 'Accepted' WHERE counselor_id = %s", (cid,))
#         con.commit()
#         messagebox.showinfo("Success", f"Counselor ID {cid} has been accepted successfully!🤗")
#         show_counselors()

#     def delete_counselor(cid):
#         ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Counselor ID {cid}?")
#         if ans:
#             cursor.execute("DELETE FROM counselors WHERE counselor_id = %s", (cid,))
#             con.commit()
#             messagebox.showinfo("Success", f"Counselor ID {cid} has been deleted successfully!👍")
#             show_counselors()

#     def accept_student(sid):
#         cursor.execute("UPDATE students SET status = 'Accepted' WHERE student_id = %s", (sid,))
#         con.commit()
#         messagebox.showinfo("Success", f"Student ID {sid} has been accepted successfully!🤗")
#         show_students()

#     def delete_student(sid):
#         ans = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Student ID {sid}?")
#         if ans:
#             cursor.execute("DELETE FROM students WHERE student_id = %s", (sid,))
#             con.commit()
#             messagebox.showinfo("Success", f"Student ID {sid} has been deleted successfully!👍")
#             show_students()

#     # THEME DESIGN TOKENS (Light Theme / White background)
#     bg_shadow = "#e2e8f0"       # Light gray shadow for tiles
#     card_color = "#f8fafc"      # Light grey card
#     table_bg = "#f1f5f9"        # Light table header background
#     text_dark = "#1e293b"       # Slate 800
#     text_muted = "#64748b"      # Slate 500
#     accent_blue = "#3b82f6"     # Slate blue

#     def setup_header():
#         # Top Header Navigation Bar
#         header_shadow = Frame(root, bg=bg_shadow, bd=0)
#         header_shadow.place(x=6, y=6, relwidth=1, height=60)
#         current_widgets.append(header_shadow)

#         header = Frame(root, bg=card_color, highlightbackground="#cbd5e1", highlightthickness=1)
#         header.place(x=0, y=0, relwidth=1, height=60)
#         current_widgets.append(header)

#         lbl_admin = Label(header, text=f"🔑 ADMIN PROFILE: {admin_name} (ID: {admin_id})", fg=accent_blue, bg=card_color, font=("Segoe UI", 12, "bold"))
#         lbl_admin.pack(side=LEFT, padx=30, pady=12)

#         btn_logout = Button(header, text="LOG OUT", fg="white", bg="#ef4444", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=logout_action)
#         btn_logout.pack(side=RIGHT, padx=30, pady=12, ipadx=10, ipady=4)

#     def show_dashboard():
#         clear_screen()
#         setup_header()

#         # Dashboard Title
#         title_label = Label(root, text="ADMIN CONTROL DASHBOARD", fg=text_dark, bg="white", font=("Segoe UI", 24, "bold"))
#         title_label.place(x=450, y=120)
#         current_widgets.append(title_label)

#         # 1st TILE: Counselor approvals (Purple Theme)
#         shadow_counselor = Frame(root, bg=bg_shadow, bd=0)
#         shadow_counselor.place(x=489, y=246, width=400, height=65)
#         current_widgets.append(shadow_counselor)

#         btn_counselor = Button(root, text="COUNSELORS APPROVALS  →", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_counselors)
#         btn_counselor.place(x=483, y=240, width=400, height=65)
#         current_widgets.append(btn_counselor)

#         # 2nd TILE: Student management (Teal Theme)
#         shadow_student = Frame(root, bg=bg_shadow, bd=0)
#         shadow_student.place(x=489, y=346, width=400, height=65)
#         current_widgets.append(shadow_student)

#         btn_student = Button(root, text="STUDENTS MANAGEMENT  →", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_students)
#         btn_student.place(x=483, y=340, width=400, height=65)
#         current_widgets.append(btn_student)

#         # 3rd TILE: Academic Fee control (Blue Theme)
#         shadow_fee = Frame(root, bg=bg_shadow, bd=0)
#         shadow_fee.place(x=489, y=446, width=400, height=65)
#         current_widgets.append(shadow_fee)

#         btn_fee = Button(root, text="ACADEMIC FEE CONTROL  →", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=show_academic_fee)
#         btn_fee.place(x=483, y=440, width=400, height=65)
#         current_widgets.append(btn_fee)

#     def show_counselors():
#         clear_screen()
#         setup_header()

#         # Back Button
#         btn_back = Button(root, text="← BACK", fg="white", bg="#475569", activebackground="#334155", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=show_dashboard)
#         btn_back.place(x=30, y=80, width=100, height=35)
#         current_widgets.append(btn_back)

#         lbl_title = Label(root, text="COUNSELORS REGISTRATION LIST", fg=text_dark, bg="white", font=("Segoe UI", 20, "bold"))
#         lbl_title.place(x=480, y=80)
#         current_widgets.append(lbl_title)

#         # Main Table Container Card
#         list_shadow = Frame(root, bg=bg_shadow, bd=0)
#         list_shadow.place(x=56, y=136, width=1266, height=580)
#         list_frame = Frame(root, bg="white", bd=0, highlightbackground="#cbd5e1", highlightthickness=1)
#         list_frame.place(x=50, y=130, width=1266, height=580)
#         current_widgets.append(list_frame)

#         canvas = Canvas(list_frame, bg="white", highlightthickness=0)
#         scrollbar = Scrollbar(list_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = Frame(canvas, bg="white")

#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )

#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)

#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")

#         cursor.execute("SELECT counselor_id, name, username, contact, status FROM counselors")
#         counselors = cursor.fetchall()

#         if not counselors:
#             lbl_no = Label(scrollable_frame, text="No registered counselors found.", fg=text_muted, bg="white", font=("Segoe UI", 14, "bold"))
#             lbl_no.pack(pady=100, padx=400)
#         else:
#             # Table Header
#             header_row = Frame(scrollable_frame, bg=table_bg)
#             header_row.pack(fill="x", expand=True, pady=(10, 5))

#             Label(header_row, text="Counselor ID", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=15, anchor="w").grid(row=0, column=0, padx=10, pady=10)
#             Label(header_row, text="Name", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=22, anchor="w").grid(row=0, column=1, padx=10, pady=10)
#             Label(header_row, text="Username", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=22, anchor="w").grid(row=0, column=2, padx=10, pady=10)
#             Label(header_row, text="Contact", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=18, anchor="w").grid(row=0, column=3, padx=10, pady=10)
#             Label(header_row, text="Status", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=12, anchor="w").grid(row=0, column=4, padx=10, pady=10)
#             Label(header_row, text="Actions", font=("Segoe UI", 11, "bold"), fg=text_dark, bg=table_bg, width=25).grid(row=0, column=5, columnspan=2, padx=10, pady=10)

#             for c in counselors:
#                 c_id, name, username, contact, status = c

#                 row_frame = Frame(scrollable_frame, bg="white", bd=1, highlightbackground="#e2e8f0", highlightthickness=1)
#                 row_frame.pack(fill="x", expand=True, pady=5)

#                 Label(row_frame, text=c_id, font=("Segoe UI", 10), fg=text_dark, bg="white", width=15, anchor="w").grid(row=0, column=0, padx=10, pady=10)
#                 Label(row_frame, text=name, font=("Segoe UI", 10), fg=text_dark, bg="white", width=22, anchor="w").grid(row=0, column=1, padx=10, pady=10)
#                 Label(row_frame, text=username, font=("Segoe UI", 10), fg=text_dark, bg="white", width=22, anchor="w").grid(row=0, column=2, padx=10, pady=10)
#                 Label(row_frame, text=contact, font=("Segoe UI", 10), fg=text_dark, bg="white", width=18, anchor="w").grid(row=0, column=3, padx=10, pady=10)

#                 status_color = "#d97706" if status == "Pending" else "#059669"
#                 Label(row_frame, text=status, font=("Segoe UI", 10, "bold"), fg=status_color, bg="white", width=12, anchor="w").grid(row=0, column=4, padx=10, pady=10)

#                 btn_accept = Button(row_frame, text="Accept", fg="white", bg="#10b981", activebackground="#059669", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2",
#                                     command=lambda cid=c_id: accept_counselor(cid))
#                 btn_accept.grid(row=0, column=5, padx=5, pady=10, ipadx=10, ipady=3)

#                 if status == "Accepted":
#                     btn_accept.configure(state="disabled", bg="#e2e8f0", fg="#94a3b8", text="Accepted")

#                 btn_delete = Button(row_frame, text="Delete", fg="white", bg="#ef4444", activebackground="#dc2626", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2",
#                                     command=lambda cid=c_id: delete_counselor(cid))
#                 btn_delete.grid(row=0, column=6, padx=5, pady=10, ipadx=10, ipady=3)

#     def show_students():
#         clear_screen()
#         setup_header()

#         # Back Button
#         btn_back = Button(root, text="← BACK", fg="white", bg="#475569", activebackground="#334155", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=show_dashboard)
#         btn_back.place(x=30, y=80, width=100, height=35)
#         current_widgets.append(btn_back)

#         lbl_title = Label(root, text="STUDENTS REGISTRATION LIST", fg=text_dark, bg="white", font=("Segoe UI", 20, "bold"))
#         lbl_title.place(x=480, y=80)
#         current_widgets.append(lbl_title)

#         # Main Table Container Card
#         list_shadow = Frame(root, bg=bg_shadow, bd=0)
#         list_shadow.place(x=26, y=136, width=1326, height=580)
#         list_frame = Frame(root, bg="white", bd=0, highlightbackground="#cbd5e1", highlightthickness=1)
#         list_frame.place(x=20, y=130, width=1326, height=580)
#         current_widgets.append(list_frame)

#         canvas = Canvas(list_frame, bg="white", highlightthickness=0)
#         scrollbar = Scrollbar(list_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = Frame(canvas, bg="white")

#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )

#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)

#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")

#         cursor.execute("SELECT student_id, name, username, phonenumber, emailid, course, academic_year, semester, status FROM students")
#         students = cursor.fetchall()

#         if not students:
#             lbl_no = Label(scrollable_frame, text="No registered students found.", fg=text_muted, bg="white", font=("Segoe UI", 14, "bold"))
#             lbl_no.pack(pady=100, padx=420)
#         else:
#             # Table Header
#             header_row = Frame(scrollable_frame, bg=table_bg)
#             header_row.pack(fill="x", expand=True, pady=(10, 5))

#             Label(header_row, text="Student ID", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=10, anchor="w").grid(row=0, column=0, padx=5, pady=10)
#             Label(header_row, text="Name", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=15, anchor="w").grid(row=0, column=1, padx=5, pady=10)
#             Label(header_row, text="Username", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=15, anchor="w").grid(row=0, column=2, padx=5, pady=10)
#             Label(header_row, text="Phone", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=12, anchor="w").grid(row=0, column=3, padx=5, pady=10)
#             Label(header_row, text="Email ID", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=18, anchor="w").grid(row=0, column=4, padx=5, pady=10)
#             Label(header_row, text="Course", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=10, anchor="w").grid(row=0, column=5, padx=5, pady=10)
#             Label(header_row, text="Academic Yr", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=10, anchor="w").grid(row=0, column=6, padx=5, pady=10)
#             Label(header_row, text="Semester", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=7, anchor="w").grid(row=0, column=7, padx=5, pady=10)
#             Label(header_row, text="Status", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=10, anchor="w").grid(row=0, column=8, padx=5, pady=10)
#             Label(header_row, text="Actions", font=("Segoe UI", 10, "bold"), fg=text_dark, bg=table_bg, width=20).grid(row=0, column=9, columnspan=2, padx=5, pady=10)

#             for s in students:
#                 s_id, name, username, phone, email, course, year, sem, status = s

#                 row_frame = Frame(scrollable_frame, bg="white", bd=1, highlightbackground="#e2e8f0", highlightthickness=1)
#                 row_frame.pack(fill="x", expand=True, pady=5)

#                 Label(row_frame, text=s_id, font=("Segoe UI", 9), fg=text_dark, bg="white", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=10)
#                 Label(row_frame, text=name, font=("Segoe UI", 9), fg=text_dark, bg="white", width=15, anchor="w").grid(row=0, column=1, padx=5, pady=10)
#                 Label(row_frame, text=username, font=("Segoe UI", 9), fg=text_dark, bg="white", width=15, anchor="w").grid(row=0, column=2, padx=5, pady=10)
#                 Label(row_frame, text=phone, font=("Segoe UI", 9), fg=text_dark, bg="white", width=12, anchor="w").grid(row=0, column=3, padx=5, pady=10)
#                 Label(row_frame, text=email, font=("Segoe UI", 9), fg=text_dark, bg="white", width=18, anchor="w").grid(row=0, column=4, padx=5, pady=10)
#                 Label(row_frame, text=course, font=("Segoe UI", 9), fg=text_dark, bg="white", width=10, anchor="w").grid(row=0, column=5, padx=5, pady=10)
#                 Label(row_frame, text=year, font=("Segoe UI", 9), fg=text_dark, bg="white", width=10, anchor="w").grid(row=0, column=6, padx=5, pady=10)
#                 Label(row_frame, text=sem, font=("Segoe UI", 9), fg=text_dark, bg="white", width=7, anchor="w").grid(row=0, column=7, padx=5, pady=10)

#                 status_color = "#d97706" if status == "Pending" else "#059669"
#                 Label(row_frame, text=status, font=("Segoe UI", 9, "bold"), fg=status_color, bg="white", width=10, anchor="w").grid(row=0, column=8, padx=5, pady=10)

#                 btn_accept = Button(row_frame, text="Accept", fg="white", bg="#10b981", activebackground="#059669", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2",
#                                     command=lambda sid=s_id: accept_student(sid))
#                 btn_accept.grid(row=0, column=9, padx=3, pady=10, ipadx=8, ipady=3)

#                 if status == "Accepted":
#                     btn_accept.configure(state="disabled", bg="#e2e8f0", fg="#94a3b8", text="Accepted")

#                 btn_delete = Button(row_frame, text="Delete", fg="white", bg="#ef4444", activebackground="#dc2626", font=("Segoe UI", 8, "bold"), bd=0, cursor="hand2",
#                                     command=lambda sid=s_id: delete_student(sid))
#                 btn_delete.grid(row=0, column=10, padx=3, pady=10, ipadx=8, ipady=3)

#     def show_academic_fee():
#         clear_screen()
#         setup_header()

#         # Back Button
#         btn_back = Button(root, text="← BACK", fg="white", bg="#475569", activebackground="#334155", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=show_dashboard)
#         btn_back.place(x=30, y=80, width=100, height=35)
#         current_widgets.append(btn_back)

#         lbl_title = Label(root, text="ACADEMIC FEE STATUS CONTROL", fg=text_dark, bg="white", font=("Segoe UI", 20, "bold"))
#         lbl_title.place(x=480, y=80)
#         current_widgets.append(lbl_title)

#         # Main Table Container Card
#         list_shadow = Frame(root, bg=bg_shadow, bd=0)
#         list_shadow.place(x=56, y=136, width=1266, height=580)
#         fee_frame = Frame(root, bg="white", bd=0, highlightbackground="#cbd5e1", highlightthickness=1)
#         fee_frame.place(x=50, y=130, width=1266, height=580)
#         current_widgets.append(fee_frame)

#         lbl_info = Label(fee_frame, text="ACADEMIC PAYMENT RECORDS MODULE", fg=accent_blue, bg="white", font=("Segoe UI", 18, "bold"))
#         lbl_info.pack(pady=(120, 10))

#         lbl_desc = Label(fee_frame, text="Review pending academic payments, print invoices,\nand log manually received fees.", fg=text_muted, bg="white", font=("Segoe UI", 12))
#         lbl_desc.pack(pady=10)

#     # Start by showing the dashboard
#     show_dashboard()

#     root.mainloop()