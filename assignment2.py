file = open("passwordlist.txt", "r")
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