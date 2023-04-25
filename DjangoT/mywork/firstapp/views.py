from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import testing
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.




def index(request):
    feat = testing.objects.all()
    return render(request, 'index.html', {'feats': feat})

def counter(request):
    word = request.POST['words']
    amount=len(word.split())


    return render(request, 'counter.html', {'ammount': amount} )


def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['username']
        password2 = request.POST['username']
        try:
            if password == password2 :
                    if User.objects.filter(email= email).exists():
                        messages.info(request, 'user email register')
                        return redirect('register')
                    elif User.objects.filter(username= username).exists():
                        messages.info(request,'user name  regiter')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save();
                        username =''
                        password =''
                        return redirect('login')
                    
            else:
                    messages.info(request,'password does not match')
                            
                    return redirect('register')
            

        except:
             messages.info(request,'all field must be fill')
         
         
                    

                
            



            

    return render(request,'register.html')


def onepage(request):
    
   


    return render(request, 'onepage.html' )


def login(request):
    messages.info(request, 'account created login now')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        username.str()
        password.str()


        user = auth.authenticate(username=username,password=password)

        if user is  not None:
            return redirect('/')
        else:
            messages.info(request,'username or passwrd error register or login with the riht details')
            return redirect('login')
            
        
        
    


    return render(request,'login.html')




