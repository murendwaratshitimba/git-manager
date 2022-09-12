from os import system
import emoji

def welcome():

    print("""********************************************
Welcome to gitlab/github ssh and gpg keys manager program

by Murendwa Ratshitimba
**********************************************************
    """)

def ssh_key_command(algorithm):

    system("ssh-key-gen -t " + algorithm)


def generate_ssh_key():

    """
    Generate ssh key 
    """

    while True:

        algorithim = input("""Choose Algorithm

        1. ED25519
        2. RSA
        3. ED25519_SK
        4. ECDSA

        NB: Only choose a number from the list above

        """).strip().lower()


        if algorithim == "1":

            ssh_key_command("ed25519")

        elif algorithim == "2":

            pass

        elif algorithim == "3":

            pass

        elif algorithim == "4":
            pass

        else:

            print("""******
            Invalid Input..
            ****************
            \n\n""")


def main():

    # welcome the user
    welcome()
    generate_ssh_key()

if __name__ == "__main__":

    main()