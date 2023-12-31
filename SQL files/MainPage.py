import time
def Login_Register():
    print(" \033[1mThis is bold text\033[0m")
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
    print("+==================================+")
    print("|             "+"\033[3mLOGIN\033[0m","               |")
    print("|             "+"\033[3mRegister\033[0m","            |")
    print("|             "+"\033[3mQuit\033[0m","                |")
    print("+==================================+")

    print("\033[2mEnter Login or Register or Quit:\033[0m ")

    
#def LoginPage():
def show_loading_page(message, dots=4, delay=0.5):
    print(message, end='', flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print('.', end='', flush=True)
    print()

Login_Register()
choice = input()
choice =choice.lower()

if (choice == "login"):
    show_loading_page(f"Loading Login page", dots=5, delay=0.5)