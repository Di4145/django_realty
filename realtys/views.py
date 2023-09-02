from django.shortcuts import render
from realtys.models import Realty
# Create your views here.


def index(request):
    realty = Realty.objects.all()
    return render(request, 'index.html', {'realty': realty})

def search(request):
    realtys = Realty.objects.all()
    return render(request, 'search.html', {'realtys': realtys})


# def details(request):
#     realty = Realty.objects.all()
#     return render(request, 'detail.html', )