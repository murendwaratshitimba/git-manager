import os

def view_gpg_public_key():


    email = input("Email: ").strip()

    os.system("gpg --list-secret-keys --keyid-format LONG " + email)

    secret_ID = input("SigningID: ").strip()

    os.system("gpg --armor --export " + secret_ID)

