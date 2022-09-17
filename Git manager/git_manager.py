from colorama import Fore, Style
from generate_ssh_key import generate_ssh_key
from generate_gpg_key import generate_gpp_key
from ssh_config import configureAccount
from default_config import default


"""
Welcome Message.
"""
def welcome():

    print(Fore.LIGHTCYAN_EX + """**********************************************************
Welcome to gitlab/github ssh and gpg keys manager program

by Murendwa Ratshitimba
**********************************************************
    """)
    default()
    print(Style.RESET_ALL)
    

def commands():

    print(Fore.LIGHTMAGENTA_EX + """\nValid Commands:
    
    1. user - choose the gitlab account
    2. ssh - generate an ssh key
    3. gpg - generate a gpg key
    4. config - configure ssh 
    5. quit - quit the program
    \n""")
    print(Style.RESET_ALL)


def main():

    # welcome the user
    welcome()

    # valid comamands
    commands()

    # choose mode
    while True:

        mode = input(Fore.CYAN + Style.BRIGHT + "\nEnter a valid command: ").lower()

        if mode == "user":

            pass  

        elif mode == "ssh":

            print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
            generate_ssh_key() 
            

        elif mode == "gpg":

            print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
            generate_gpp_key()

        elif mode == "config":

            configureAccount()
    

        elif mode == "quit":

            break

        elif mode == "help":

            commands()
            
        else:

            print(Fore.RED + Style.BRIGHT + "\nInvalid command\n")
            print(Style.RESET_ALL)


if __name__ == "__main__":

    main()