import pandas as pd
import random as rand

with open('files/list_buffor.txt') as input:
    users_to_use = input.readlines()

# print(len(users_to_use))

x = pd.read_csv('files/final_data_1.txt', header = None, names = ['client', 'rating', 'data', 'film'])

output = []
list_of_max = []

counter = 0

for user in users_to_use:
    user_ratings = x[x.client == int(user)]
    list_of_max.append(len(user_ratings))

# print(max(list_of_max))

for hehe in list_of_max:
    if max(list_of_max) == list_of_max[counter]:
        break
    counter += 1

# print(users_to_use[counter])
# print(list_of_max[counter])

user_ratings = x[x.client == int(users_to_use[counter])]
list_of_film = list(set(user_ratings.film))
# print(len(list_of_film))
# print(list_of_film)

for user in users_to_use:
    user_ratings = x[x.client == int(user)]
    # print(user_ratings)
    # cybant = 0
    # df = pd.DataFrame(columns=['client', 'rating', 'data', 'film'])
    # for  index, row in user_ratings.iterrows():
    #     # print(rating)
    #     # print(user_ratings)
    #     row.update(pd.DataFrame([['film'],[list_of_film[cybant]]]))
    #     df.append(row)
    #     cybant += 1
    # counter += 1
    # rand.shuffle(list_of_film)
    output.append(user_ratings)
    if counter % 10 == 0:
        print("DAWAJ SZEF - " + str(counter))

# result = pd.concat(output)
# print(len(result))
print(output[10])

# with open('files/really.txt', 'w') as xxx:
for chuj in output:
    chuj.to_csv('files/really.txt', mode='a', header=False)
print('correctly saved')
