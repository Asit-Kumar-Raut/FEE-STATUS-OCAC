import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tkinter import *
from PIL import Image, ImageTk
from admin import admin_register
from counsiler import consiler_register
from student import student_register

def admin_registerpage():
    root.destroy()
    admin_register.main()

def conciler_registerpage():
    root.destroy()
    consiler_register.main()

def student_registerpage():
    root.destroy()
    student_register.main()

# Button Hover Animations
def on_enter_blue(e):
    e.widget.config(bg="#2563eb")

def on_leave_blue(e):
    e.widget.config(bg="#3b82f6")

def on_enter_purple(e):
    e.widget.config(bg="#7c3aed")

def on_leave_purple(e):
    e.widget.config(bg="#8b5cf6")

def on_enter_teal(e):
    e.widget.config(bg="#0f766e")

def on_leave_teal(e):
    e.widget.config(bg="#0d9488")

def main():
    global root
    root = Tk()
    root.title("Fee-Status-Manager - Home")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # DESIGN SYSTEM & PALETTE
    bg_shadow = "#020617"       # Dark shadow color
    card_color = "#0f172a"      # Slate 900
    text_color = "#f8fafc"      # Slate 50
    text_muted = "#94a3b8"      # Slate 400

    # BACKGROUND IMAGE
    project_root = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(project_root, "images", "WhatsApp Image 2026-06-23 at 11.19.09 AM.jpeg")
    bg = Image.open(bg_path)
    img = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(img)

    # CANVAS FOR TRUE TRANSPARENT LABELS
    canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor=NW)
    canvas.image = background_photo

    # TITLE LABEL (Drawn directly on canvas for 100% transparent background)
    canvas.create_text(683, 110, text="Choose Your Role", fill="#f8fafc", font=("Segoe UI", 28, "bold"), anchor=CENTER)

    # CENTRAL OPTIONS CARD SHADOW & FRAME
    card_shadow = Frame(root, bg=bg_shadow, bd=0)
    canvas.create_window(689, 406, window=card_shadow, width=480, height=380)

    card = Frame(root, bg=card_color, bd=0, padx=40, pady=30, highlightbackground="#1e293b", highlightthickness=1)
    canvas.create_window(683, 400, window=card, width=480, height=380)

    Label(card, text="Role Selection", font=("Segoe UI", 15, "bold"), fg=text_color, bg=card_color).pack(pady=(0, 3))
    Label(card, text="Please select your credential profile", font=("Segoe UI", 10), fg=text_muted, bg=card_color).pack(pady=(0, 20))

    # ADMIN BUTTON (Blue Accent)
    btn_admin = Button(card, text="Admin Portal  →", fg="white", bg="#3b82f6", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=admin_registerpage)
    btn_admin.pack(pady=10, ipady=12, fill=X)
    btn_admin.bind("<Enter>", on_enter_blue)
    btn_admin.bind("<Leave>", on_leave_blue)

    # COUNSELOR BUTTON (Purple Accent)
    btn_counselor = Button(card, text="Counselor Desk  →", fg="white", bg="#8b5cf6", activebackground="#7c3aed", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=conciler_registerpage)
    btn_counselor.pack(pady=10, ipady=12, fill=X)
    btn_counselor.bind("<Enter>", on_enter_purple)
    btn_counselor.bind("<Leave>", on_leave_purple)

    # STUDENT BUTTON (Teal Accent)
    btn_student = Button(card, text="Student Portal  →", fg="white", bg="#0d9488", activebackground="#0f766e", activeforeground="white", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=student_registerpage)
    btn_student.pack(pady=10, ipady=12, fill=X)
    btn_student.bind("<Enter>", on_enter_teal)
    btn_student.bind("<Leave>", on_leave_teal)

    # TEAM MEMBERS WIDGET (Drawn directly on canvas for 100% transparent background)
    team_text = (
        "🌟 DEVELOPMENT TEAM\n"
        "• ASIT KUMAR RAUT (Team Leader)\n"
        "• BISHWAPRAKASH ROUT\n"
        "• AKASH KUMAR SWAIN\n"
        "• ADITYA KUMAR SAHOO"
    )
    canvas.create_text(1336, 710, text=team_text, fill="#ffffff", font=("Segoe UI", 11, "bold"), anchor=SE, justify=LEFT)

    # FOOTER LABEL
    footer_text = "Fee-Status-Manager © 2026 • Secure & Verified Connections"
    canvas.create_text(683, 730, text=footer_text, fill=text_muted, font=("Segoe UI", 9), anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()
