import time


#Method to display the login/register page
def login_register():
  
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
    print("+==================================+")
    print("|             "+"\033[3mLOGIN\033[0m","               |")
    print("|             "+"\033[3mRegister\033[0m","            |")
    print("|             "+"\033[3mQuit\033[0m","                |")
    print("+==================================+")

    print("\033[2mEnter Login or Register or Quit:\033[0m ")

#Method for the loading page...
def show_loading_page(message, dots=4, delay=0.5):
    print(message, end='', flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print('.', end='', flush=True)
    print()

login_register()
choice = input()
choice =choice.lower()

#Method to print the login page
def login_page():
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
    print("+==================================+")
    print("\t  UserId:",end="")
    userid = input()
    print("\t  Password:",end="")
    password = input()










if (choice == "login"):
    show_loading_page(f"Loading Login page", dots=5, delay=0.5)
    login_page()
elif(choice == "register"):
    show_loading_page(f"Loading Register page", dots=5, delay=0.5)
elif(choice =="quit"):
    show_loading_page(f"Quiting program", dots=5, delay=0.5)