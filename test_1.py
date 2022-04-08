import datetime


with open('file.txt', 'a') as file:
    for i in range(1, 301):
        now = datetime.datetime.now()
        file.writelines([str(i), ' ' * (4-len(str(i))), str(now.second), ' ' * 2, str(now.microsecond), '\n'])

