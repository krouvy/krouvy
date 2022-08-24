year = int(input('Введи год '))
print(year % 4 == 0)
print((not(year % 400) or (not(year % 4) and (year % 100))))