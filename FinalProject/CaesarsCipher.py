words = ["Slitheen", "slitheen", "whovian", "Paracelsus", "paracelsus", "Sola Dosis Facit Venenum", "sola dosis facit venenum", "SolaDosisFacitVenenum", "soladosisfacitvenenum", "Theophrastus Bombastus Von Hohenheim", "TheophrastusBombastusVonHohenheim", "theophrastus bombastus von hohenheim", "theophrastusbombastusvonhohenheim", "Jodie Whittake", "JodieWhittake", "jodie whittake", "jodiewhittake", "Tardis", "tardis", "theTardis", "thetardis", "Slitheen",
"Paracelsus",
"paracelsus",
"Sola",
"Dosis",
"Facit",
"Venenum",
"sola",
"dosis",
"facit",
"venenum",
"SolaDosisFacitVenenum",
"soladososfacitvenenum",
"Tiger",
"tiger",
"DoctorWho",
"doctorwho",
"Jodie",
"JodieWhittake",
"Whittake",
"Cyberman",
"cyberman",
"Dalek",
"dalek",
"DalektheCyberman",
"Dalekcyberman",
"fantastic!",
"Jodie Whittake",
"brilliant",
"doctor",
"fighting",
"sonic",
"screwdriver",
"SonicScrewdriver",
"Tardis",
"Villains",
"DalektheCyberman",
"favorite",
"Slitheen",
"family",
"SlitheenFamily",
"TheSlitheenFamily",
"Mycat",
"MyCat",
"Theophrastus",
"Bombastus",
"VonHohenheim",
"TheophrastusBombastusVonHohenheim",
"TBVH",
"tbvh",
"scientist",
"father of toxicology",
"fatheroftoxicology",
"FatherofTexicology",
"Sola Dosis Facit Venenum",
"SolaDosisFacitVenenum",
"Sola",
"Dosis",
"Facit",
"Venenum",
"ILoveCats",
"Ilovecats",
"ilovecats",
"Cat",
"Cats",
"Thedosemakesthepoison",
"TheDoseMakesThePoison",
"thedosemakesthepoison",
"Theophrastusbombastusvonhohenheim",
"theophrastusbombastusvonhohenheim",
"Soladosisfacitvenenum",
"soladosisfacitvenenum",
"a",
"d",
"z",]

"""
text is the word you want to encrypt. 
s is an int that decides steps forward or backwards in the alphabet you want to encrypt.+ is forward, - is backwards. 
"""
def encrypt(text, s):
    result = ""

    # transverse the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
        #print(result)

"""
here is the methods to include in the word list.
"""
try:
    outputFile = open("wordlist.txt", "w") # lager en ny fil kalt myOutFile
except Exception as e:
    print(e)

#Select how to encrypt the text. -3 is backwards
s = -3
for x in words:
    #print(encrypt(x, s))
    outputFile.write(encrypt(x, s))
    outputFile.write("\n")

outputFile.close()