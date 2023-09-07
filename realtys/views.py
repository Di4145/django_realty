from django.shortcuts import render
from realtys.models import Realty, RealtyType
from django.db.models import Q
# Create your views here.


def index(request):
    realty = Realty.objects.all()
    return render(request, 'index.html', {'realty': realty})

def search(request):
    text_q = request.GET.get('text')
    price1_q = request.GET.get('price1')
    price2_q = request.GET.get('price2')
    s1_q = request.GET.get('s1')
    s2_q = request.GET.get('s2')
    type_q = request.GET.get('type')


    if text_q:
        text = text_q.split()
        q_object = Q()
        for i in text:
            q_object &= (Q(info__iregex=i) | Q(header__iregex=i))
        realtys = Realty.objects.filter(q_object)
    else:
        realtys = Realty.objects.all()

    if price1_q:
        realtys = realtys.filter(cost__gte=price1_q)

    if price2_q:
        realtys = realtys.filter(cost__lte=price2_q)

    if s1_q:
        realtys = realtys.filter(s__gte=s1_q)

    if s2_q:
        realtys = realtys.filter(s__lte=s2_q)

    if type_q:
        realtys = realtys.filter(type=type_q)

    types = RealtyType.objects.all()

    return render(request, 'search.html', {'realtys': realtys, 'types': types})


def detail(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty})