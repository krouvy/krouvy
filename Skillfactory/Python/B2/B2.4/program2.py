path = '/home/user/documents/file.txt'

listPath = path[1:].split('/')

print(listPath) # разделитель можно указать в качестве аргумента

print('\\'.join(listPath))
