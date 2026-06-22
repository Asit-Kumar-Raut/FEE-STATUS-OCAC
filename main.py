#conection of python programme with mysql
from tkinter import *
from PIL import Image, ImageTk
import admin_register
import consiler_register
import student_register

def admin_registerpage():
    root.destroy()
    admin_register.main()  # call function from admin register _page.py

def conciler_registerpage():
    root.destroy()
    consiler_register.main()

def student_registerpage():
    root.destroy()
    student_register.main()
    


def main():
    global root
    root = Tk()
    root.title("Fee-status-manager")
    root.geometry("1366x768+0+0")
    root.resizable(False,False)  # This disables both width and height resizing

    #BACKGROUND IMAGE 
    #Use forward slashes to avoid accidental escape sequences in the string
    bg = Image.open(r"images\Gemini_Generated_Image_5h883b5h883b5h88.png")
    background_photo = ImageTk.PhotoImage(bg)
    background_label = Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # TITLE LABEL
    title_label = Label(root, text="choose your role ", fg="#1e293b", font=("Helvetica", 28, "bold"))
    title_label.place(x=515, y=120)

    # Vertical Buttons (Larger sizing and centered under the title)
    btn = Button(root, text="continue as admin", fg="red", bg="#00d5ff", font=("Arial", 14, "bold"), bd=0, cursor="hand2",command=admin_registerpage)
    btn.place(x=483, y=240, width=400, height=65)

    btn1=Button(root,text="continue as counsiler",fg="black",bg="red",font=("Arial",14, "bold"), bd=0, cursor="hand2",command=conciler_registerpage)
    btn1.place(x=483, y=340, width=400, height=65)

    btn2 = Button(root, text="countinue as student", fg="red", bg="yellow", font=("Arial", 14, "bold"), bd=0, cursor="hand2",command=student_registerpage)
    btn2.place(x=483, y=440, width=400, height=65)

    root.mainloop()
main()