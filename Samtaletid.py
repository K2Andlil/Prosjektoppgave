#Oppgave c
import Les

#Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = Les.les_data()

#Finner korteste og lengste samtaletid
min_varighet = varighet.min()
max_varighet = varighet.max()

print(f"Den korteste samtaletiden i uke 24 varte: {min_varighet} minutter")
print(f"Den lengste samtaletiden i uke 24 varte: {max_varighet} minutter")