class PersonList:
    def __init__(self, ages):
        self.agesList = [{'Age': Person(age)} for age in ages]

        print(self.agesList)

        for i in self.agesList:
            for key, value in i.items():
                print(key, value.age)

    def GetAgePopularity(self):
        map = {}
        for i in self.agesList:
            for key, value in i.items():
                if value.age in map.keys():
                    map[value.age] += 1
                else:
                    map[value.age] = 1
        return map


class Person:
    def __init__(self, age):
        self.age = age


pl = PersonList([18, 44, 18])
print(pl.GetAgePopularity())
