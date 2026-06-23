import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tkinter import *
from PIL import Image, ImageTk

def launch_home():
    root.destroy()
    import home
    home.main()

# Hover Animations
def on_enter_proceed(e):
    e.widget.config(bg="#10b981") # Active green

def on_leave_proceed(e):
    e.widget.config(bg="#059669") # Emerald green

def main():
    global root
    root = Tk()
    root.title("Fee Status Manager - Welcome")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # Theme Colors
    bg_shadow = "#020617"  # Deep shadow
    card_color = "#0f172a" # Slate 900
    text_color = "#f8fafc" # Slate 50
    accent_color = "#3b82f6" # Slate blue border
    text_muted = "#94a3b8"  # Slate 400

    # Background Image
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

    # 3D SHADOW FRAME (Behind card)
    shadow_card = Frame(root, bg=bg_shadow, bd=0)
    canvas.create_window(689, 376, window=shadow_card, width=600, height=540)

    # Large Splash Welcome Card
    splash_card = Frame(root, bg=card_color, highlightbackground=accent_color, highlightthickness=1, padx=40, pady=30)
    canvas.create_window(683, 370, window=splash_card, width=600, height=540)

    # Card Content (labels match card color)
    Label(splash_card, text="WELCOME TO", fg=text_muted, bg=card_color, font=("Segoe UI", 13, "bold")).pack(pady=(10, 2))
    Label(splash_card, text="FEE STATUS MANAGER", fg="#60a5fa", bg=card_color, font=("Segoe UI", 26, "bold")).pack(pady=(0, 20))

    # Dev Team Credits Panel (inside card)
    credit_frame = LabelFrame(splash_card, text=" 🌟 SYSTEM DEVELOPED BY ", fg="#f59e0b", bg=card_color, font=("Segoe UI", 11, "bold"), padx=20, pady=15, bd=1, highlightbackground="#3b82f6", highlightthickness=1)
    credit_frame.pack(fill=X, pady=10)

    Label(credit_frame, text="ASIT KUMAR RAUT", fg="#10b981", bg=card_color, font=("Segoe UI", 13, "bold")).pack(anchor=CENTER, pady=3)
    Label(credit_frame, text="(Team Leader)", fg="#10b981", bg=card_color, font=("Segoe UI", 9, "italic")).pack(anchor=CENTER, pady=(0, 8))
    
    Label(credit_frame, text="BISHWAPRAKASH ROUT", fg=text_color, bg=card_color, font=("Segoe UI", 11, "bold")).pack(anchor=CENTER, pady=3)
    Label(credit_frame, text="AKASH KUMAR SWAIN", fg=text_color, bg=card_color, font=("Segoe UI", 11, "bold")).pack(anchor=CENTER, pady=3)
    Label(credit_frame, text="ADITYA KUMAR SAHOO", fg=text_color, bg=card_color, font=("Segoe UI", 11, "bold")).pack(anchor=CENTER, pady=3)

    # PROCEED BUTTON
    btn_proceed = Button(splash_card, text="PROCEED  →", fg="white", bg="#059669", activebackground="#10b981", activeforeground="white", font=("Segoe UI", 13, "bold"), bd=0, cursor="hand2", command=launch_home)
    btn_proceed.pack(fill=X, ipady=12, pady=(25, 0))
    btn_proceed.bind("<Enter>", on_enter_proceed)
    btn_proceed.bind("<Leave>", on_leave_proceed)

    # Foot note
    footer_text = "Fee-Status-Manager © 2026 • Secure & Verified Connections"
    canvas.create_text(683, 730, text=footer_text, fill=text_muted, font=("Segoe UI", 10), anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()
