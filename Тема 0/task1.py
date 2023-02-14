'''
Определить является ли заданное натуральное число простым.
'''

def func1(n):
    if n > 0:
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
        return f'{n} - простое число' if c == 2 else f'{n} - составное число'
    else:
        return f'{n} не является натуральным числом'

print(func1(int(input())))