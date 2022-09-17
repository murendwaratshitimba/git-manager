import os

def configureAccount():

    home_directory = os.path.expanduser("~")

    # start adding contents to the file
    config_file = open(home_directory + "/.ssh/config","r")

    content = config_file.read()

    config_file.close()

    
    
    config_file = open(home_directory + "/.ssh/config", "w")

    host = input("HostName: ").lower()
    user = input("gitlab/github username: ").lower()
    ssh_path = input("Private Key Path: ").lower()

    # configure

    configure = """Host {0}

    HostName {0}
    User {1}
    IdentityFile ~{2}
    
    """.format(host, user, ssh_path)

    config_file.write(configure)
    config_file.write(content)
    config_file.close()

