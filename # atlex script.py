# atlex script


import paramiko

# Setting parameters for connecting to the server
server_ip = input("Введите IP-адрес сервера: ")
username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

# Create an SSHClient object and set the no host key policy
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connecting to server
ssh_client.connect(server_ip, username=username, password=password)

commands = [
    'sudo apt update && sudo apt upgrade -y',
    'sudo apt install nginx -y',
    'sudo apt install curl -y',
    'sudo apt install python -y',
    'sudo apt install python3-apt -y',
    'sudo apt-get install ssh -y',
    'sudo apt install gnupg -y',
    'mkdir ~/.ssh',
    'nano ~/.ssh/authorized_keys',  
    'nano /etc/ssh/sshd_config',     
    'sudo systemctl reload ssh'       
]

for command in commands:
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    print(output)


# Closing the connection to the server
ssh_client.close()