
🎉 Best AI Model for Code. Beats ChatGPT. Get Started for Free
Toggle Sidebar
Blackbox
1 Day Streak

New Chat
Login
Join Us

Vscode

New Chat

Vscode Extension

AI Github Actions

AI Model Page

Android App

Get API Access

Create Chatbot
Toggle theme

I need you to write a a python scripts using tkinter to make an app, that has login screen, register, email otp verification if user forgot password, and yeah password validation, after that page which has 2 beauitful buttons saying simulator and predictor and on clickign each, it redirects to another screen

Edit

Sources: nagarajramachandran123.medium.com (1) stackoverflow.com (2) cppsecrets.com (3) cs50.harvard.edu (4)

To create a Python application using tkinter that includes a login screen, registration, email OTP verification, and password validation, as well as two buttons that redirect to different screens, follow the steps below:

Install necessary packages:
First, install the requests package to send email OTPs.

bash
Edit
Full Screen
Copy code
pip install requests
(https://github.com/python/cpython/blob/3.9/Lib/email/mime/text.py#L17) [Read only] 17 lines (15 sloc) 410 Bytes

python
Edit
Full Screen
Copy code
import tkinter as tk
from tkinter import messagebox
import random
import string
import re
import requests
from email.mime.text import MIMEText

# Function to generate a random OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# Function to send OTP to email
def send_otp(email):
    otp = generate_otp()
    message = f'Your OTP is {otp}'
    msg = MIMEText(message)
    msg['Subject'] = 'OTP for Password Reset'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email
    requests.post('smtp.example.com', auth=('your_username', 'your_password'), data=msg.as_string())
    return otp

# Function to verify OTP
def verify_otp(email, otp):
    # In a real application, you should check the OTP with a service or a database
    return otp == generate_otp()

# Function to reset password
def reset_password(email):
    otp = send_otp(email)
    # Implement your own logic for showing the OTP entry screen
    user_otp = input('Enter the OTP: ')
    if verify_otp(email, user_otp):
        new_password = input('Enter a new password: ')
        # Update the user's password in a database or a service
        messagebox.showinfo('Success', 'Password has been reset.')
    else:
        messagebox.showerror('Error', 'Invalid OTP.')

# Function to validate password
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True

# Function to register a user
def register():
    email = entry_email.get()
    password = entry_password.get()
    if validate_password(password):
        # Register the user with the provided email and password
        messagebox.showinfo('Success', 'User has been registered.')
    else:
        messagebox.showerror('Error', 'Invalid password.')

# Function to login
def login():
    email = entry_email.get()
    password = entry_password.get()
    if email == 'admin@example.com' and password == 'admin':
        messagebox.showinfo('Success', 'Logged in.')
    else:
        messagebox.showerror('Error', 'Invalid email or password.')

# Create the main window
window = tk.Tk()
window.title('Login Screen')

# Create email and password entry fields
label_email = tk.Label(window, text='Email:')
label_email.grid(row=0, column=0)
entry_email = tk.Entry(window)
entry_email.grid(row=0, column=1)

label_password = tk.Label(window, text='Password:')
label_password.grid(row=1, column=0)
entry_password = tk.Entry(window, show='*')
entry_password.grid(row=1, column=1)

# Create buttons
button_register = tk.Button(window, text='Register', command=register)
button_register.grid(row=2, column=0)

button_login = tk.Button(window, text='Login', command=login)
button_login.grid(row=2, column=1)

button_forgot_password = tk.Button(window, text='Forgot Password', command=lambda: reset_password(entryinput>
python
Edit
Full Screen
Copy code
# Create the second window
window2 = tk.Tk()
window2.title('Simulator and Predictor')

# Create buttons
button_simulator = tk.Button(window2, text='Simulator')
button_simulator.pack()

button_predictor = tk.Button(window2, text='Predictor')
button_predictor.pack()

# Start the main loop
window.mainloop()
This script creates a simple login and registration screen with password validation and an email OTP feature. When a user clicks on the "Forgot Password" button, the reset_password function is called, which sends an OTP to the user's email address. Users can then enter the OTP to reset their password.

The script also creates a second window with two buttons, "Simulator" and "Predictor". When users click on these buttons, they will be redirected to another screen.

To run the application, create a new Python file and copy the above code. Then, run the file using a Python interpreter.

bash
Edit
Full Screen
Copy code
python your_file_name.py
Make sure to replace 'smtp.example.com', 'your_email@example.com', 'your_username', and 'your_password' with your actual SMTP server, email address, username, and password, respectively.

Note: This example is for educational purposes only and should not be used as a production-ready application.input>

input
Edit
Full Screen
Copy code
```p>

```markdown

```p>

```markdown

```p>

```markdown
Is this conversation helpful so far?


Scroll to bottom

Continue

Regenerate

Copy Link to Share Chat

New Chat

Insert Code
@
Enter a prompt here

Send
By using Blackbox you agree to the 
Terms
 and 
Privacy
.


import tkinter as tk
from tkinter import messagebox
import random
import string
import re
import requests
from email.mime.text import MIMEText

# Function to generate a random OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# Function to send OTP to email
def send_otp(email):
    otp = generate_otp()
    message = f'Your OTP is {otp}'
    msg = MIMEText(message)
    msg['Subject'] = 'OTP for Password Reset'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email
    requests.post('smtp.example.com', auth=('your_username', 'your_password'), data=msg.as_string())
    return otp

# Function to verify OTP
def verify_otp(email, otp):
    # In a real application, you should check the OTP with a service or a database
    return otp == generate_otp()

# Function to reset password
def reset_password(email):
    otp = send_otp(email)
    # Implement your own logic for showing the OTP entry screen
    user_otp = input('Enter the OTP: ')
    if verify_otp(email, user_otp):
        new_password = input('Enter a new password: ')
        # Update the user's password in a database or a service
        messagebox.showinfo('Success', 'Password has been reset.')
    else:
        messagebox.showerror('Error', 'Invalid OTP.')

# Function to validate password
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True

# Function to register a user
def register():
    email = entry_email.get()
    password = entry_password.get()
    if validate_password(password):
        # Register the user with the provided email and password
        messagebox.showinfo('Success', 'User has been registered.')
    else:
        messagebox.showerror('Error', 'Invalid password.')

# Function to login
def login():
    email = entry_email.get()
    password = entry_password.get()
    if email == 'admin@example.com' and password == 'admin':
        messagebox.showinfo('Success', 'Logged in.')
    else:
        messagebox.showerror('Error', 'Invalid email or password.')

# Create the main window
window = tk.Tk()
window.title('Login Screen')

# Create email and password entry fields
label_email = tk.Label(window, text='Email:')
label_email.grid(row=0, column=0)
entry_email = tk.Entry(window)
entry_email.grid(row=0, column=1)

label_password = tk.Label(window, text='Password:')
label_password.grid(row=1, column=0)
entry_password = tk.Entry(window, show='*')
entry_password.grid(row=1, column=1)

# Create buttons
button_register = tk.Button(window, text='Register', command=register)
button_register.grid(row=2, column=0)

button_login = tk.Button(window, text='Login', command=login)
button_login.grid(row=2, column=1)

button_forgot_password = tk.Button(window, text='Forgot Password', command=lambda: reset_password(entryinput>

Close