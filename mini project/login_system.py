from tkinter import *
from tkinter import messagebox
import ast
import os

loggedin_username = None
loggedin_password = None
user_dict = {}

# Get the username/password list as dictionary from datasheet.txt
def get_user_pwd_list():
    global user_dict
    try:
        file = open('datasheet.txt', 'r+')
        data = file.read()
        user_dict = ast.literal_eval(data)#coverts string data into dictionary
    except:
        print('No user credential file available...')
        user_dict = {}
    print(str(user_dict))
    return user_dict

# Update user_dict into datasheet.txt
def update_new_user_data():
    global user_dict
    try:
        file = open('datasheet.txt', 'w')
        pp = str(user_dict)
        file.write(pp)
        file.close()
    except:
        print('User credential file not found!!!')

# Returns True if username available in user_dict which is globally declared or returns False 
def user_available(user_name):
    global user_dict
    if bool(user_dict):
        return user_name in user_dict.keys()
    else:
        return False

#collect values for username, password and confirm password
def signup():
    signup_username = signup_user_input.get()
    signup_pwd = signup_pwd_input.get()
    signup_confirm_pwd = signup_confirm_pwd_input.get()

    if not user_available(signup_username):
        if signup_pwd == signup_confirm_pwd:
            # Add signed up user credential to user_dict
            user_dict[signup_username] = signup_pwd
            update_new_user_data()
            messagebox.showinfo("Signup", "User Successfully Signed up. Redirecting to Login page!")
            show_login()
        else:
            messagebox.showerror('Login Error', 'Password and Confirm Password are not matching. Both should match.')
    else:
        messagebox.showerror('Login Error', 'Username already exists!')

def show_login():
    window.withdraw()  # hide the signup window
    login_window.deiconify()  # show the login window

# Validate user credential against user_dict
def valid_user_pwd():
    global user_dict
    loggedin_username = login_user_input.get()
    loggedin_password = login_pwd_input.get()

    if loggedin_username in user_dict.keys():
        if user_dict[loggedin_username] == loggedin_password:
            return True
        else:
            messagebox.showerror('Invalid user credential', 'Invalid password for the user.')
            return False
    else:
        messagebox.showerror('Invalid user credential', 'Invalid user.')
        return False

def goto_pp():
    if valid_user_pwd():
        os.system('python pp.py')

# Get user credential from datasheet.txt and store it in user_dict atvery first of the program running 
get_user_pwd_list()

# Signup Window
window = Tk()
window.title('Signup')
window.state('zoomed')  # Start the window in a maximized state
window.configure(bg="#fff")
window.resizable(True,True)#allows to resize the window

img = PhotoImage(file='login.png')
Label(window, image=img, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
heading.place(x=100, y=5)

signup_user_input = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
signup_user_input.place(x=30, y=80)
signup_user_input.insert(0, 'Username')
signup_user_input.bind('<FocusIn>', lambda e: signup_user_input.delete(0, 'end'))
signup_user_input.bind('<FocusOut>', lambda e: signup_user_input.insert(0, 'Username') if not signup_user_input.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

signup_pwd_input = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11), show='*')
signup_pwd_input.place(x=30, y=150)
signup_pwd_input.insert(0, 'Password')
signup_pwd_input.bind('<FocusIn>', lambda e: signup_pwd_input.delete(0, 'end'))
signup_pwd_input.bind('<FocusOut>', lambda e: signup_pwd_input.insert(0, 'Password') if not signup_pwd_input.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

signup_confirm_pwd_input = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11),
                     show='*')
signup_confirm_pwd_input.place(x=30, y=220)
signup_confirm_pwd_input.insert(0, 'Confirm Password')
signup_confirm_pwd_input.bind('<FocusIn>', lambda e: signup_confirm_pwd_input.delete(0, 'end'))
signup_confirm_pwd_input.bind('<FocusOut>', lambda e: signup_confirm_pwd_input.insert(0, 'Confirm Password') if not signup_confirm_pwd_input.get() else None)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text="Already have an account?", fg='black', bg='white',
              font=("Microsoft YaHei UI Light", 9))
label.place(x=50, y=340)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_login)
signin.place(x=200, y=340)

# Login Window
login_window = Toplevel(window)
login_window.title('Login')
login_window.configure(bg="#fff")
login_window.resizable(True, True)
login_window.withdraw()  # hide login window initially
login_window.state('zoomed')  # Maximize the window on Windows


img_login = PhotoImage(file='login.png')
Label(login_window, image=img_login, bg='white').place(x=50, y=50)

frame_login = Frame(login_window, width=350, height=350, bg="white")
frame_login.place(x=480, y=70)

heading_login = Label(frame_login, text='Sign in', fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
heading_login.place(x=100, y=5)

def on_enter_login_user(e):
    login_user_input.delete(0, 'end')
def on_leave_login_user(e):
    name = login_user_input.get()
    if name == '':
        login_user_input.insert(0, 'Username')

login_user_input = Entry(frame_login, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
login_user_input.place(x=30, y=80)
login_user_input.insert(0, 'Username')
login_user_input.bind('<FocusIn>', on_enter_login_user)
login_user_input.bind('<FocusOut>', on_leave_login_user)

Frame(frame_login, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter_login_pwd(e):
    login_pwd_input.delete(0, 'end')
def on_leave_login_pwd(e):
    name = login_pwd_input.get()
    if name == '':
        login_pwd_input.insert(0, 'Password')

login_pwd_input = Entry(frame_login, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11), show='*')
login_pwd_input.place(x=30, y=150)
login_pwd_input.insert(0, 'Password')
login_pwd_input.bind('<FocusIn>', on_enter_login_pwd)
login_pwd_input.bind('<FocusOut>', on_leave_login_pwd)

Frame(frame_login, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame_login, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=goto_pp).place(x=35, y=204)
login_label = Label(frame_login, text="Don't have an account?", fg='black', bg='white',
                    font=("Microsoft YaHei UI Light", 9))
login_label.place(x=75, y=270)

login_signup = Button(frame_login, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                      command=show_login)
login_signup.place(x=215, y=270)

window.mainloop()
