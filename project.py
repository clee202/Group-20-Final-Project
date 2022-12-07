import tkinter
import sys
from tkinter import *

#creates a window for the login page
window = tkinter.Tk()

#create login page title and size
window.title("Login Page")
window.geometry('330x200')

#function used to validate login credentials
def login():
    if username_entry.get() == "u" and password_entry.get() == "p":

        #Quits the login page
        window.destroy()

        #Opens a new frame with the address book page
        frame = tkinter.Tk()
        
        frame.title("Address Book")
        frame.geometry('320x310')

        #Contacts label above the contact listbox
        name_label = tkinter.Label(frame, text = "Contacts" )
        name_label.place(x = 205)

        #contact list containing all of the data
        contacts = [
                ['john smith','123-123-1234','johnsmith@gmail.com'], 
                ['jane doe','321-321-3210', 'jdoe@gmail.com'] 
                ] 

        #displays the name of each person in the contacs
        def listbox():
            listbox = Listbox(frame, width=25, height= 15, selectmode=SINGLE)
            listbox.place(x= 155, y = 20)

            for names in contacts:
                listbox.insert(0, (names[0]))

        listbox()

        def add():
            frame2 = tkinter.Tk()
            frame2.title("Add contact")
            frame2.geometry("300x170")

            name_label = tkinter.Label(frame2, text = "Name: ")
            name_label.place(x = 20, y = 15)
            name_entry = tkinter.Entry(frame2)
            name_entry.place(x = 130, y = 15)

            phone_label = tkinter.Label(frame2, text = "Phone Number: ")
            phone_label.place(x = 20, y = 50)
            phone_entry = tkinter.Entry(frame2)
            phone_entry.place(x = 130, y = 50)
          
            email_label = tkinter.Label(frame2, text = "email: ")
            email_label.place(x = 20, y = 85)
            email_entry = tkinter.Entry(frame2)
            email_entry.place(x = 130, y = 85)
            
            #needs command to add the contact to the contacts list
            add_contact = tkinter.Button(frame2, text = "Add", width = 12)
            add_contact.place(x=175, y = 130)

        def view():
            #needs to show contact information based on the selection made on the listbox
            frame3 = tkinter.Tk()
            frame3.title("Contact information")
            frame3.geometry("300x170")

            name_label = tkinter.Label(frame3, text = "Name: ")
            name_label.place(x = 20, y = 15)

            phone_label = tkinter.Label(frame3, text = "Phone Number: ")
            phone_label.place(x = 20, y = 50)
            
            email_label = tkinter.Label(frame3, text = "email: ")
            email_label.place(x = 20, y = 85)
           

        #adds a new contact
        add_button = tkinter.Button(frame, text = "Add", width = 12, command = add)
        add_button.place(x=30, y = 25)

        #deletes a contact 
        #needs delete command
        delete_button = tkinter.Button(frame, text = "Delete", width = 12)
        delete_button.place(x=30, y = 75)

        #updates a contact with new information
        #needs update command
        update_button = tkinter.Button(frame, text = "Update", width = 12)
        update_button.place(x = 30, y = 125)

        #views the contacts information
        #needs view command
        view_button = tkinter.Button(frame, text = "View", width = 12, command=view)
        view_button.place(x = 30, y = 175)

        #quits program
        quit_button = tkinter.Button(frame, text = "Quit", width = 12, command = frame.destroy)
        quit_button.place(x=30, y = 225)

    else:
        error_page()

def error_page():
    #creates a new error page
    window2 = tkinter.Tk()

    #creates an error title and size
    window2.title("Try again")
    window2.geometry('300x180')

    #Shows an error message and asks the user to try again
    error_message = tkinter.Label(window2, text = "Wrong Username or Password.\n Try again.").pack()

    #ok button closes the error window and returns to the login page
    ok_button= tkinter.Button(window2, text = "Ok", command= window2.destroy).pack()

#Creates a login label 
login_label = tkinter.Label(window, text = "INST326 Group Project Login Page", font=(35))
login_label.grid(row=0, column=0, columnspan=2, sticky = "news", pady = 20)

#creates a label named username and an entry box for the username
username_label = tkinter.Label(window, text = "Username")
username_label.grid(row=1, column=0)
username_entry = tkinter.Entry(window)
username_entry.grid(row=1, column=1)

#creates a label named password and an entry box for the password
password_label = tkinter.Label(window, text = "Password")
password_label.grid(row=2, column=0)
password_entry = tkinter.Entry(window, show = "*")
password_entry.grid(row=2, column=1)

#create a login button to allow access to the address book
login_button = tkinter.Button(window, text = "Login", command= login)
login_button.grid(row = 3, column = 0, columnspan = 2, pady = 20)

#needed to run the tkinter program
window.mainloop()