# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e8VV8NcB1c0bHwtujVutErivPmOsl4Vg
"""

#Lucru cu Liste
#1. Creare lista file adaugate in septembrie 2021
filmesept21 = ["Blood Brothers: Malcolm X & Muhammad Ali","Paradise Hills","JJ+E", "Show Dogs", "If I Leave Here Tomorrow: A Film About Lynyrd Skynyrd","Untold: Breaking Point","Shadow Parties","Angamaly Diaries","A Champion Heart",
   "Worth","Afterlife of the Party","Anjaam","Bright Star","Dhanak","Final Account","Gurgaon","Here and There","In the Cut","Shikara","A Cinderella Story","Agatha Christie's Crooked House" ]
print("Lista de de file din septembrie 2021")
print(filmesept21)

#2. Lungimea listei de filme
print("Lungime lista:")
print(len(filmesept21))

#3. Adaugarea filmului Blade Runner: The Final Cut la finalul listei
filmesept21.append("Blade Runner: The Final")
print("Dupa adaugarea filmului in lista:")
print(filmesept21)

#4. Adaugarea filmului Chappie pe pozitia 5 
filmesept21.insert(5,"Chappie")
print("Dupa adaugarea filmului pe pozitia 5:")
print(filmesept21)

#5. Eliminarea filmului Chappie
filmesept21.remove("Chappie")
print("Dupa eliminarea filmului:")
print(filmesept21)

#6. Inlocuirea primului film cu filmul 
filmesept21[0]="Cliffhanger"
print("Dupa inlocuirea primului film:")
print(filmesept21)

#7. Extragerea filmului de pe pozitia 1 
print("Filmul de pe pozitia 1 este:")
filmesept21.pop(1)

#8. Inversarea elementelor listei de filme
filmesept21.reverse()
print("Dupa inversarea listei de filme:")
print(filmesept21)

#9. Golire listei
filmesept21.clear()
print("Lista:")
print(filmesept21)

#LUCRUL CU DICTIONARE 
#1. Creare dictionar si afisarea lui
filmesidirectori = {"Dick Johnson Is Dead":"Kirsten Johnson","My Little Pony: A New Generation":"Robert Cullen","Sankofa":"Haile Gerima","The Starling":"Theodore Melfi","Je Suis Karl":"Christian Schwochow","Europe's Most Dangerous Man: Otto Skorzeny in Spain":"Pedro de Echave GarcÃ­a, Pablo AzorÃ­n Williams"}
print("Dictionar:")
print(filmesidirectori)

#2. Afisarea directorului care regizeaza filmul Dick Johnson Is Dead
print("Filmul Dick Johnson Is Dead este regizat de directorul:")
print(filmesidirectori.get("Dick Johnson Is Dead"))

#3. Corespondenta dintre filme si regizor
print("Corespondenta dintre filme si regizori:")
print(filmesidirectori.items())

#4.Eliminarea filmului The Starling
print("Dupa eliminarea filmului The Starling:")
filmesidirectori.pop('The Starling')

#5.Filmele din dictionar
print("Filmele din dictionar  sunt:")
print(filmesidirectori.keys())

#6. Directorii filmelor
print("Directorii filmelor sunt:")
print(filmesidirectori.values())

#LUCRUL CU SETURI 
#1. Crearea unui set care contine productiile adaugate pe data de 9 septembrie 2021
setProductiiSept2021={"Blood Brothers: Malcolm X & Muhammad Ali","Mighty Raju","Paradise Hills","The Women and the Murderer"}
print("Productii adaugate :")
print(setProductiiSept2021)

#2. Crearea unui set care contine productiile adaugate pe data de 9 septembrie 2020
setProductiiSept2020={"Cargo","Cuties","Get Organized with The Home Edit","La LÃ­nea: Shadow of Narco","So Much Love to Give","The Social Dilemma"}
print("Productii adaugate :")
print(setProductiiSept2020)

#3. Adaugarea unuei noi productii in lista anului 2020 luna septembrie
setProductiiSept2020.add("Interstellar")
print("Update:")
print(setProductiiSept2020)

#4. Productiile care au fost adaugati in 2021
print("Productii adaugate in 2021:")
print(setProductiiSept2021.difference(setProductiiSept2020))

#5.Elementele necomune 
print("Elementele necomune:")
print(setProductiiSept2021.symmetric_difference(setProductiiSept2020))

#6. Afisarea tuturor productilor care au aparut in 2020 si 2021
toateProductiile=setProductiiSept2021.union(setProductiiSept2020)
print("Toate productiile:")
print(toateProductiile)

#LUCRUL CU TUPLURI 
#1. Crearea tuplului ce contine productii din 4 iunie 2021 si afisarea lui
productii6Iunie2021=("Breaking Boundaries: The Science Of Our Planet", "Feel Good", "Fireplace 4K: Classic Crackling Fireplace from Fireplace for Your Home","Human: The World Within", "Sweet & Sour","Sweet Tooth","Trippin' with the Kandasamys","Xtreme")
print("Productii aparute in 6 iunie 2021:")
print(productii6Iunie2021)

#2. Numarul de ordine al productiei "Feel Good"
print("Numarul de ordine al serialului Feel Good este:")
print(productii6Iunie2021.index("Feel Good")+1)

#LUCRUL CU FUNCTII, STRUCTURI CONDITIONATE SI REPETITIVE
filme=["Avvai Shanmughi", "Go! Go! Cory Carson: Chrissy Takes the Wheel", "Minsara Kanavu","Grown Ups", "Dark Skies"]
data_aparitie=[1996,2021,1997,2010,2013]
durata=[161,61,147,103,97]
gen=["Comedies","Children & Family Movies","Comedies","Comedies","Horror Movies"]
#1. Functie care parcurge listele si afiseaza datele legate de actori in mod unitar
def afisare_filme(filme,data_aparitie,durata,gen):
 for i in range(len(filme)):
  film='Nume film:' +filme[i]+',data aparitie:'+str(data_aparitie[i])+',durata:'+str(durata[i])+', gen:' +gen[i]
  print(film)
afisare_filme(filme,data_aparitie,durata,gen)
print("\n")

#2. Functia care mareste durata filmului daca este sub 100 de minute transformand-o intr-o editie speciala
def marire_durata(filme,durata):
  for i in range(len(filme)):
    if durata[i]<100:
      durata[i]+=100;
#3. Functia care afiseaza datele initiale, va marii duratele, iar apoi va afisa datele actualizate
def apelare_functii(filme,data_aparitie,durata,gen):
  print("Date initiale:")
  afisare_filme(filme,data_aparitie,durata,gen)
  marire_durata(filme,durata)
  print("Date noi:")
  afisare_filme(filme,data_aparitie,durata,gen)
apelare_functii(filme,data_aparitie,durata,gen)

#4. Functia care genereaza un grafic de tip PieChart in functie de durata filemor 
import pandas as pd
import matplotlib.pyplot as plt
def PieChart(filme,durata):
  cols=['c','m','r','k','b']
  plt.pie(durata,labels=filme, colors=cols)
  plt.title('Piechart durata')
  plt.show()
PieChart(filme,durata)

from google.colab import drive
drive.mount('/content/drive')

#1. Importarea fisierului csv
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/drive/MyDrive/Python/Movies.csv', sep=',',header=0)
print(df)

#2.Folosirea funcției iloc() pentru identificarea numelui filmului
print(df.iloc[1, 1])

#3. Modificarea duratei filmului pentru adaugarea de 10 minute in plus pentru reclama cu ajutorul funcției loc()
print(df.loc[1, 'duration'])
df.loc[1,'duration'] = 109
print(df.loc[1, 'duration'])

#4. Ștergerea coloanei genului filmului
df = df.drop("listed_in", axis=1)
print(df.head())

#5. Înlocuirea valorii lipsă a venitului cu mesajul "Valoare inexistena"
df=pd.read_csv('/content/drive/MyDrive/Python/Movies.csv', sep=',',header=0, usecols=['date_added'])
print(df['date_added'])
print(df.loc[df['date_added'].isnull()])
print('-----------------------')
print(df['date_added'].fillna('Valoare inexistenta'))

#6. Stergerea filmului din lista a carui declaratie despre venit lipseste
df = df.drop([2], axis=0)
print(df.head(10))

#LUCRUL CU INNER MERGE
import pandas as pd
#1. Prima lista cu date contine numele filmelor si data cand au fost lansate.
df1=pd.DataFrame({
 "Film":["Welcome Home","The Girl and the Gun","Fireplace 4K: Classic Crackling Fireplace from Fireplace for Your Home","Vampire Academy","Awake","Copenhagen","A Haunted House 2"],
 "Data aparitie":["2018","2019","2015","2014","2021","2014","2014"],
})
df1

#2. A doua lista de date contine din nou numele filmelor si data la care au fost adaugate pe Netflix
df2=pd.DataFrame({
 "Film":["Welcome Home","The Girl and the Gun","Fireplace 4K: Classic Crackling Fireplace from Fireplace for Your Home","Vampire Academy", "Awake","Copenhagen","A Haunted House 2"],
 "Data adaugare pe Netflix":["6/2/2021","6/3/2021","6/4/2021","6/7/2021","6/9/2021","6/10/2021","6/10/2021"],
})
df2

#3. Combinatia dintre cele doua liste de date.
rez=pd.merge(df1,df2,on="Film")
rez

#GRUPAREA DATELOR ȘI PRELUCRAREA STATISTICA
#Durata filmelor si filmele adaugate pe data de 1 august 2021
import pandas as pd
df = pd.DataFrame({'Film': ['Cloudy with a Chance of Meatballs', 'Catch Me If You Can', 'Boyka: Undisputed', 'Beowulf', 'Beethoven s 2nd','Beethoven'],
 'Durata': [90, 142, 90, 114, 88, 87]
 })
df

df.groupby(['Film']).mean()

#REGRESIE LINIARA MULTIPLA
import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv('/content/drive/MyDrive/Python/Marketing.csv')
df
X = pd.DataFrame(df, columns=['Internet', 'Panou'])
y = df['Rating']
results = smf.ols('y ~ Internet + Panou', data=df).fit()
print("In urma regresiei liniare multiple avem urmatorii parametrii:\n")
print(results.params)
print(round(results.predict(df[:5])))

#CONVERSIA UNUI STRING IN INT
import pandas as pd
Data = {'Film': ['Jaws','Catch Me If You Can','The BFG'],
 'ID': ['42','330','1204']}
#Convesia din string in int
df = pd.DataFrame(Data)
df['ID'] = df['ID'].astype(int)
print (df)

#REGRESIA LOGISTICA
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
#Se efectueaza promovari in cazul departamentului de analisti de date
df=pd.read_csv('/content/drive/MyDrive/Python/Promovari.csv')
df

#Starea variabilei independente (reprezentate de x) și variabilei dependente (reprezentată de y)
x = df[['Studii', 'Experienta','Numar_Proiecte']]
y = df['Promovat']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=1)

#Aplicam regresia logistica
logistic_regression= LogisticRegression()
logistic_regression.fit(x_train,y_train)
y_pred=logistic_regression.predict(x_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actualitate'], colnames=['Predictie'])
sn.heatmap(confusion_matrix, annot=True)

print('Precizie: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

