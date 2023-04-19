class person:
    head =1
    hand = 2
    legs  = 2
    eyes = 2
x = person()
print(x.head)


class car:
    def __init__(self, name , age):
        self.name = name
        self.age = age

x = car('peter',43)
print(x.age)