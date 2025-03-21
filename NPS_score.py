import Les

#Henter data fra array i Les.py
u_dag, kl_slett, varighet, score = Les.les_data()

#Initialiser variabler for positiv og negativ tilbakemelding
positive_count = 0
negative_count = 0
total_count = 0

#Går gjennom score-listen og teller antallet positive og negative tilbakemeldinger
for s in score:
    if s:  # Hopper over tomme celler
        total_count += 1
        if s < 7:
            negative_count += 1
        elif 7 <= s <= 8:
            pass  # Nøytral tilbakemelding påvirker ikke NPS
        elif 9 <= s <= 10:
            positive_count += 1

#Beregner prosentandel for positie og negative tilbakemeldinger
positive_percentage = (positive_count / total_count) * 100
negative_percentage = (negative_count / total_count) * 100

#Beregner NPS og avrunder tallet
NPS = round(positive_percentage - negative_percentage, 1)

#Skriver ut NPS
print(f"NPS Score: {NPS}")