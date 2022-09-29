import os

"""
Configure the gpg signatures
"""
def gpg_configuration():

    home_directory = os.path.expanduser("~")
    signature = input("configuration file name: ").strip()
    email = input("Email: ").lower()

    config_file = open(home_directory + "/.gitconfig." + signature, "w")

    print("\n\n")
    os.system("gpg --list-secret-keys --keyid-format LONG " + email)

    signingkey = input("gpg private key: ").strip()

    configure = """[user]
    email = {0}
    signingkey = {1}
    """.format(email, signingkey)
    
    # write to the file
    config_file.write(configure)

    # close the file
    config_file.close()

    




