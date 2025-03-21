#Oppgave b
import Les
import pandas as p
import matplotlib.pyplot as plt

#Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = Les.les_data()

#Finner antall hendvendelser per ukedag
ukedager_telling = p.Series(u_dag).value_counts().sort_index()

#Viser resultatene i søylediagram
ukedager_telling.plot(kind='bar')
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.title('Antall henvendelser per ukedag')
plt.show()