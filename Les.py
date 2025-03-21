#Oppgave a
import pandas as p

def les_data():
#Leser inn filen og henter ut relevante kolonner
    x = p.read_excel('support_uke_24.xlsx', usecols='A:D')

    #Lagrer data i array
    u_dag = x.iloc[:, 0].to_numpy()
    kl_slett = x.iloc[:, 1].to_numpy()
    varighet = x.iloc[:, 2].to_numpy()
    score = x.iloc[:, 3].to_numpy()

    #Returnerer variabler
    return u_dag, kl_slett, varighet, score