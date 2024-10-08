#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:01:35 2024

@author: sara
"""

#Oppgave d) og e)
from datetime import datetime
import matplotlib.pyplot as plt

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
    try:
        data = linje.strip().split(";") 
        tid_fil1.append(
            datetime.strptime(data[2], '%d.%m.%Y %H:%M')  #e)
            )  
        lufttemperatur_fil1x = data[3].replace(',', '.')
        lufttemperatur_fil1_float = float(lufttemperatur_fil1x)
        lufttemperatur_fil1.append(lufttemperatur_fil1_float)
        
        lufttrykk_fil1x = data[4].replace(",",".")
        lufttrykk_fil1_float = float(lufttrykk_fil1x)
        lufttrykk_fil1.append(lufttrykk_fil1_float)
    except ValueError:
        pass

# Fyll listene for fil2
for linje in linjer2:
    data = linje.strip().split(";")
    if len(data) >= 5:
        # Hent dato og tid
        dato_tid_fil2.append(parse_datetime(data[0]))
        
        # Hent verdier og erstatt komma med punktum
        trykk_barometer_fil2x = data[2].replace(",", ".")
        trykk_absolutt_fil2x = data[3].replace(",", ".")
        temperatur_fil2x = data[4].replace(",", ".")
        
        # Sjekk om barometertrykk er en tom streng
        if trykk_barometer_fil2x == '':
            try:
                # Hvis barometertrykk mangler, legg bare til absolutt trykk og temperatur
                trykk_absolutt_fil2_float = float(trykk_absolutt_fil2x)
                trykk_absolutt_fil2.append(trykk_absolutt_fil2_float)
                
                temperatur_fil2_float = float(temperatur_fil2x)
                temperatur_fil2.append(temperatur_fil2_float)
                
                # Legg til en None-verdi for barometertrykk for å opprettholde lengden
                trykk_barometer_fil2.append(None)
            except ValueError:
                # Hopp over linjer som ikke kan konverteres til float
                pass
        else:
            try:
                # Konverter og legg til barometertrykk
                trykk_barometer_fil2_float = float(trykk_barometer_fil2x)
                trykk_barometer_fil2.append(trykk_barometer_fil2_float)
                
                # Konverter og legg til absolutt trykk og temperatur
                trykk_absolutt_fil2_float = float(trykk_absolutt_fil2x)
                trykk_absolutt_fil2.append(trykk_absolutt_fil2_float)
                
                temperatur_fil2_float = float(temperatur_fil2x)
                temperatur_fil2.append(temperatur_fil2_float)
            except ValueError:
                # Hopp over linjer som ikke kan konverteres til float
                pass

# Plotting
plt.plot(tid_fil1, lufttemperatur_fil1, label="Meterologisk")
plt.plot(dato_tid_fil2, temperatur_fil2, label="UiS")
plt.legend()
plt.show()


#g) 

import numpy as np
import matplotlib.pyplot as plt

def beregn_gjennomsnitt(tider, temperaturer, n):
    gyldige_tidspunkter = []
    gjennomsnittsverdier = []
    
    # Gå gjennom hvert tidspunkt
    for i in range(n, len(tider) - n):
        # Beregn gjennomsnittet av de n forrige, den nåværende, og de n neste målingene
        snitt = np.mean(temperaturer[i - n:i + n + 1])
        
        # Legg til gyldig tidspunkt og gjennomsnittstemperatur i listene
        gyldige_tidspunkter.append(tider[i])
        gjennomsnittsverdier.append(snitt)
    
    return gyldige_tidspunkter, gjennomsnittsverdier

# Eksempeldata
tider = np.linspace(0, 100, 1000)  # 1000 tidspunkter
temperaturer = np.sin(tider) * 10 + 20  # Eksempeltemperaturer (sinuskurve)

# Beregn gjennomsnitt med n=30
n = 30
gyldige_tidspunkter, gjennomsnittsverdier = beregn_gjennomsnitt(tider, temperaturer, n)

# Plot original temperaturkurve og gjennomsnittskurve
plt.figure(figsize=(10, 6))
plt.plot(tider, temperaturer, label='Temperatur', color='blue')
plt.plot(gyldige_tidspunkter, gjennomsnittsverdier, label=f'Gjennomsnitt (n={n})', color='orange')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur og glidende gjennomsnitt')
plt.legend()
plt.grid(True)
plt.show()