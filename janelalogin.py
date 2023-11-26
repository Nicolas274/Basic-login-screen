from tkinter import Tk, Button, Frame, Entry, END
import tkinter
import customtkinter
import packaging

        
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


window = customtkinter.CTk()
window.geometry("500x300")


def click():
    print("Hello!")
    
#    
def toogle_password():
    if password.cget('show') == '':
        password.configure(show='*')
    else:
        password.configure(show='')
    

text = customtkinter.CTkLabel(window, text="Login")
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text="E-mail")
email.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(window, placeholder_text="Password", show="*")
password.pack(padx=10, pady=10)

button = customtkinter.CTkCheckBox(window, text="Show password", command=toogle_password)
button.pack(padx=10, pady=5)


button = customtkinter.CTkButton(window, text="Login", command=click)
button.pack(padx=10, pady=10)



window.mainloop()