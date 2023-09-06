from django.shortcuts import render
from realtys.models import Realty
# Create your views here.


def index(request):
    realty = Realty.objects.all()
    return render(request, 'index.html', {'realty': realty})

def search(request):
    realtys = Realty.objects.all()
    # realtys = Realty.objects.filter(info__iregex='балкон')
    return render(request, 'search.html', {'realtys': realtys})


def detail(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty})