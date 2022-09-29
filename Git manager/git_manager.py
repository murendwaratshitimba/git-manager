from colorama import Fore, Style
from generate_ssh_key import generate_ssh_key
from generate_gpg_key import generate_gpp_key
from view_ssh import view_ssh_public_key
from gpg_config import gpg_configuration
from ssh_config import configureAccount
from gitconfig import gitconfig
from view_gpg import view_gpg_public_key
from change_gpg_password import change_gpg_password
from default_config import *
from change_ssh_key_password import change_ssh_key_password


"""
Welcome Message.
"""
def welcome():

    print(Fore.LIGHTCYAN_EX + """**********************************************************
Welcome to gitlab/github ssh and gpg keys manager program

by Murendwa Ratshitimba
**********************************************************
    """)

    default_ssh_directory()
    default()
    print(Style.RESET_ALL)
    

def commands():

    print(Fore.LIGHTMAGENTA_EX + """\nValid Commands:
    
    1. user - choose the gitlab account
    2. ssh - generate an ssh key
    3. gpg - generate a gpg key
    4. config ssh- configure ssh 
    5. config gpg
    6. view ssh - ssh pub key
    7. view gpg - gpg pub key
    8. ssh passwd
    9. gpg passwd
    10. quit - quit the program
    \n""")

    # reset the text color
    print(Style.RESET_ALL)


def main():

    # welcome the user
    welcome()

    # valid comamands
    commands()

    # choose mode
    while True:

        mode = input(Fore.CYAN + Style.BRIGHT + "\nEnter a command: ").lower()

        if mode == "user":

            gitconfig()
            break

        elif mode == "ssh":

            print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
            generate_ssh_key() 
            

        elif mode == "gpg":

            print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
            generate_gpp_key()

        elif mode == "config ssh":

            configureAccount()

        elif mode == "config gpg":

            gpg_configuration()

        elif mode == "view ssh":

            view_ssh_public_key()

        elif mode == "view gpg":

            view_gpg_public_key()

        elif mode == "ssh passwd":

            change_ssh_key_password()

        elif mode == "gpg passwd":

            change_gpg_password()

        elif mode == "quit":

            break

        elif mode == "help":

            commands()
            
        else:

            print(Fore.RED + Style.BRIGHT + "\nInvalid command\n")
            print(Style.RESET_ALL)


if __name__ == "__main__":

    main()