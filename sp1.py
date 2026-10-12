# Kód žáka: 27
# Datum: 12. 10. 2026
# Program jede s kuličkou tam a zpět a pak vypíše tabulku čísel 1 až pocet (číslo, druhá mocnina, odmocnina).

import math
import time

pocet = 8          # délka dráhy kuličky i počet řádků tabulky (číslo od 5 do 15)
PAUZA = 0.1        # kolik sekund se čeká mezi řádky, aby byl pohyb vidět
KULICKA = "O"      # znak, který se posouvá po obrazovce

print("Kulička jede")

# 1) kulička jede doprava: i mezer a za nimi kulička
for i in range(pocet):
    print(" " * i + KULICKA)
    time.sleep(PAUZA)

# 2) kulička se vrací doleva: mezer ubývá, proto pocet - i
for i in range(pocet):
    print(" " * (pocet - i) + KULICKA)
    time.sleep(PAUZA)

print("Tabulka")

# 3) číslo, jeho druhá mocnina a odmocnina pro 1 až pocet
for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
