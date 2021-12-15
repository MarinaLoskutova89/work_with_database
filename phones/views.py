from django.shortcuts import render, redirect, reverse

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')


    context = {

    }
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.all()
    template = 'product.html'
    context = {
        'phone': phones
    }
    return render(request, template, context)