import os


"""
Create or edit the .gitconfig file
"""
def gitconfig():

    home_directory = os.path.expanduser("~")

    gitconfig_file = open(home_directory + "/.gitconfig", "w")
    account_name = input("Your Name: ").title()
    email = input("Email: ").lower()
    file_name = input("gpg Config file Name: ").lower()
    

    configure = """[init]
	defaultBranch = main

[commit]
	gpgsign = true

[user]
	name = {0}
	useConfigOnly = true
	email = {1}

[include]
	path = ~/.gitconfig.{2}
    
    """.format(account_name, email, file_name)

    gitconfig_file.write(configure)

    gitconfig_file.close()

