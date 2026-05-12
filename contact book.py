from tkinter import *
from tkinter import messagebox
import csv
def save_data():
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    contact=contact_entry.get()
    email=email_entry.get()
    if first_name=="" or last_name=="" or contact=="" or email=="":
        messagebox.showerror("Error","All Fields Required")
    elif len(contact)!=10:
        messagebox.showerror("Error", "Contact number must be 10 digits")
    elif "@" not in email:
        messagebox.showerror("Error", "Enter valid email")
    else:
        with open("contacts.csv",mode="a" ,newline="") as file:
            writer=csv.writer(file)
            writer.writerow([first_name,last_name,contact,email])
            messagebox.showinfo("Contact Saved successflly")
            first_name_entry.delete(0,END)
            last_name_entry.delete(0,END)
            contact_entry.delete(0,END)
            email_entry.delete(0,END)
root=Tk()
root.title("PhoneBook")
root.geometry("500x450")
heading=Label(root,text="PhoneBook", bg="blue", fg="white" ,font=("Arial",20))
heading.pack(pady=10)
Label(root,text="First Name").pack()
first_name_entry=Entry(root,width=30)
first_name_entry.pack(pady=5)
Label(root,text="Last Name").pack()
last_name_entry=Entry(root,width=30)
last_name_entry.pack(pady=5)
Label(root,text="ContactNumber").pack()
contact_entry=Entry(root,width=30)
contact_entry.pack(pady=5)
Label(root,text="Email").pack()
email_entry=Entry(root,width=30)
email_entry.pack(pady=5)
submit_button=Button(root,text="Submit",command=save_data)
submit_button.pack(pady=20)
root.mainloop()
