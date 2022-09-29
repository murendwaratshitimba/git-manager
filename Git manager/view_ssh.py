import os

def view_ssh_public_key():

    home_directory = os.path.expanduser("~")

    name = input("ssh file name: ").strip()

    os.system("cat " + home_directory + "/.ssh/" + name + ".pub")

