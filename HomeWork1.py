class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

lion = Animal('lion', 10, 200)
zebra = Animal('zebra', 5, 120)
camel = Animal('camel', 15, 250)
hawk = Animal('hawk', 3, 25)

print(lion.name, lion.age, lion.weight)
print(zebra.name, zebra.age, zebra.weight)
print(camel.name, camel.age, camel.weight)
print(hawk.name, hawk.age, hawk.weight)