from curses.ascii import isdigit
from os import system
import emoji

"""
Welcome Message.
"""
def welcome():

    print("""**********************************************************
Welcome to gitlab/github ssh and gpg keys manager program

by Murendwa Ratshitimba
**********************************************************
    """)


"""
Generate the ssh key using just an algorithm
"""
def ssh_key_command(algorithm):

    system("ssh-keygen -t " + algorithm)


"""
Generate an an ssh key using algorithm and the bit size
"""
def ssh_key_command_bits(algorithm, bits):

    system("ssh-keygen -t " + algorithm + " -b " + bits)


def valid_bits():

    while True:

        bit_size = input("Specify the bits size [minimum is 1024 bits]: ").strip()

        if bit_size.isdigit() :

            if int(bit_size) >= 1024:


                return bit_size
            
            else:

                print("\nprovide bits is less than 1024!!\n")
        
        else:

            print("Please specify valid digits")


def generate_ssh_key():

    """
    Generate ssh key 
    """

    algorithims = ["ED25519", "RSA", "ECDSA"]
    

    while True:

        algorithim = input("""Choose Algorithm

        1. ED25519 [recommended]
        2. RSA [At least 2048 bits size is recommended]
        3. ECDSA

        NB: Only choose a number from the list above

        Option: """).strip().lower()

        print()


        if algorithim == "1":

            ssh_key_command(algorithims[0])

        elif algorithim == "2":

            bit_size = valid_bits()
            ssh_key_command_bits(algorithims[1], bit_size)

            

        elif algorithim == "3":

            ssh_key_command(algorithims[2])

        else:

            print("""
****************
Invalid Option
****************\n""")


def main():

    # welcome the user
    welcome()
    generate_ssh_key()


if __name__ == "__main__":

    main()