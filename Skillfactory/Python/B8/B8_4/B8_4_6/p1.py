import time

try:
    for i in [10 - i for i in range(0, 11)]:
        file = open('file', 'a', encoding='utf8')
        file.write(f"{10 / i}\n")
        file.close()
        print(10 / i)
        time.sleep(1)

except ZeroDivisionError as error:
    print('Ошибка')
    file = open('file', 'a', encoding='utf8')
    file.write(f'{error}\n')
    file.close()
