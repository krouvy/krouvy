num = input('Введите палиндром ')

print(num, '- палиндром' if num == num[::-1] else '- не палиндром')