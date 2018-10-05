"""
Sorterer tekstfilen passwordlist fra oppgven slik at du for en kolone med brukernavn og passord i alfabetisk rekkefølge.
Lettere og finne spesefike brukere og kan og se hvor mange like brukernavn du har.
Er også numerert slik at du har oversikt over total nr av brukere
Print er kun for å kunne se hvordan det blir uten å trenge å åpne filen
"""
"""
Bruker en except for å fange opp en av de vanligste feilene, har og en except etter for å fange
opp andre mulige feil
"""
try:
    file = open("passwordlist.txt", "r")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
f = file.read()
file.close()

passwordlist = f.split(';') # Splitter filen og legger den in i en liste basert på ;
passwordlist.sort()
del passwordlist[0] #Sletter index = som er tom pga filen slutter med et ;

n = 0
try:
    outputFile = open("myOutFile.txt", "w") # lager en ny fil kalt myOutFile
except Exception as e:
    print(e)
outputFile.write("Brukernavn og passordliste")
outputFile.write("\n")
for line in passwordlist:
    n = n+1
    outputFile.write("Nr " + str(n) + ": " + line)
    outputFile.write("\n")
    print("Nr " + str(n) + ": " + line)
outputFile.close()
