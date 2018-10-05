# LBYL - we check if the file exists and opens it if it does, then give the exception if it is not found
import os
try:
    if os.stat("passwordlist.txt"):
        file = open("passwordlist.txt", "r")
except IOError:
    print("File not found")
f = file.read()
file.close()

l = f.split(';')
print (len(l))

unamelist = []
pwdlist = []

for i in l:
    a = l[0]
    b = a.split(':')
    del(l[0])
    unamelist.append(b[0])
    pwdlist.append(b[1])

for u in unamelist:
    print (u)

for p in pwdlist:
    print (p)

uniqueunamelist = []
unameduplist = []
for u in unamelist:
    if u not in uniqueunamelist:
        uniqueunamelist.append(u)
    else:
        unameduplist.append(u)
        uniqueunamelist.remove(u)
        unameduplist.append(u)

uniquepwdlist = []
pwdduplist = []
for u in pwdlist:
    if u not in uniquepwdlist:
        uniquepwdlist.append(u)
    else:
        pwdduplist.append(u)
        uniquepwdlist.remove(u)
        pwdduplist.append(u)
        
        
"""
Denne delen finner ut hvor mange unike passord hver bruker har
"""
def find_unique_passwords():
    name = ""
    for i, j in zip(unamelist, pwdlist):
        teller = -1
        teller3 = 0
        for x in unamelist:
            teller = teller + 1
            if i == x:
                teller3 = teller3 + 1
                name = str(x)
                #print(x, pwdlist[teller]) printen fungerer ikke helt, mangler 1 passord på hver bruker?

        print(name + " har " + str(teller3) + " forskjellige passord")
        

unameduplist.sort()
pwdduplist.sort()
print ("Unique usernames")
print (uniqueunamelist)
print ("duplicate usernames")
print (unameduplist)
print ("Unique passwords")
print (uniquepwdlist)
print ("Duplicate passwords")
print (pwdduplist)
print ("Unique", len(uniqueunamelist))
print ("Duplicates", len(unameduplist))
print ("Unique passwords", len(uniquepwdlist))
print ("Duplicate passwords", len(pwdduplist))
find_unique_passwords()