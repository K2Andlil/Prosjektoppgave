#Oppgave e
import pandas as p
import matplotlib.pyplot as plt
import Les

#Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = Les.les_data()

#Konverterer kl_slett til datetime
kl_slett = p.to_datetime(kl_slett, format='%H:%M:%S')

#Henter timen fra kl_slett
kl_slett_timer = kl_slett.hour

#Fordeler basert på tidsrom
tidsrom = p.cut(kl_slett_timer, bins=[8, 10, 12, 14, 16], labels=['kl: 08-10', 'kl: 10-12', 'kl: 12-14', ' kl:14-16'])

#Teller antall henvendelser per tidsrom og lager sektordiagram
tidsrom.value_counts().plot(kind='pie', title="Fordeling av hendvendelser basert på tidsrom i uke 24")
plt.axis('equal')
plt.show()
