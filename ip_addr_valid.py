from bcolors import bcolors
import sys


def ip_addr_valid(ip_list):
    """
    Check if a list of IPv4 addresses is valid

    excluded addresses (invalid):

    loopback:                   127.0.0.0 - 127.255.255.255
    multicast:                  224.0.0.0 - 239.255.255.255
    broadcast:                  255.255.255.255
    link-local:                 169.254.0.0 - 169.254.255.255
    reserved for future use:    240.0.0.0 - 255.255.255.254

    0.0.0.0 <- non-routable meta-address used to designate an invalid,
               unknwon or non-applicable target

    0.0.0.0 – 0.255.255.255 <- only valid as sourse address (scope: software)

    ---------------------------------------------------------
    proper unicast addresses:          1.0.0.0 - 223.255.255.255
    """

    #Checking for duplicates
    ip_set = set(ip_list)
    if len(ip_set) != len(ip_list):
        duplicated = []
        for ip in ip_set:
            if ip_list.count(ip) > 1:
                duplicated.append(ip)
        
        print(f'{bcolors.FAIL}Duplicated IPv4 addresses: ', end='')
        print(*(ip for ip in duplicated), sep=', ', end='')
        print(bcolors.ENDC)
        sys.exit()

    #Checking every IPv4 address from the list
    for ip in ip_list:

        #Splitting an address to octets
        octets = ip.split('.')
        
        #Checking the octets:
        if(len(octets) != 4):
            print(f'{bcolors.FAIL}Invalid IPv4 address (invalid number of octets): {ip}{bcolors.ENDC}')
            sys.exit()
        elif (1 <= int(octets[0]) <= 223) == False:
            print(f'{bcolors.FAIL}Invalid IPv4 address (not a proper unicast): {ip}{bcolors.ENDC}')
            sys.exit()
        elif (0 <= int(octets[1]) <= 255 and 0 <= int(octets[2]) <= 255 and 0 <= int(octets[3]) <= 255) == False:
            print(f'{bcolors.FAIL}Invalid IPv4 address: {ip}{bcolors.ENDC}')
            sys.exit()
        elif int(octets[0]) == 127:
            print(f'{bcolors.FAIL}Invalid IPv4 address (loopback): {ip}{bcolors.ENDC}')
            sys.exit()
        elif int(octets[0]) == 169 and int(octets[1]) == 254:
            print(f'{bcolors.FAIL}Invalid IPv4 address (link-local): {ip}{bcolors.ENDC}')
            sys.exit()
