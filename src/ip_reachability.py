import sys
import subprocess

def ip_reachability_check(ip_list):

    for ip in ip_list:

        ping_result = subprocess.call(["ping", '-c', '2', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_result == 0 :
            print(f"{ip} is reachable")
            continue
        else:
            print(f"{ip} is not reachable")
            sys.exit()