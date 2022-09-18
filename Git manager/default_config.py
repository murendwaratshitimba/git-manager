import os


def default():

    home_directory = os.path.expanduser("~")

    # Ensure that the file already exists
    if os.path.exists(home_directory + "/.ssh/config"):
        pass

    else:
        config_file = open(home_directory + "/.ssh/config", "a")

        config_file.write("""### -- general --

Host *

    AddKeysToAgent yes
    IdentitiesOnly yes
    PreferredAuthentications publickey
    Compression yes
        """)

        config_file.close()

def default_ssh_directory():

    home_directory = os.path.expanduser("~")

    if os.path.exists(home_directory + "/.ssh"):

        pass
    
    else:

        os.system("mkdir " + home_directory + "/.ssh") 
        print("done")

