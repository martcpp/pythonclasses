print('CREATE ACCOUNT')
username = input('username :')
password = input('password :')

print('created succufully ')

print('login into account')

username1 = input('username :')
password2 = input('password :')

if username == username1 and password == password2 :
    print('login in succusflly')
elif username == username1 and password != password2:
    print('check your pssword')
else :
    print('wrong')
