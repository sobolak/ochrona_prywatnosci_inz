import json
from numpy import mean
import pandas as pd

def films_to_delete(file):
    with open(file) as f:
        data = f.read()

    data = data.replace("\'", "\"")

    js = json.loads(data)

    to_delete = []

    for x in js:
        if js[x] <= 700:
            to_delete.append(int(x))

    return to_delete

def delete_small_films(data, list_to_delete, output_file):
    print(data.shape)

    counter = 0

    for film_id in list_to_delete:
        data = data.loc[data["film"] != film_id]
        if counter % 50 == 0:
            print(counter)
        counter += 1

    print(data.shape)

    data.to_csv(output_file, sep = ',', index = False)

print('1')

# film_to_delete_1 = films_to_delete('files/films_1.txt')
# film_to_delete_2 = films_to_delete('files/films_2.txt') 
# film_to_delete_3 = films_to_delete('files/films_3.txt') 
film_to_delete_4 = films_to_delete('files/films_4.txt') 

print('2')

# final_film_1 = pd.read_csv('files/data_1.txt', header = None, names = ['clienr', 'rating', 'data', 'film'])
# final_film_2 = pd.read_csv('files/data_2.txt', header = None, names = ['clienr', 'rating', 'data', 'film'])
# final_film_3 = pd.read_csv('files/data_3.txt', header = None, names = ['clienr', 'rating', 'data', 'film'])
final_film_4 = pd.read_csv('files/data_4.txt', header = None, names = ['clienr', 'rating', 'data', 'film'])

print('3')

# delete_small_films(final_film_1, film_to_delete_1, 'files/final_data_1.txt')
# delete_small_films(final_film_2, film_to_delete_2, 'files/final_data_2.txt')
# delete_small_films(final_film_3, film_to_delete_3, 'files/final_data_3.txt')
delete_small_films(final_film_4, film_to_delete_4, 'files/final_data_4.txt')

print('4')

# for film_id in film_to_delete_1:
#     x = x[x['film'].str.contains(film_id) == False]

# print(x.head())        counter += 1
