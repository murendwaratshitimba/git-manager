import os

def change_gpg_password():

    email = input("Email: ").strip().lower()

    os.system("gpg --list-secret-keys --keyid-format LONG " + email)

    secretID = input("ID: ").strip().lower()

    os.system("gpg --edit-key " + secretID)

