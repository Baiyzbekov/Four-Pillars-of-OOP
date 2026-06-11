class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass
dog = Dog()
dog.eat()

#Dog inherits the eat() method from Animal