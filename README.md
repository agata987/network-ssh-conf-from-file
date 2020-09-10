# network-ssh-conf-from-file

**! Warning, in ssh_connection.py:**  
For testing purposes, this allows auto-accepting unknown host keys:  
**session.set_missing_host_key_policy(paramiko.AutoAddPolicy())**  
Do not use in production! The default would be RejectPolicy.  

The scripts can be used to configure routers and switches using ssh.  
IPv4 addresses are given in a file (e.g ip_addresses.txt)  
Commands are given in a file (e.g commands_file.txt)
