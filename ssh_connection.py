import os.path
import sys
import paramiko
import time
import re
import threading
from bcolors import bcolors


class SSH_connection(object):
    """
    Make the connection and execute the commands on remote devices based on IPv4 addresses list.

    """

    def __init__(self, username, password, cmd_file):

        self.username = username
        self.password = password
        self.cmd_file = cmd_file

    # Make connection and execute the commands on a device with given IPv4 address
    def ssh_connection(self, ip):

        try:
            session = paramiko.SSHClient()

            #For testing purposes, this allows auto-accepting unknown host keys !!!!
            #Do not use in production! The default would be RejectPolicy
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            session.connect(ip, username=self.username, password=self.password)

            #Starting interactive shell session on the remote device
            connection = session.invoke_shell()

            #Entering global config mode
            connection.send('enable\n')
            #To show the entire output (for ex. no space pressing needed if we run 'show run')
            connection.send('terminal length 0\n')
            time.sleep(1)
            connection.send('configure terminal\n')
            time.sleep(1)

            #Opening commands file
            commands_file = open(self.cmd_file, 'r')

            #Starting from the beginning of the file
            commands_file.seek(0)

            #Executing commands
            for command in commands_file.readlines():
                connection.send(command + '\n')
                time.sleep(2)

            commands_file.close()

            #Checking the output for IOS syntax errors
            # 65535 <- max number for bytes to receive
            output = connection.recv(65535)

            if re.search(b'invalid input', output, re.IGNORECASE):
                print(f'{bcolors.FAIL}Syntax error on: {ip}{bcolors.ENDC}')
            else:
                print(f'{bcolors.OKBLUE}Device {ip} configured.{bcolors.ENDC}')

            #Reading command output
            print(f'{bcolors.HEADER}{ip} output:{bcolors.ENDC} {str(output)}\n')

            session.close()
        
        except paramiko.AuthenticationException:
            print(f'Authentication failed for {ip}.')

    def execute_commands(self, ip_list):

        threads = []

        for ip in ip_list:
            th = threading.Thread(target=self.ssh_connection, args=(ip, ))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()
