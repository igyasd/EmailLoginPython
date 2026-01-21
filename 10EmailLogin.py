from tkinter import *

window = Tk()
window.title("Login by Vaggos")
window.geometry("420x300")
window.resizable(False, False)

top_frame = Frame(window, bg="#3A6EA5", height=60)
top_frame.pack(fill="x")

Label(top_frame, text="Welcome to Windows XP", bg="#3A6EA5", fg="white",
      font=("Tahoma", 14, "bold")).place(x=120, y=15)

main_frame = Frame(window, bg="#ECE9D8")
main_frame.pack(fill="both", expand=True)

Label(main_frame, text="Username:", bg="#ECE9D8", fg="black", font=("Tahoma", 10)).place(x=60, y=60)
Label(main_frame, text="Password:", bg="#ECE9D8", fg="black", font=("Tahoma", 10)).place(x=60, y=100)
Label(main_frame, text="Email:", bg="#ECE9D8", fg="black", font=("Tahoma", 10)).place(x=60, y=140)

username_entry = Entry(main_frame, width=22, font=("Tahoma", 10))
username_entry.place(x=150, y=60)
password_entry = Entry(main_frame, width=22, show="*", font=("Tahoma", 10))
password_entry.place(x=150, y=100)
email_entry = Entry(main_frame, width=22, font=("Tahoma", 10))
email_entry.place(x=150, y=140)

def Login():
    Name = username_entry.get()
    Pass = password_entry.get()
    Email = email_entry.get()
    if Name == "Guest" and Pass == "1234" and Email == "Guest@gmail.com":
        welcome_window = Toplevel(window)
        welcome_window.title("Welcome")
        welcome_window.geometry("300x150")
        welcome_window.configure(bg="#ECE9D8")
        Label(welcome_window, text=f"Welcome, {Name}!", font=("Tahoma", 12, "bold"),
              bg="#ECE9D8", fg="black").pack(expand=True)
    else:
        error_label.config(text="Invalid credentials!", fg="red")

btn = Button(main_frame, text="Log in", width=12, font=("Tahoma", 10), command=Login)
btn.place(x=160, y=185)

error_label = Label(main_frame, text="", bg="#ECE9D8")
error_label.place(x=160, y=215)

window.mainloop()
