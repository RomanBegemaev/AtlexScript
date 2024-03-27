# atlexscript

import os
import paramiko

# Setting parameters for connecting to the server
server_ip = input("Enter IP-Adress: ")
username = input("Enter username: ")
password = input("Enter password: ")
domain = input("Enter domain name: ")

# Create an SSHClient object and set the no host key policy
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#nginx conf
source_filename = 'baseConfig.txt'

def copy_nginx_config_and_modify(filename, domain):
    # Открываем исходный файл для чтения
    with open(filename, 'r') as file:
        text = file.readlines()

    # Создаем новый список для модифицированного текста
    new_text = []

    # Проходим по каждой строке исходного файла
    for line in text:
        if 'name domain' in line:
            # Если строка содержит 'name domain', заменяем domain на новое значение
            new_text.append(line.replace('domain', domain))
        else:
            # Для остальных строк просто добавляем их в новый текст
            new_text.append(line)

    # Создаем новый файл с модифицированным текстом
    with open(domain, 'w') as new_file:
        new_file.writelines(new_text)

    # Выводим сообщение об успешном создании нового файла
    print(f'Файл {domain} успешно создан с модифицированным текстом.')





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

# Вызываем функцию для копирования текста и изменения имени домена
copy_nginx_config_and_modify(source_filename, domain)

# Closing the connection to the server
ssh_client.close()