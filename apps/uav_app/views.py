from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'contact/contact.html')

@login_required
def ucav(request):
    return render(request, 'ucav/list.html')