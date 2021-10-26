import os
from ip_validity_check import ip_validity_check
from ip_reachability import ip_reachability_check
from ssh_conn import ssh_connection


def extract_ip_from_file():

    ip_file_path = input("Enter path for file containing the ip addresses: ")

    if not os.path.isfile(ip_file_path):
        print("Invalid path for file")

    ip_file = open(ip_file_path, 'r')

    ip_file.seek(0)

    ip_list = []

    for ip in ip_file.readlines():
        ip_list.append(ip.rstrip("\n"))
    
    print(ip_list)

    ip_file.close()

    return ip_list
