# EAFP - we try to ping, then get the error if it doesn't work
class PingIP:
    def __init__(self):
        import os
        try:
            os.system('ping -c 1 127.0.0.1')
        except OSError as e:
            print("e")

    def iprange():
        import os
        for ping in range(0,256):
            ip="127.0.0."+str(ping)
            os.system('ping -c 1 %s' % ip)
PingIP()
PingIP.iprange()
