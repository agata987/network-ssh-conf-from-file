from file_ip_read import file_ip_read
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import SSH_connection
import os
from bcolors import bcolors

# Reading list of IPv4 addresses from a given file
ip_list = file_ip_read()

# Checking the addresses validity
ip_addr_valid(ip_list)

# Checking the connectivity to the remote devices
ip_reach(ip_list)

# Prompting for username, password for ssh and the commands list file
username = input('Enter the username for ssh: ')
password = input('Enter the password for ssh: ')
cmd_file = input('Enter the path for a command file: ')

while not os.path.isfile(cmd_file):
    print(f'{bcolors.FAIL}File \'{cmd_file}\' not found!{bcolors.ENDC}')
    cmd_file = input('Enter the path for a command file: ')

# Executing commands via ssh
ssh_con = SSH_connection(username, password, cmd_file)
ssh_con.execute_commands(ip_list)
