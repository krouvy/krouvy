import os

print(os.getcwd()[0:-5])  # получить текущую директорию
print(os.listdir(os.getcwd()[0:-5]))  # получить список файлов текущей