import numpy as np
from scipy.stats import rv_discrete, kurtosis, skew
import random
import matplotlib.pyplot as plt

#1. tworzenie tablicy z wartościami z tabeli
X = np.array([1,2,3,6,7,9])
PX = np.array([0.1, 0.15, 0.05, 0.2, 0.1, 0.4])

#rozkład prawdopodobieństwa 
distribution = rv_discrete(name='rozkład prawdopodobieństwa', values=(X,PX))

#2.
#pętla, powtórzenie eksperymentu 10000 razy
samples = [5, 25, 50]
number = 10000
bins=20 

fig, axs = plt.subplots(1, len(samples), figsize=(15, 5)) #siatka do utworzenia 3 wykresów

for i, n in enumerate(samples):
    SampleDst=[]  #tablica do przechowania wartości średnich
     #pętla żeby powtórzyć 10 000 razy
    for k in range(number):
        #Generowanie kolejno 5, 25, 50 próbek
        random_sample = distribution.rvs(size=n)
        #Wyznaczenie średniej μ
        sample_mean = np.mean(random_sample)
        #Dodanie średniej do tablicy
        SampleDst.append(sample_mean)

#Histogram rozkładu próbkowego średniej
    axs[i].hist(SampleDst, bins=np.linspace(min(SampleDst), max(SampleDst), bins+1),
                density=True, alpha=0.6, color='g', edgecolor='black')
    
    axs[i].set_title(f'Histogram dla n={n}')
    axs[i].set_xlabel('Średnia')
    axs[i].set_ylabel('Prawdopodobieństwo')
    plt.show()   

plt.hist(SampleDst, bins=20, density=True, color='red', edgecolor='black')
plt.title('Rozkład próbkowy średniej')
plt.xlabel('Średnia')
plt.ylabel('Prawdopodobieństwo')
plt.legend()
plt.show() 