# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""
Created on Tue Oct  1 14:12:45 2024

@author: sara
"""

#Oppgave d) og e)

from datetime import datetime #e)

# Åpne og les filene
with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as f1, open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as f2:
    # Les linjene og splitt dataene på mellomrom eller komma
    # Forutsetter at første linje er header og hopper over den
    linjer1 = f1.readlines()[1:]
    linjer2 = f2.readlines()[1:]

# Initialiser lister for hver kolonne i fil1
navn_fil1 = []
stasjon_fil1 = []
tid_fil1 = []
lufttemperatur_fil1 = []
lufttrykk_fil1 = []

# Initialiser lister for hver kolonne i fil2
dato_tid_fil2 = []
tid_siden_start_fil2 = []
trykk_barometer_fil2 = []
trykk_absolutt_fil2 = []
temperatur_fil2 = []

#e) 
# Ta in dato og tid som tekst 
# Identifisere type dato 
# Konvertere til datetime
# Returner datetime ut av funksjonen 
def parse_datetime(datetime_string):
    if "/" in datetime_string:
        return datetime.strptime(datetime_string, '%m/%d/%Y %H:%M:%S %p')
    else:
        return datetime.strptime(datetime_string, '%m.%d.%Y %H:%M')

linjer1.pop()
# Fyll listene for fil1
for linje in linjer1:
    data = linje.replace(",",".").strip().split(";")
    navn_fil1.append(data[0])
    stasjon_fil1.append(data[1])
    tid_fil1.append(
        datetime.strptime(data[2], '%d.%m.%Y %H:%M')  #e)
        )  
    lufttemperatur_fil1.append(data[3])
    lufttrykk_fil1.append(data[4])

# Fyll listene for fil2
for linje in linjer2:
    data = linje.replace(",",".").strip().split(";")
    dato_tid_fil2.append(
        parse_datetime(data[0])              #e)
        )
    tid_siden_start_fil2. append(data[1])
    trykk_barometer_fil2.append(data[2])
    trykk_absolutt_fil2.append(data[3])
    temperatur_fil2.append(data[4])

temperatur_fil2.replace(',', '.')
    
#f)
import matplotlib.pyplot as plt                

x_koordinater = [tid_fil1, dato_tid_fil2]
y_koordinater = [lufttemperatur_fil1, temperatur_fil2]

plt.plot(x_koordinater[0], y_koordinater[0], "o-")
plt.plot(x_koordinater[1], y_koordinater[1], "o-")
plt.show()
        




