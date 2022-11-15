# -*- coding: utf-8 -*-
"""federated_netflix_presentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JUI2atEMuKnseqhxnDvgfDOOclffsnpl
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

def make_plot_interval(data, name):
  plt.figure(figsize=(15, 5))

  plt.subplot(121)

  plt.plot(data.Runda, data.Funkcja_kosztu)
  plt.fill_between(data.Runda, (data.Funkcja_kosztu-data.AVG_loss), (data.Funkcja_kosztu+data.AVG_loss), color='b', alpha=.1)

  plt.ylabel('Funkcja kosztu')
  plt.xlabel('Runda')
  plt.title('Funkcja kosztu ' + name)

  plt.subplot(122)

  plt.plot(data.Runda, data.Dokładność)
  plt.fill_between(data.Runda, (data.Dokładność-data.AVG_acc), (data.Dokładność+data.AVG_acc), color='b', alpha=.1)

  plt.ylabel('Dokładność')
  plt.xlabel('Runda')
  plt.title('Dokładność ' + name)
  plt.show()

data = pd.read_csv('/content/drive/MyDrive/inz/matrix.csv')

data = data.rename(
      columns={'Column1' : 'film',
               'Column2' : 'Runda',
               'Column3' : 'Funkcja_kosztu',
               'Column4' : 'Dokładność',
               'Column5' : 'AVG_loss',
               'Column6' : 'AVG_acc'})

print(data.head())

data_200 = data[data.film == 200]
data_500 = data[data.film == 500]
data_1000 = data[data.film == 1000]
data_2000 = data[data.film == 2000]
data_3000 = data[data.film == 3000]
data_4000 = data[data.film == 4000]
data_5000 = data[data.film == 5000]

data = data.rename(
      columns={'film' : 'ilość filmów'})
  
  plt.figure(figsize=(15, 5))

  plt.subplot(121)

  sns.lineplot(data = data, x = 'Runda', y = 'Funkcja_kosztu', hue = 'ilość filmów' , palette = 'dark')

  plt.ylabel('Funkcja kosztu')
  plt.xlabel('Runda')
  plt.title('Funkcja kosztu')

  plt.subplot(122)

  sns.lineplot(data = data, x = 'Runda', y = 'Dokładność', hue = 'ilość filmów' , palette = 'dark')

  plt.ylabel('Dokładność')
  plt.xlabel('Runda')
  plt.title('Dokładność')
  plt.show()

make_plot_interval(data_200, " dla bazy z 200 filmami")
make_plot_interval(data_500, " dla bazy z 500 filmami")
make_plot_interval(data_1000, " dla bazy z 1000 filmami")
make_plot_interval(data_2000, " dla bazy z 2000 filmami")
make_plot_interval(data_3000, " dla bazy z 3000 filmami")
make_plot_interval(data_4000, " dla bazy z 4000 filmami")
make_plot_interval(data_5000, " dla bazy z 5000 filmami")

from tabulate import tabulate

table = [['ilość filmów', 'funkcja kosztu', 'średni poziom ufności funkcji kosztu', 'dokładność', 'średni poziom ufności dokładności'],
         [str(200), str(data_200['Funkcja_kosztu'].min()), str(data_200['AVG_loss'].mean()), str(data_200['Dokładność'].max()), str(data_200['AVG_acc'].mean())],
         [str(500), str(data_500['Funkcja_kosztu'].min()), str(data_500['AVG_loss'].mean()), str(data_500['Dokładność'].max()), str(data_500['AVG_acc'].mean())],
         [str(1000), str(data_1000['Funkcja_kosztu'].min()), str(data_1000['AVG_loss'].mean()), str(data_1000['Dokładność'].max()), str(data_1000['AVG_acc'].mean())],
         [str(2000), str(data_2000['Funkcja_kosztu'].min()), str(data_2000['AVG_loss'].mean()), str(data_2000['Dokładność'].max()), str(data_2000['AVG_acc'].mean())],
         [str(3000), str(data_3000['Funkcja_kosztu'].min()), str(data_3000['AVG_loss'].mean()), str(data_3000['Dokładność'].max()), str(data_3000['AVG_acc'].mean())],
         [str(4000), str(data_4000['Funkcja_kosztu'].min()), str(data_4000['AVG_loss'].mean()), str(data_4000['Dokładność'].max()), str(data_4000['AVG_acc'].mean())],
         [str(5000), str(data_5000['Funkcja_kosztu'].min()), str(data_5000['AVG_loss'].mean()), str(data_5000['Dokładność'].max()), str(data_5000['AVG_acc'].mean())],
        ]
         
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))