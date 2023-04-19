try:

    name = int(input('enter a number: '))
    print(name)
except:
    print('check your input something went wrong')
else:
    print('nothing when wrong')
finally:
    print('try expect finish')
    