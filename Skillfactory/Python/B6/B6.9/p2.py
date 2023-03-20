class Animal:
    def speak(self):
        print('What?')
        raise RuntimeError("Чтобы животные разговаривали им нужен класс")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create a list of Animal objects
animals = [Dog(), Cat(), Animal()]

# Call the speak method on each object
for animal in animals:
    print(animal.speak())