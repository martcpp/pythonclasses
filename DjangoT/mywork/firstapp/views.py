from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "partrick"
    return render(request, 'index.html', {'name': name})

def counter(request):
    word = request.POST['words']
    amount=len(word.split())


    return render(request, 'counter.html', {'ammount': amount} )