# LBYL - we check if the file exists and opens it if it does, then give the exception if it is not found
import os
try:
    if os.stat("passwordlist.txt") == true:
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
Har en generel ty block som kan plukke opp flere feilen som kan oppstå i for loopen
og printer ut hva som gikk galt
"""
def find_unique_passwords():
    name = ""
    try:
        for i, j in zip(unamelist, pwdlist):
            teller = -1
            teller2 = 1
            for x in unamelist:
                teller = teller + 1
                if i == x:
                    teller2 = teller2 + 1
                    name = str(x)


            print(name + " har " + str(teller2) + " forskjellige passord")
    except Exception as e:
        print(e)
        

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