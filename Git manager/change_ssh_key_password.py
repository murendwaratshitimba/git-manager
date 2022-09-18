import os

def change_ssh_key_password():

    home_directory = os.path.expanduser("~") + "/.ssh/"
    name = input("ssh-key name: ").lower().strip()


    os.system("ssh-keygen -p -f " + home_directory + name)

