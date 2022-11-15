# -*- coding: utf-8 -*-
"""federated_differential_cifar_presentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pm9ti6if-S8nmqr7MZhDV-c2SAN7R56N
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

def make_plot(data_frame, title, if_10 = False):
  plt.figure(figsize=(15, 5))
  dff = data_frame.rename(
      columns={'AVG_acc': 'Dokładność',
               'AVG_loss': 'Funkcja kosztu',
               'Column2': 'Runda',
               'Column3' : 'Liczba serwerow'})
  print(dff.columns)

  plt.subplot(121)
  plt.title('Dokładność dla ' + title)
  p1 = sns.lineplot(data=dff, x='Runda', y='Dokładność', hue='Liczba serwerow', palette='dark')
  plt.subplot(122)
  plt.title('Funkcja kosztu dla ' + title)
  p2 = sns.lineplot(data=dff, x='Runda', y='Funkcja kosztu', hue='Liczba serwerow', palette='dark')

def make_plot_normal(data_frame, title):
  plt.figure(figsize=(15, 5))
  dff = data_frame.rename(
      columns={'accuracy': 'Dokładność',
               'loss': 'Funkcja kosztu',
               'epoch': 'Runda'})
  print(dff.columns)

  plt.subplot(121)
  plt.title('kosztu dla ' + title)
  plt.plot(dff['Runda'],dff['Funkcja kosztu'])
  plt.fill_between(dff['Runda'], (dff['Funkcja kosztu']-dff['interval_loss']), (dff['Funkcja kosztu']+dff['interval_loss']), color='b', alpha=.1)
  plt.subplot(122)
  plt.title('dokldamodść dla ' + title)
  plt.plot(dff['Runda'],dff['Dokładność'])
  plt.fill_between(dff['Runda'], (dff['Dokładność']-dff['interval_acc']), (dff['Dokładność']+dff['interval_acc']), color='b', alpha=.1)


def smaller_sampling(data_frame):
  to_delete = []
  delete = 0
  for i in range(len(data_frame)):
    if delete == 1:
      to_delete.append(i)
      delete = 0
    else:
      delete = 1
  return data_frame.drop(data_frame.index[to_delete])

def make_plot_interval(data_frame, title):
  plt.figure(figsize=(15, 5))
  dff = data_frame.rename(
      columns={'AVG_acc': 'Dokładność',
               'AVG_loss': 'Funkcja kosztu',
               'Column2': 'Runda',
               'Column3' : 'Liczba serwerow'})

  plt.subplot(121)
  plt.title('kosztu dla ' + title)
  plt.plot(dff['Runda'],dff['Funkcja kosztu'])
  plt.fill_between(dff['Runda'], (dff['Funkcja kosztu']-dff['interval_loss']), (dff['Funkcja kosztu']+dff['interval_loss']), color='b', alpha=.1)
  plt.subplot(122)
  plt.title('dokldamodść dla ' + title)
  plt.plot(dff['Runda'],dff['Dokładność'])
  plt.fill_between(dff['Runda'], (dff['Dokładność']-dff['interval_acc']), (dff['Dokładność']+dff['interval_acc']), color='b', alpha=.1)
  plt.ylim(0, 0.03)

buffor = pd.read_csv('/content/drive/MyDrive/inz/cifar_all_to_notebook.csv')
buffor = smaller_sampling(buffor)

buffor.head()

make_plot(buffor, "dla wszystkich ilości serwerów w rundzie ")

buffor = pd.read_csv('/content/drive/MyDrive/inz/CIFAR_ALL_NORMAL_to_notebook.csv')
make_plot_normal(buffor, "dla normalnego modelu")

buffor_10 = buffor[buffor.Column3 == 10]
make_plot_interval(buffor_10, "dla 10 serwerów w rundzie")

buffor_30 = buffor[buffor.Column3 == 30]
make_plot_interval(buffor_30, "dla 30 serwerów w rundzie")

buffor_50 = buffor[buffor.Column3 == 50]
make_plot_interval(buffor_50, "dla 50 serwerów w rundzie")

buffor_70 = buffor[buffor.Column3 == 70]
make_plot_interval(buffor_70, "dla 70 serwerów w rundzie")

buffor_100 = buffor[buffor.Column3 == 100]
make_plot_interval(buffor_100, "dla 100 serwerów w rundzie")

buffor.columns

from tabulate import tabulate

table = [['ilość serwerów w rundzie', 'funkcja kosztu', 'średni poziom ufności funkcji kosztu', 'dokładność', 'średni poziom ufności dokładności'],
         [str(10),  str(buffor_10['AVG_loss'].min()), str(buffor_10['interval_loss'].mean()), str(buffor_10['AVG_acc'].max()), str(buffor_10['interval_acc'].mean())],
         [str(30),  str(buffor_30['AVG_loss'].min()), str(buffor_30['interval_loss'].mean()), str(buffor_30['AVG_acc'].max()), str(buffor_30['interval_acc'].mean())],
         [str(50),  str(buffor_50['AVG_loss'].min()), str(buffor_50['interval_loss'].mean()), str(buffor_50['AVG_acc'].max()), str(buffor_50['interval_acc'].mean())],
         [str(70),  str(buffor_70['AVG_loss'].min()), str(buffor_70['interval_loss'].mean()), str(buffor_70['AVG_acc'].max()), str(buffor_70['interval_acc'].mean())],
         [str(100),  str(buffor_100['AVG_loss'].min()), str(buffor_100['interval_loss'].mean()), str(buffor_100['AVG_acc'].max()), str(buffor_100['interval_acc'].mean())],
         ['N/A', str(buffor['loss'].min()), str(buffor['interval_loss'].mean()), str(buffor['accuracy'].max()), str(buffor['interval_acc'].mean())]]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))