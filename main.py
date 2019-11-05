'''
import os
import sys
print(os.getcwd())
print('Pyton', sys.version[:5])
print()
'''

n = int(input())
#n = 3
enter = []
for i in range(n):
    enter.append([w for w in input().strip().split(';')])
#enter = [['Зенит', '3', 'Спартак', '1'], ['Спартак', '1', 'ЦСКА', '1'], ['ЦСКА', '0', 'Зенит', '2']]


answer = {}
for x in enter:
    if answer.get(x[0]) == None:
        answer[x[0]] = [0, 0, 0, 0, 0]
    if answer.get(x[2]) == None:
        answer[x[2]] = [0, 0, 0, 0, 0]

    # Всего_игр
    answer[x[0]][0] += 1
    answer[x[2]][0] += 1

    # Побед Ничьих Поражений Всего_очков
    if int(x[1]) < int(x[3]):
        answer[x[2]][1] += 1 # за победу
        answer[x[2]][4] += 3 # очков
        answer[x[0]][3] += 1 # за поражение
    elif int(x[1]) > int(x[3]):
        answer[x[0]][1] += 1 # за победу
        answer[x[0]][4] += 3 # очков
        answer[x[2]][3] += 1 # за поражение
    else:
        answer[x[0]][2] += 1 # за ничью
        answer[x[2]][2] += 1 # за ничью
        answer[x[0]][4] += 1 # очков
        answer[x[2]][4] += 1 # очков

for key, val in answer.items():
    print(key, end = ':')
    print(*val)

