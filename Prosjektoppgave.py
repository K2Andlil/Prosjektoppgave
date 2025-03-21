#Oppgave a

import pandas as p
import matplotlib.pyplot as plt
import time

# Leser inn filen og henter ut relevante kolonner
def les_data():
    x = p.read_excel('support_uke_24.xlsx', usecols='A:D')

    # Lagrer data i array
    u_dag = x.iloc[:, 0].to_numpy()
    kl_slett = x.iloc[:, 1].to_numpy()
    varighet = x.iloc[:, 2].to_numpy()
    score = x.iloc[:, 3].to_numpy()

    # Returnerer variabler
    return u_dag, kl_slett, varighet, score

#Oppgave b

# Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = les_data()

# Finner antall hendvendelser per ukedag
ukedager_telling = p.Series(u_dag).value_counts().sort_index()

# Viser resultatene i søylediagram
ukedager_telling.plot(kind='bar')
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.title('Antall henvendelser per ukedag')
plt.show()

time.sleep(3)

#Oppgave c

# Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = les_data()

# Finner korteste og lengste samtaletid
min_varighet = varighet.min()
max_varighet = varighet.max()

print(f"Den korteste samtaletiden i uke 24 varte: {min_varighet} minutter")
time.sleep(1)
print(f"Den lengste samtaletiden i uke 24 varte: {max_varighet} minutter")

time.sleep(3)


#Oppgave d

# Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = les_data()

# Konverterer varighet til timedelta
varighet_timedelta = p.to_timedelta(varighet)

# Beregner gjennomsnittlig samtaletid i minutter og runder til 1 desimal
snitt_varighet = varighet_timedelta.mean()
snitt_varighet_minutter = round(snitt_varighet.total_seconds() / 60, 1)

print(f"Snittet av samtaletiden i uke 24 var: {snitt_varighet_minutter} minutter")

time.sleep(3)

#Oppgave e

# Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = les_data()

# Konverterer kl_slett til datetime
kl_slett = p.to_datetime(kl_slett, format='%H:%M:%S')

# Henter timen fra kl_slett
kl_slett_timer = kl_slett.hour

# Fordeler basert på tidsrom
tidsrom = p.cut(kl_slett_timer, bins=[8, 10, 12, 14, 16], labels=['kl: 08-10', 'kl: 10-12', 'kl: 12-14', ' kl:14-16'])

# Teller antall henvendelser per tidsrom og lager sektordiagram
tidsrom.value_counts().plot(kind='pie', title="Fordeling av hendvendelser basert på tidsrom i uke 24")
plt.axis('equal')
plt.show()

time.sleep(3)

#Oppgave f

# Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = les_data()

# Initialiser variabler for positiv og negativ tilbakemelding
positive_count = 0
negative_count = 0
total_count = 0

# Går gjennom score-listen og teller antallet positive og negative tilbakemeldinger
for s in score:
    if s:  # Hopper over tomme celler
        total_count += 1
        if s < 7:
            negative_count += 1
        elif 7 <= s <= 8:
            pass  # Nøytral tilbakemelding påvirker ikke NPS
        elif 9 <= s <= 10:
            positive_count += 1

# Beregner prosentandel for positive og negative tilbakemeldinger
positive_percentage = (positive_count / total_count) * 100
negative_percentage = (negative_count / total_count) * 100

# Beregner NPS og avrunder tallet
NPS = round(positive_percentage - negative_percentage, 1)

# Skriver ut NPS
print(f"NPS Score for uke 24 var: {NPS}")