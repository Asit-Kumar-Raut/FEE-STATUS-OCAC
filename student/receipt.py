import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import db

def main(student_id="101", role="student", caller_name="Caller Name", caller_id="1"):
    root = Tk()
    root.title("Fee Payment Receipts")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    bg_color = "#f8fafc"
    root.config(bg=bg_color)

    student_info = db.get_student(student_id)

    if not student_info:
        messagebox.showerror("Error", f"Student with ID {student_id} not found!")
        root.destroy()
        return

    s_name = student_info.get("name", "")
    course = student_info.get("course", "")
    semester = student_info.get("semester", "")
    total_fee = student_info.get("total_fee", 100000)
    paid_amount = student_info.get("paid_amount", 0)
    pending_amount = student_info.get("pending_amount", 100000)
    college_name = student_info.get("college_name", "College")

    def back_action():
        root.destroy()
        if role == "student":
            from student import studentdash_board
            studentdash_board.main(s_name, student_id)
        elif role == "admin":
            from admin import admin_student_fee
            # Re-routing back using college_name and college_id which are passed as caller_name/caller_id
            admin_student_fee.main(caller_name, caller_id, student_id)
        elif role == "counselor":
            from counsiler import counciler_student
            counciler_student.main(caller_name, caller_id, student_id)

    header_frame = Frame(root, bg="#1e293b")
    header_frame.place(x=0, y=0, width=1366, height=60)

    lbl_title = Label(header_frame, text="🧾 FEE PAYMENT RECEIPTS", fg="#f8fafc", bg="#1e293b", font=("Segoe UI", 14, "bold"))
    lbl_title.place(x=30, y=15)

    btn_back = Button(header_frame, text="← BACK", fg="white", bg="#475569", activebackground="#334155", activeforeground="white", font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2", command=back_action)
    btn_back.place(x=1200, y=12, width=100, height=35)
    btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#334155"))
    btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#475569"))

    details_card = Frame(root, bg="white", bd=1, relief=SOLID, highlightthickness=0)
    details_card.place(x=50, y=90, width=1266, height=100)

    border_left = Frame(details_card, bg="#3b82f6", width=5)
    border_left.pack(side=LEFT, fill=Y)

    Label(details_card, text=f"Student Name: {s_name}", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg="white").place(x=20, y=20)
    Label(details_card, text=f"Student ID: {student_id}  |  College: {college_name}", font=("Segoe UI", 11), fg="#475569", bg="white").place(x=20, y=55)

    Label(details_card, text=f"Course: {course}", font=("Segoe UI", 11, "bold"), fg="#1e293b", bg="white").place(x=450, y=20)
    Label(details_card, text=f"Semester: {semester}", font=("Segoe UI", 11), fg="#475569", bg="white").place(x=450, y=55)

    Label(details_card, text=f"Total Fee: ₹ {total_fee:,}", font=("Segoe UI", 11, "bold"), fg="#0d9488", bg="white").place(x=850, y=20)
    Label(details_card, text=f"Paid Amount: ₹ {paid_amount:,}   |   Pending Amount: ₹ {pending_amount:,}", font=("Segoe UI", 11), fg="#e11d48", bg="white").place(x=850, y=55)

    lbl_table = Label(root, text="PAYMENT HISTORY LOG", font=("Segoe UI", 12, "bold"), fg="#1e293b", bg=bg_color)
    lbl_table.place(x=50, y=215)

    table_frame = Frame(root, bg="white", bd=1, relief=SOLID)
    table_frame.place(x=50, y=245, width=1266, height=370)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="#0f172a",
                    rowheight=35,
                    fieldbackground="white",
                    font=("Segoe UI", 10))
    style.map("Treeview", background=[("selected", "#dbeafe")], foreground=[("selected", "#1e40af")])
    style.configure("Treeview.Heading",
                    background="#f1f5f9",
                    foreground="#475569",
                    font=("Segoe UI", 10, "bold"),
                    rowheight=35)

    cols = ("Payment ID", "Amount Paid", "Payment Mode", "UTR Number", "Date & Time")
    tree = ttk.Treeview(table_frame, columns=cols, show="headings", style="Treeview")
    
    tree.column("Payment ID", width=220, anchor=CENTER)
    tree.column("Amount Paid", width=180, anchor=E)
    tree.column("Payment Mode", width=150, anchor=CENTER)
    tree.column("UTR Number", width=220, anchor=W)
    tree.column("Date & Time", width=250, anchor=CENTER)

    for col in cols:
        tree.heading(col, text=col)

    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    payments = db.get_payments(student_id)

    if not payments:
        tree.insert("", "end", values=("N/A", "₹ 0", "No Payments", "-", "No history found"))
    else:
        for p in payments:
            pid = p.get("payment_id", "")
            amount = p.get("amount", 0)
            mode = p.get("mode", "")
            utr = p.get("utr_number", "")
            p_date = p.get("payment_date", "")
            utr_display = utr if utr else "-"
            # Formatting timestamp
            if "T" in p_date:
                p_date = p_date.replace("T", " ")[:19]
            amt_str = f"₹ {amount:,}"
            tree.insert("", "end", values=(pid, amt_str, mode, utr_display, p_date))

    def download_selected_receipt():
        import datetime
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors

        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a payment from the history log to download receipt!😟")
            return
            
        values = tree.item(selected_item, "values")
        pid, amount, mode, utr, p_date = values
        
        if pid == "N/A":
            messagebox.showerror("Error", "No valid payment record selected!😟")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")],
            initialfile=f"Receipt_{pid}.pdf",
            title="Save Payment Receipt"
        )
        
        if not file_path:
            return
            
        try:
            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter # 612 x 792
            
            # Draw header band (dark slate blue)
            c.setFillColor(colors.HexColor("#1e293b"))
            c.rect(0, height - 80, width, 80, fill=True, stroke=False)
            
            # Title text
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(width / 2.0, height - 48, "FEE PAYMENT RECEIPT")
            
            # Decorative teal accent bar
            c.setFillColor(colors.HexColor("#0d9488"))
            c.rect(0, height - 85, width, 5, fill=True, stroke=False)
            
            # Reset fill color
            c.setFillColor(colors.black)
            
            # College header details
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, height - 130, str(college_name).upper())
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.HexColor("#475569"))
            c.drawString(50, height - 145, "Official Payment Confirmation Document")
            
            # Horizontal divider
            c.setStrokeColor(colors.HexColor("#e2e8f0"))
            c.setLineWidth(1)
            c.line(50, height - 160, width - 50, height - 160)
            
            # Student Details Header
            c.setFillColor(colors.HexColor("#1e293b"))
            c.setFont("Helvetica-Bold", 11)
            c.drawString(50, height - 185, "STUDENT DETAILS")
            
            # Student fields
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(colors.HexColor("#475569"))
            c.drawString(50, height - 210, "Student Name:")
            c.drawString(50, height - 235, "Student ID:")
            c.drawString(50, height - 260, "Course:")
            c.drawString(50, height - 285, "Semester:")
            
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)
            c.drawString(160, height - 210, str(s_name))
            c.drawString(160, height - 235, str(student_id))
            c.drawString(160, height - 260, str(course))
            c.drawString(160, height - 285, str(semester))
            
            # Divider
            c.setStrokeColor(colors.HexColor("#e2e8f0"))
            c.line(50, height - 310, width - 50, height - 310)
            
            # Payment Details Header
            c.setFillColor(colors.HexColor("#1e293b"))
            c.setFont("Helvetica-Bold", 11)
            c.drawString(50, height - 335, "PAYMENT INFORMATION")
            
            # Payment fields
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(colors.HexColor("#475569"))
            c.drawString(50, height - 360, "Payment ID:")
            c.drawString(50, height - 385, "Payment Mode:")
            c.drawString(50, height - 410, "UTR / Ref No:")
            c.drawString(50, height - 435, "Date & Time:")
            c.drawString(50, height - 460, "Amount Paid:")
            
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.black)
            c.drawString(160, height - 360, str(pid))
            c.drawString(160, height - 385, str(mode))
            c.drawString(160, height - 410, str(utr))
            c.drawString(160, height - 435, str(p_date))
            
            # Highlight amount paid
            c.setFont("Helvetica-Bold", 11)
            c.setFillColor(colors.HexColor("#0d9488"))
            c.drawString(160, height - 460, str(amount))
            
            # Divider
            c.setStrokeColor(colors.HexColor("#e2e8f0"))
            c.line(50, height - 485, width - 50, height - 485)
            
            # Payment Status Badge
            c.setFillColor(colors.HexColor("#10b981")) # Emerald Green
            c.rect(50, height - 530, 120, 30, fill=True, stroke=False)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(110, height - 518, "SUCCESSFUL")
            
            # Footer disclaimer
            c.setFillColor(colors.HexColor("#94a3b8"))
            c.setFont("Helvetica-Oblique", 9)
            c.drawString(50, 100, "This is a computer-generated confirmation receipt. No manual signature is required.")
            c.drawString(50, 85, f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Signatory line
            c.setStrokeColor(colors.HexColor("#1e293b"))
            c.setLineWidth(1.5)
            c.line(width - 200, 130, width - 50, 130)
            c.setFillColor(colors.HexColor("#1e293b"))
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(width - 125, 115, "Authorized Signatory")
            
            # Border frame
            c.setStrokeColor(colors.HexColor("#cbd5e1"))
            c.setLineWidth(1)
            c.rect(20, 20, width - 40, height - 40, fill=False, stroke=True)
            
            c.save()
            messagebox.showinfo("Success", f"Receipt PDF downloaded successfully:\n{file_path} 👍")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF receipt:\n{e}")

    btn_download = Button(root, text="📥 DOWNLOAD SELECTED RECEIPT (PDF)", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 11, "bold"), bd=0, cursor="hand2", command=download_selected_receipt)
    btn_download.place(x=50, y=630, width=320, height=40)

    root.mainloop()

if __name__ == "__main__":
    main()
