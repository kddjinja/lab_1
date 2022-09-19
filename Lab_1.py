import csv
import random

k_z = 0  # счетчик записей в файле
k_z_30 = 0  # счетчик строк, где в названии больше 30 символов
flag = 0
data = input('Search for author: ')
years = ['2014', '2016', '2017']
with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    for row in list(table)[1:]:
        k_z += 1
        if len(row[1]) > 30:
            k_z_30 += 1
        lower_case = row[3].lower()
        index = lower_case.find(str(data.lower()))
        if (index != -1) and ((row[6][:4]) in years):
            print(row)
            flag = 1
    if flag == 0:
        print('Nothing found.')
print('Всего записей в файле: ', k_z)
print('Книг с названием, содержащим более 30 символов: ', k_z_30)

with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    f = open('result.txt', 'w')
    count = 1  # номер книги в выводе
    l = random.randint(1, k_z - 19)  # рандомно выбирается строка, с которой начинается запись в файл
    for row in list(table)[l:]:
        f.write(str(count) + ') ' + row[3] + ' - ' + row[1] + ' - ' + row[6][:4] + '\n')
        count += 1
        if count == 21:
            break
f.close()

with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    set_tags = set()  # множество тэгов
    for row in list(table):
        d = row[12].split('# ')
        for i in range(len(d)):
            set_tags.add('#' + d[i])
print(set_tags)

with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    giving_max = 0  # максимальное число выдач
    for row in list(table)[1:]:
        giving_max = max(giving_max, int(row[8]))

with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    count_popular = 1  # счетчик номера книги в списке популярных
    for row in list(table):
        if row[0] != 'ID':
            if int(row[8]) == giving_max:
                print(str(count_popular) + ') ' + row[1] + ' - ' + row[4] + ' - ' + row[6][:4])
                count_popular += 1
                if count_popular == 21:
                    break
