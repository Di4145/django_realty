from django.shortcuts import render
from realtys.models import Realty, RealtyType, Bill, RealtyManager, Usd
from django.db.models import Q
from django import template



# Create your views here.


def index(request):
    title = 'Агенство недвижимости'
    managers = RealtyManager.objects.all()[:3]
    realtys = Realty.objects.all()[:5]
    return render(request, 'index.html', {'realtys': realtys, 'managers': managers, 'title': title})


def contacts(request):
    title = 'Контакты'
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = 'plotnikov-d@bk.ru'
        email_manager = 'menedger@mail.ru'
        bill_obj = Bill(name=name, email=email, subject=subject, message=message, from_email=from_email,
                        email_manager=email_manager)
        bill_obj.save()
    return render(request, 'contacts.html', {'title': title})


def search(request):
    usd = Usd.objects.last()
    rate_usd = round(1/usd.usd_now, 2)
    title = 'Поиск'
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

    return render(request, 'search.html', {'realtys': realtys, 'types': types, 'title': title, 'rate_usd': rate_usd})


def detail(request, id):
    realty = Realty.objects.get(id=id)
    title = realty.header
    if realty.sale:
        new_cost = int(realty.cost  - (realty.cost * realty.sale))
    else:
        new_cost = 0


    return render(request, 'detail.html', {'realty': realty, 'title': title, 'new_cost': new_cost})
