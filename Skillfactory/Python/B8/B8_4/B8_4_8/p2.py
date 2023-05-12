with open('input', encoding='utf8') as file:
    reversList = file.readlines()
    reversList.reverse()
    for student in reversList:
        print(student.strip())
