from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    randpassword=''

    charcters =list('abcdefghijklmnnopqrstuvwxyz')
    length = int(request.GET.get('length', 13))
    if request.GET.get('uppercase'):
        charcters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        charcters.extend(list('01234456789'))
    if request.GET.get('specialCharacter'):
        charcters.extend(list('!@#$%^&*(){}[]?><.,:'))

    for x in range(length):
        randpassword+= random.choice(charcters)

    return render(request, 'generator/password.html', {'password':randpassword})

