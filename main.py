from tkinter import *
from PIL import Image, ImageTk

def launch_home():
    root.destroy()
    import home
    home.main()

def main():
    global root
    root = Tk()
    root.title("Fee Status Manager - Welcome")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)

    # Theme Colors
    text_color = "#f8fafc"
    text_muted = "#94a3b8"

    # Background Image
    bg = Image.open(r"images\WhatsApp Image 2026-06-23 at 11.19.09 AM.jpeg")
    img = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(img)

    # CANVAS FOR TRUE TRANSPARENT LABELS
    canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor=NW)
    canvas.image = background_photo

    # Render Welcome headers directly on canvas
    canvas.create_text(683, 110, text="WELCOME TO", fill=text_muted, font=("Segoe UI", 16, "bold"), anchor=CENTER)
    canvas.create_text(683, 160, text="FEE STATUS MANAGER", fill="#60a5fa", font=("Segoe UI", 32, "bold"), anchor=CENTER)

    # Render credits header directly on canvas
    canvas.create_text(683, 270, text="🌟 SYSTEM DEVELOPED BY 🌟", fill="#f59e0b", font=("Segoe UI", 15, "bold"), anchor=CENTER)

    # Team Members
    canvas.create_text(683, 330, text="ASIT KUMAR RAUT", fill="#10b981", font=("Segoe UI", 18, "bold"), anchor=CENTER)
    canvas.create_text(683, 360, text="(Team Leader)", fill="#10b981", font=("Segoe UI", 11, "italic"), anchor=CENTER)

    canvas.create_text(683, 410, text="BISHWAPRAKASH ROUT", fill=text_color, font=("Segoe UI", 14, "bold"), anchor=CENTER)
    canvas.create_text(683, 445, text="AKASH KUMAR SWAIN", fill=text_color, font=("Segoe UI", 14, "bold"), anchor=CENTER)
    canvas.create_text(683, 480, text="ADITYA KUMAR SAHOO", fill=text_color, font=("Segoe UI", 14, "bold"), anchor=CENTER)

    # PROCEED BUTTON
    btn_proceed = Button(root, text="PROCEED  →", fg="white", bg="#059669", font=("Segoe UI", 14, "bold"), bd=0, cursor="hand2", command=launch_home)
    canvas.create_window(683, 580, window=btn_proceed, width=320, height=52, anchor=CENTER)

    # Foot note
    footer_text = "Fee-Status-Manager © 2026 • Secure & Verified Connections"
    canvas.create_text(683, 730, text=footer_text, fill=text_muted, font=("Segoe UI", 10), anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()
