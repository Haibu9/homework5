import random

def rand():
    vars = []
    for i in range(3, 21):
        vars.append(i)
    y = random.choice(vars)
    return y

def calculations(x):
    otvet = ''
    for i in range(1, 20):
        for j in range(1, 20):
            if x % (i + j) == 0 and i < j:
                otvet = f'{otvet}{i}{j}'
    return otvet


q = rand()
print('На левой табличке число: ', q)
a = calculations(q)
print('Пароль: ', a)