class Person:
    arms_count = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi {self.name}")

    def __str__(self):
        return f"Person<name={self.name}>"



me = Person('Nick')
clone = Person("Nick")
you = Person('Cage')

print(me, you)
print(me == clone)
print(me.name, you.name)

print(len(dir(Person)), sep="\n")
print(*dir(Person), sep="\n")

