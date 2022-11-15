import pandas as pd

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