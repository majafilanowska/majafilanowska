import pandas as pd 
import os
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import rv_discrete, kurtosis, skew
import scipy.stats as stats

#Dane z tabelki
x = np.array([1, 2, 3, 6, 7, 9])
px = np.array([0.1, 0.15, 0.05, 0.2, 0.1, 0.4])
distribution = rv_discrete(name='Rozkład prawdopodobieństwa', values=(x, px))

number = 10000
samples = [5, 25, 50]
bins = 20

#Tworzenie siatki do 3 wykresów
fig, axs = plt.subplots(1, len(samples), figsize=(15, 5))

for i, n in enumerate(samples):
    SampleDst = []
   
 #Powtórzenie eksperymentu 10 000 razy
    for _ in range(number):
        random_sample = distribution.rvs(size=n)
        #Wyznaczenie średniej 
        sample_mean = np.mean(random_sample)
        #Dodanie średniej do tablicy
        SampleDst.append(sample_mean)

        kurtoza = kurtosis(SampleDst)
        skewness = skew(SampleDst)

    # Histogram
    axs[i].hist(SampleDst, bins=np.linspace(min(SampleDst), max(SampleDst), bins+1),
                density=True, alpha=0.6, color='red', edgecolor='black')
    
    axs[i].set_title(f'Histogram dla n={n}')
    axs[i].set_xlabel('Średnia')
    axs[i].set_ylabel('Prawdopodobieństwo')
plt.show()




























#4.
#wczytywanie pliku csv echomonths
file_path = "C:\\studia\\SEMESTR 3\\biostats"
file_name = "echoMonths.csv"
file = os.path.join(file_path, file_name)
data = pd.read_csv(file)
#print(data.head())

#5.
#wyodrębnienie dane z zakresu po zawale do zgonu
months = data['months_survived']
print(months)
#Wyznaczanie średniej i odchylenia standardowego
mean_months = months.mean()
std_dev_months = months.std()

#Tworzenie histogramu
plt.hist(months, bins=10, edgecolor='black')
plt.title('Histogram liczby miesięcy życia')
plt.xlabel('Liczba miesięcy')
plt.ylabel('Częstość')
plt.show()

#6.
sample_size=10
number=10000
SampleDst2=[] 
#pętla dla 10000 powtórzeń
for i in range(number):
    sample = np.random.choice(months, size=sample_size, replace=False) #losowanie 10 próbek
    srednia = np.mean(sample)
    SampleDst2.append(srednia)

print("Średnia dla 10 pierwszych losowań:", SampleDst2[:10])

#7. 
#Histogram rozkładu próbkowego średniej
plt.hist(SampleDst2, bins=10, edgecolor='black')
plt.title('Histogram rozkładu próbkowego średniej')
plt.xlabel('Średnia liczba miesięcy życia')
plt.ylabel('Częstość')
plt.show()

#kurtoza i skośność
kurtoza = kurtosis(SampleDst2)
skosnosc = skew(SampleDst2)

#Obliczenie błędu standardowego dla populacji. Błąd standardowy mierzy, jak bardzo średnia próbki różni się od prawdziwej średniej populacji.
data_error = np.std(SampleDst2, ddof=1) / np.sqrt(len(SampleDst2))

print("Wynik kurtozy:", kurtoza)
print("Wynik skośności:", skosnosc)
print("wynik błędu standardowego:",data_error)

#wyniki te sugerują, że rozkład danych jest stosunkowo bliski rozkładowi normalnemu, mając niewielką kurtozę, skośność i błąd standardowy. Jednak wartości te są stosunkowo niewielkie, co sugeruje, że różnice od rozkładu normalnego są subtelne. 

#8.
#prawdopodobieństwo, że w wylosowanej próbce 10-osobowej, średnia liczba długość życia po zawale będzie równa co najmniej 35 miesięcy
miesiace = 35
#Obliczenie prawdopodobieństwa
probability = sum(sample >= miesiace for sample in SampleDst2) / len(SampleDst2)
print(f"Prawdopodobieństwo, że średnia liczba miesięcy życia >= {miesiace}: {probability:.4f}")

#9.
#Przedział ufności 
stopien = len(SampleDst2) - 1     #liczba stopni swobody
critical = stats.t.ppf(0.975, stopien)  #wartość krytyczna wartości t dla 95% przedziału ufności
przedzial = (srednia - critical * data_error, srednia + critical * data_error) #przedział ufności
print("Przedział ufności dla średnich długości życia po zawale:", przedzial) 

#10.
roznica = 5
poziom_ufnosci = 0.95
wartosc_krytyczna = stats.norm.ppf((1+poziom_ufnosci)/2)
odchylenie = np.std(SampleDst2)
liczba_probek = ((wartosc_krytyczna*odchylenie)/roznica)**2
print("Minimalna liczba próbek:",liczba_probek)








