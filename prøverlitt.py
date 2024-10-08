#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:01:35 2024

@author: sara
"""


from datetime import datetime
import matplotlib.pyplot as plt

# Oppdatert parse_datetime-funksjon
def parse_datetime(datetime_string):
    try:
        # Prøv først med AM/PM-format
        return datetime.strptime(datetime_string, '%m/%d/%Y %I:%M:%S %p')
    except ValueError:
        # Hvis det feiler, prøv 24-timers-formatet
        return datetime.strptime(datetime_string, '%m.%d.%Y %H:%M')

# Åpne og les filene
with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as f1, open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as f2:
    linjer1 = f1.readlines()[1:]
    linjer2 = f2.readlines()[1:]

# Initialiser lister for fil1
tid_fil1 = []
lufttemperatur_fil1 = []
lufttrykk_fil1 = []

# Initialiser lister for fil2
dato_tid_fil2 = []
trykk_barometer_fil2 = []
trykk_absolutt_fil2 = []
temperatur_fil2 = []

# Fyll listene for fil1
for linje in linjer1:
    try:
        data = linje.strip().split(";")
        tid_fil1.append(datetime.strptime(data[2], '%m.%d.%Y %H:%M'))  #e)
        lufttemperatur_fil1x = data[3].replace(',', '.')
        lufttemperatur_fil1.append(float(lufttemperatur_fil1x))
        lufttrykk_fil1x = data[4].replace(",", ".")
        lufttrykk_fil1.append(float(lufttrykk_fil1x))
    except ValueError:
        pass
    
# Fyll listene for fil2
for linje in linjer2:
    data = linje.strip().split(";")
    if len(data) >= 5:
        # Bruk parse_datetime til å tolke datoen
        dato_tid_fil2.append(parse_datetime(data[0]))
        trykk_barometer_fil2x = data[2].replace(",", ".")
        trykk_absolutt_fil2x = data[3].replace(",", ".")
        temperatur_fil2x = data[4].replace(",", ".")
        
        if trykk_barometer_fil2x == '':
            try:
                trykk_absolutt_fil2.append(float(trykk_absolutt_fil2x))
                temperatur_fil2.append(float(temperatur_fil2x))
                trykk_barometer_fil2.append(None)  # Fyll inn None hvis data mangler
            except ValueError:
                pass
        else:
            try:
                trykk_barometer_fil2.append(float(trykk_barometer_fil2x))
                trykk_absolutt_fil2.append(float(trykk_absolutt_fil2x))
                temperatur_fil2.append(float(temperatur_fil2x))
            except ValueError:
                pass

# Plotting
plt.plot(tid_fil1, lufttemperatur_fil1, label="Meterologisk")
plt.plot(dato_tid_fil2, temperatur_fil2, label="UiS")
plt.legend()
plt.show()