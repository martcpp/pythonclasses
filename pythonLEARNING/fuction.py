def greetings(name):
    print('Welcome to my learning ', name)

greetings(4) 


def salutes(*names):
    print('greeting to you ', names[2])
salutes('obi','ade','ada')

def addNumber(num1,num2):
    return num1+num2
x = int(input('enter num1: '))
y = int(input('enter num1: '))
print(addNumber(x,y))

