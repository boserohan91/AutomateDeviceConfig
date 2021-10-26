import os
import sys
import time
import re
import paramiko
from paramiko.ssh_exception import AuthenticationException



cred_file_path = input("Enter path for the file containing username/password: ")

if not os.path.isfile(cred_file_path):
    print("Path for credential file is invalid")
    sys.exit()



cmd_file_path = input("Enter path for command file: ")

if not os.path.isfile(cmd_file_path):
    print("Path for command file is invalid")
    sys.exit()
else:
    print("Sending commands to device(s)...\n")



def ssh_connection(ip):

    global cred_file_path
    global cmd_file_path

    cred_file = open(cred_file_path, 'r')

    cred_file.seek(0)
    username = cred_file.readlines()[0].split(",")[0].rstrip("\n")

    cred_file.seek(0)
    password = cred_file.readlines()[0].split(",")[1].rstrip("\n")

    try:

        session = paramiko.SSHClient()

        #for testing purposes only
        #allows auto-accepting host keys, can be a security issue in production environments
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        session.connect(ip.rstrip('\n'), username=username, password=password)

        connection = session.invoke_shell()

        #Setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        cmd_file = open(cmd_file_path, 'r')
        cmd_file.seek(0)
        for command in cmd_file.readlines():
            connection.send(command + "\n")
            time.sleep(2)

        cred_file.close()
        cmd_file.close()

        output = connection.recv(65535)

        if re.search(b"% Invalid Input", output):
            print(f"* Atleast one IOS syntax error on device {ip}\n")
        else:
            print(f"Done for device {ip} \n")

        #print(str(output)+"\n")

        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password \n* Check username/password file or device configuration file.")
        print("* Program terminated..Bye!")

