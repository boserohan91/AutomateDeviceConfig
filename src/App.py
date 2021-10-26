import sys

from ip_validity_check import ip_validity_check
from ip_reachability import ip_reachability_check
from ssh_conn import ssh_connection
from spawn_threads import spawn_threads
from ip_extract import extract_ip_from_file

iplist = extract_ip_from_file()

try:
    ip_validity_check(iplist)
except KeyboardInterrupt:
    print("Exiting program...")
    sys.exit()

try:
    ip_reachability_check(iplist)
except KeyboardInterrupt:
    print("Exiting Program...")
    sys.exit()

spawn_threads(iplist, ssh_connection)




