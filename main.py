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

    # BACKGROUND IMAGE
    bg = Image.open(r"images\WhatsApp Image 2026-06-23 at 11.19.09 AM.jpeg")
    img = bg.resize((1366, 768), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(img)
    
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # CENTRAL CREDITS CARD
    card = Frame(root, bg="#0f172a", bd=1, highlightbackground="#1e293b", highlightthickness=1)
    card.place(x=443, y=190, width=480, height=380)


    Label(card, text="🌟 SYSTEM DEVELOPED BY 🌟", fg="#f59e0b", bg="#0f172a", font=("Segoe UI", 15, "bold")).pack(pady=(20, 10))
    Label(card, text="ASIT KUMAR RAUT\n(Team Leader)", fg="#10b981", bg="#0f172a", font=("Segoe UI", 16, "bold"), justify=CENTER).pack(pady=10)
    Label(card, text="BISHWA PRAKASH ROUT", fg="#f8fafc", bg="#0f172a", font=("Segoe UI", 13, "bold")).pack(pady=5)
    Label(card, text="AKASH KUMAR SWAIN", fg="#f8fafc", bg="#0f172a", font=("Segoe UI", 13, "bold")).pack(pady=5)
    Label(card, text="ADITYA KUMAR SAHOO", fg="#f8fafc", bg="#0f172a", font=("Segoe UI", 13, "bold")).pack(pady=5)


    # PROCEED BUTTON
    btn_proceed = Button(card, text="PROCEED  →", fg="white", bg="#059669", font=("Segoe UI", 12, "bold"), bd=0, cursor="hand2", command=launch_home)
    btn_proceed.pack(pady=15, ipady=10, fill=X, padx=40)

    root.mainloop()




if __name__ == "__main__":
    main()