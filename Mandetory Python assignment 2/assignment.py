class PingIP:
    def __init__(self):
        import os
        os.system('ping -c 1 127.0.0.1')

    def iprange():
        import os
        for ping in range(0,256):
            ip="127.0.0."+str(ping)
            os.system('ping -c 1 %s' % ip)
PingIP()
PingIP.iprange()
