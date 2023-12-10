from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.uav_app.forms import RentalForm

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'contact/contact.html')


@login_required
def ucav(request):
    return render(request, 'ucav/list.html')


def ucav_detail(request, pk):
    return render(request, 'ucav/detail.html', {'pk':pk})


@login_required
def rent_ucav(request, pk):
    form = RentalForm()
    return render(request, 'ucav/rent.html', {'pk':pk, 'form':form})


@login_required
def list_rentals(request):
    return render(request, 'rental/list.html')


@login_required
def edit_rental(request, pk):
    return render(request, 'rental/edit.html', {'pk':pk})