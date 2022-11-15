import pandas as pd

def add_film_id(input_file, output_file, films_output):
    with open(input_file) as input:
        records = input.readlines()

    films_statistic = {}
    film = records[0][:-2]

    counter = 1
    number_of_ratings_per_film = 0

    print("start of " + input_file)

    for record in records[1:-1]: #-1
        if record[-2] == ":":
            films_statistic.update({film : number_of_ratings_per_film})
            number_of_ratings_per_film = 0
            film = record[:-2]
        else:
            try:
                records[counter] = str(records[counter][:-1]) + "," + str(film)
                number_of_ratings_per_film += 1
            except:
                pass
        if counter % 1000000 == 0:
            print(counter)
        counter += 1

    with open(output_file, 'w') as output:
        for record in records[:-1]:
            output.write("%s\n" % record)
        print(output_file + ' correctly saved')

    with open(films_output, 'w') as q:
        q.write("%s" % films_statistic)


def del_film_id(input_file, output_file):
    with open(input_file) as input:
        records = input.readlines() 
    
    counter = 0

    for record in records: #-1
        try:
            if record[-2] == ":":
                records.pop(counter)
        except:
            pass
        if counter % 1000000 == 0:
            print(counter)
        counter += 1


    with open(output_file, 'w') as output:
        for record in records:
            output.write("%s" % record)
        print(output_file + ' correctly saved')
    

def make_client_stats(input_file, clients_statistic):
    with open(input_file) as input:
        records = input.readlines()

    for record in records:
        buff = record.split(',')
        clients_statistic.update({buff[0] : key_value(buff[0], clients_statistic)})
    
    print(clients_statistic)

def key_value(key, dict):
    try:
        return dict[key]
    except:
        return 0 

def get_high_quality_users(files):
    for file in files:
        x = pd.read_csv(files, header = None, names = ['client', 'rating', 'data', 'film'])

        list_of_users = list(set(x.client))

        print(len(list_of_users)) 

        counter = 0
        users_to_use = []
        list_of_max = []

        for user in list_of_users:        
            user_ratings = x[x.client == user]
            buffor = len(user_ratings) 
            if buffor > 100 and buffor < 170:
                counter += 1
                users_to_use.append(user)
                list_of_max.append(buffor)
                if counter % 2000 == 0 :
                    break

    with open('files/list_buffor.txt', 'w') as f:
        for user in users_to_use:
            f.write("%s\n" % user)
        print("DONE")

add_film_id('files/combined_data_1.txt', 'files/data_1_buff.txt', 'files/films_1.txt')
add_film_id('files/combined_data_2.txt', 'files/data_2_buff.txt', 'files/films_2.txt')
add_film_id('files/combined_data_3.txt', 'files/data_3_buff.txt', 'files/films_3.txt')
add_film_id('files/combined_data_4.txt', 'files/data_4_buff.txt', 'files/films_4.txt')

# make_client_stats('files/data_1.txt', {})

del_film_id('files/data_1_buff.txt', 'files/data_1.txt')
del_film_id('files/data_2_buff.txt', 'files/data_2.txt')
del_film_id('files/data_3_buff.txt', 'files/data_3.txt')
del_film_id('files/data_4_buff.txt', 'files/data_4.txt')

get_high_quality_users(['files/data_1.txt','files/data_2.txt','files/data_3.txt','files/data_4.txt'])

with open('files/really.txt') as input:
    records = input.readlines()

with open('files/list_buffor.txt') as input_2:
    users_to_use = input_2.readlines()


x = pd.read_csv('files/really.txt', header = None, names = ['client', 'rating', 'data', 'film'])

output = []
list_of_max = []

counter = 0

for user in users_to_use:
    user_ratings = x[x.client == int(user)]
    list_of_max.append(len(user_ratings))
print(max(list_of_max))
for hehe in list_of_max:
    if max(list_of_max) == list_of_max[counter]:
        break
    counter += 1

user_ratings = x[x.client == int(users_to_use[counter])]
list_of_film = list(set(user_ratings.film))

list_of_film = []

for i in range(200):
    list_of_film.append(i)