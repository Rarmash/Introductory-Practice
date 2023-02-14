'''
Определить является ли заданное натуральное число простым.
'''

def func1(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return True if c == 2 else False

print(func1(int(input())))