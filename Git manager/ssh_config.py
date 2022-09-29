import os

def configureAccount():

    home_directory = os.path.expanduser("~")

    # start adding contents to the file
    config_file = open(home_directory + "/.ssh/config","r")

    content = config_file.read()

    config_file.close()

    config_file = open(home_directory + "/.ssh/config", "w")
    
    host = input("HostName: ").lower().strip()
    user = input("gitlab/github username: ").lower().strip()
    ssh_key_name = input("ssh file name: ").lower().strip()

    # configure

    configure = """Host {0}
    HostName {0}
    User {1}
    IdentityFile ~/.ssh/{2}
    
    """.format(host, user, ssh_key_name)

    config_file.write("\r" + configure)
    config_file.write(content)
    config_file.close()

