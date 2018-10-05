"""
Sorterer tekstfilen passwordlist fra oppgaven slik at en får en kolonne med brukernavn i alfabetisk rekkefølge og en med passord.
Lettere og finne spesifike brukere og en kan se hvor mange like brukernavn du har.
Er nummerert slik at en har oversikt over total nr av brukere
Print er kun for å kunne se hvordan det blir uten å trenge å åpne filen
"""
"""
Bruker en except for å fange opp en av de vanligste feilene, har og en except etter for å fange
opp andre mulige feil. Har endra utskriften ved FileNotFoundError til "File not found" i stedet for e
LBYL - prøver å åpne fil før vi leser den, får feilmelding om det ikke går
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
