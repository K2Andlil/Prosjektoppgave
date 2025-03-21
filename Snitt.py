#Oppgave d
import Les
import pandas as p

#Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = Les.les_data()

#Konverterer varighet til timedelta
varighet_timedelta = p.to_timedelta(varighet)

#Beregner gjennomsnittlig samtaletid i minutter og runder til 1 desimal
snitt_varighet = varighet_timedelta.mean()
snitt_varighet_minutter = round(snitt_varighet.total_seconds() / 60, 1)

print(f"Snittet av samtaletiden i uke 24 var: {snitt_varighet_minutter} minutter")