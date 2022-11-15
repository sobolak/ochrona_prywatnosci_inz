import numpy
import pandas as pd
import random as rand

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

for qqq in [200, 500, 1000, 2000, 3000, 4000, 5000]:

    list_of_film = []

    for i in range(qqq):
        list_of_film.append(i)

    # print(list_of_film)

    # rand.shuffle(list_of_film)

    # print(list_of_film)

    current_user = records[0].split(",")[1]
    records[0].split(",")[4] = list_of_film[-1]
    grades = {}

    for cybant in list_of_film:
        grades[cybant] = rand.randint(1,5)

    # print(len(grades))
    # print(len(records))

    # print(grades)

    file_name = 'data_' + str(qqq) + '_5.txt'

    with open(file_name, 'w') as xxx:
        counter = 0
        list_of_grades = [1,2,3,4,5]
        for buff in records:
            splited = buff.split(",")
            if splited[1] != current_user:
                current_user = splited[1]
                counter = 0
                rand.shuffle(list_of_film)
            
            if qqq == 200 or qqq == 500 or qqq == 1000:

                if int(grades[list_of_film[counter]]) == 1:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.85, 0.05, 0.05, 0.02, 0.03])
                elif int(grades[list_of_film[counter]]) == 2:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.85, 0.01, 0.06, 0.03])
                elif int(grades[list_of_film[counter]]) == 3:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.06, 0.02, 0.85, 0.03, 0.04])
                elif int(grades[list_of_film[counter]]) == 4:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.03, 0.03, 0.04, 0.85, 0.05])
                elif int(grades[list_of_film[counter]]) == 5:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.03, 0.05, 0.04, 0.03, 0.85])

            elif qqq == 2000:
                if int(grades[list_of_film[counter]]) == 1:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.81, 0.06, 0.06, 0.03, 0.04])
                elif int(grades[list_of_film[counter]]) == 2:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.06, 0.81, 0.02, 0.07, 0.04])
                elif int(grades[list_of_film[counter]]) == 3:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.07, 0.03, 0.81, 0.04, 0.05])
                elif int(grades[list_of_film[counter]]) == 4:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.04, 0.04, 0.05, 0.81, 0.06])
                elif int(grades[list_of_film[counter]]) == 5:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.04, 0.06, 0.05, 0.04, 0.81])
            elif qqq == 3000:
                if int(grades[list_of_film[counter]]) == 1:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.8, 0.07, 0.08, 0.02, 0.03])
                elif int(grades[list_of_film[counter]]) == 2:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.8, 0.05, 0.07, 0.03])
                elif int(grades[list_of_film[counter]]) == 3:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.06, 0.05, 0.8, 0.05, 0.04])
                elif int(grades[list_of_film[counter]]) == 4:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.06, 0.04, 0.8, 0.05])
                elif int(grades[list_of_film[counter]]) == 5:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.03, 0.06, 0.04, 0.07, 0.8])
            elif qqq == 4000:
                if int(grades[list_of_film[counter]]) == 1:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.8, 0.05, 0.05, 0.05, 0.05])
                elif int(grades[list_of_film[counter]]) == 2:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.8, 0.06, 0.06, 0.03])
                elif int(grades[list_of_film[counter]]) == 3:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.06, 0.07, 0.8, 0.03, 0.04])
                elif int(grades[list_of_film[counter]]) == 4:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.03, 0.08, 0.04, 0.8, 0.05])
                elif int(grades[list_of_film[counter]]) == 5:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.07, 0.05, 0.04, 0.04, 0.8])
            elif qqq == 5000:
                if int(grades[list_of_film[counter]]) == 1:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.78, 0.05, 0.05, 0.07, 0.05])
                elif int(grades[list_of_film[counter]]) == 2:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.78, 0.06, 0.06, 0.05])
                elif int(grades[list_of_film[counter]]) == 3:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.06, 0.07, 0.78, 0.05, 0.04])
                elif int(grades[list_of_film[counter]]) == 4:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.08, 0.04, 0.78, 0.05])
                elif int(grades[list_of_film[counter]]) == 5:
                    grade = numpy.random.choice(numpy.arange(1, 6), p=[0.05, 0.05, 0.09, 0.03, 0.78])


            xxx.write("%s\n" % str(str(splited[1])+","+str(grade)+","+str(splited[3])+","+str(list_of_film[counter])))
            counter += 1
    