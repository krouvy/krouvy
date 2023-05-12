with open('input', encoding='utf8') as file:
    print('Двоишники')
    for student in file:
        if int(student.split()[-1]) < 3:
            print(student.strip())
