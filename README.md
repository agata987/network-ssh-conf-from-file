# network-ssh-conf-from-file

! Warning, in ssh_connection.py:  
For testing purposes, this allows auto-accepting unknown host keys:  
**session.set_missing_host_key_policy(paramiko.AutoAddPolicy())**  
Do not use in production! The default would be RejectPolicy.  

