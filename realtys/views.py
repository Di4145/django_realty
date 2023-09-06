from django.shortcuts import render
from realtys.models import Realty
# Create your views here.


def index(request):
    realty = Realty.objects.all()
    return render(request, 'index.html', {'realty': realty})

def search(request):
    text_q = request.GET.get('text')
    price1_q = request.GET.get('price1')
    price2_q = request.GET.get('price2')

    if text_q:
        realtys = Realty.objects.filter(info__iregex=text_q)
    else:
        realtys = Realty.objects.all()

    if price1_q:
        realtys = realtys.filter(cost__gte=price1_q)

    if price2_q:
        realtys = realtys.filter(cost__lte=price2_q)



    return render(request, 'search.html', {'realtys': realtys})


def detail(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty})