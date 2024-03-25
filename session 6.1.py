import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete, kurtosis, skew

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





