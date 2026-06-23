from tkinter import *
from PIL import Image, ImageTk

def admin_registerpage():
    root.destroy()
    from admin import admin_register
    admin_register.main()

def conciler_registerpage():
    root.destroy()
    from counsiler import consiler_register
    consiler_register.main()

def student_registerpage():
    root.destroy()
    from student import student_register
    student_register.main()

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
    bg = Image.open(r"images\WhatsApp Image 2026-06-23 at 11.19.09 AM.jpeg")
    img = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(img)

    # CANVAS FOR TRUE TRANSPARENT LABELS
    canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor=NW)
    canvas.image = background_photo

    # TITLE LABEL (Drawn directly on canvas for 100% transparent background)

    # CENTRAL OPTIONS CARD SHADOW & FRAME
    card_shadow = Frame(root, bg=bg_shadow, bd=0)
    canvas.create_window(689, 406, window=card_shadow, width=480, height=380)

    card = Frame(root, bg=card_color, bd=0, padx=40, pady=30, highlightbackground="#1e293b", highlightthickness=1)
    canvas.create_window(683, 400, window=card, width=480, height=380)

    Label(card, text="Role Selection", font=("Segoe UI", 15, "bold"), fg=text_color, bg=card_color).pack(pady=(0, 3))
    Label(card, text="Please select your credential profile", font=("Segoe UI", 10), fg=text_muted, bg=card_color).pack(pady=(0, 20))

    # ADMIN BUTTON (Blue Accent)
    btn_admin = Button(card, text="Admin→", fg="white", bg="#3b82f6", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=admin_registerpage)
    btn_admin.pack(pady=10, ipady=12, fill=X)

    # COUNSELOR BUTTON (Purple Accent)
    btn_counselor = Button(card, text="Counselor→", fg="white", bg="#8b5cf6", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=conciler_registerpage)
    btn_counselor.pack(pady=10, ipady=12, fill=X)

    # STUDENT BUTTON (Teal Accent)
    btn_student = Button(card, text="Student→", fg="white", bg="#0d9488", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=student_registerpage)
    btn_student.pack(pady=10, ipady=12, fill=X)

    # TEAM MEMBERS WIDGET (Drawn directly on canvas for 100% transparent background)
    team_text = ( "🌟 DEVELOPMENT TEAM\n""• ASIT KUMAR RAUT (Team Leader)\n""• BISHWA PRAKASH ROUT\n""• AKASH KUMAR SWAIN\n""• ADITYA KUMAR SAHOO")
    canvas.create_text(1336, 710, text=team_text, fill="#ffffff", font=("Segoe UI", 11, "bold"), anchor=SE, justify=LEFT)


    root.mainloop()

if __name__ == "__main__":
    main()
