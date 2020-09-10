import os.path
from bcolors import bcolors


def file_ip_read():
    """Return IPv4 addresses from a .txt file as a list."""

    #Prompting user for input
    file_path = input('Enter IPv4 addresses list file path: ')

    #Checking if the file exists
    while not os.path.isfile(file_path):
        print(f'{bcolors.FAIL}File \'{file_path}\' not found!{bcolors.ENDC}')
        file_path = input('Enter IPv4 addresses list file path: ')

    #Opening user selected file for reading (IP addresses file)
    ip_file = open(file_path, 'r')

    #Starting from the beginning of the file
    ip_file.seek(0)

    #Reading each line in the file and creating a list of ip addresses (removing \n)
    ip_file_lines = ip_file.readlines()
    ip_list = [line.strip() for line in ip_file_lines]

    #Cloding the file
    ip_file.close()

    return ip_list
