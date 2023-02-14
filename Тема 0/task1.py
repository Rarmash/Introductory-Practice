'''
Определить является ли заданное натуральное число простым.
'''

def func1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(func1(int(input())))