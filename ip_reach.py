import sys
import platform
import subprocess
from bcolors import bcolors


def ip_reach(ip_list):
    """Check connection to devices (ping ip addresses from the list)."""

    #List for faild pings
    failed = []

    #Os platform detection
    os_pl = platform.system()
    
    ping_parameter = '-c'
    if os_pl == 'Windows':
        ping_parameter = '-n'

    for ip in ip_list:

        #Pinging ip addresses (no need to print messages or errors)
        ping_response = subprocess.call(f'ping {ip} {ping_parameter} 2', stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) 

        if ping_response == 0:
            print(f'{ip} reachable.')
        else:
            failed.append(ip)
        
    if len(failed) > 0:

        print(bcolors.FAIL, end='')
        
        for ip in failed:
            print(f'{ip} not reachable.')

        print(f'{bcolors.ENDC}Quitting...', end='')
        sys.exit()
