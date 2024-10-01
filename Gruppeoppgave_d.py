#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:12:45 2024

@author: sara
"""

#Oppgave d)

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

# Fyll listene for fil1
for linje in linjer1:
    data = linje.strip().split(";") 
    navn_fil1.append(data[0])
    stasjon_fil1.append(data[1])
    tid_fil1.append(data[2])  
    lufttemperatur_fil1.append(data[3])
    lufttrykk_fil1.append(data[4])

# Fyll listene for fil2
for linje in linjer2:
    data = linje.strip().split(";") 
    dato_tid_fil2.append(data[0])
    tid_siden_start_fil2. append(data[1])
    trykk_barometer_fil2.append(data[2])
    trykk_absolutt_fil2.append(data[3])
    temperatur_fil2.append(data[4])