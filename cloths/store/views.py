from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Sum, Avg
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .models import ClothsData, CategoryData
from .forms import ClothsDataForm, DeleteForm


def index(request):

    clothes_list = ClothsData.tmp.all().select_related('cat', 'user')
    paginator = Paginator(clothes_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Главная страница сайта',
        'clothes_list': clothes_list,
        'page_obj': page_obj,
    }

    return render(request, 'store/index.html', context)


def about(request):
    list_cloths = ClothsData.objects.all()
    users = User.objects.all()

    paginator = Paginator(list_cloths, 3)

    count_stuff = CategoryData.objects.annotate(count=Count('clothsdata__pk'))
    average_price = ClothsData.objects.aggregate(avg_prc=Avg('price'))
    tmp = round(average_price['avg_prc'])

    return render(request, 'store/about_us.html', {
        'users': users,
        'avg_price': tmp,
        'count_stuff': count_stuff
    })


def adding(request):
    error = ''
    if request.method == "POST":
        form = ClothsDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = ClothsDataForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'store/adding.html', context)


def year(request, yearid):
    if yearid > 2022:
        return redirect('home')
    return HttpResponse(f'Now is {yearid} year')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>This page is not found</h1>')


def item(request, itemid):
    cloth = ClothsData.objects.get(pk=itemid)
    return render(request, 'store/item.html',
                  {
                      'cloth': cloth,
                  }
                  )


def about_th(request):
    return render(request, 'store/about_thing.html')


def buy(request, buyid):
    cloth = ClothsData.objects.get(id=int(buyid))
    return render(request, 'store/buy.html',
                  {
                      'cloth': cloth,
                  }
                  )


def support(request):
    return render(request, 'store/support.html')


def basket(request):
    return render(request, 'store/basket.html')


def delete(request, item_id):
    delete_object = get_object_or_404(ClothsData, pk=int(item_id))

    if request.method == 'POST':
        form = DeleteForm(request.POST, instance=delete_object)

        if form.is_valid():  # checks CSRF
            delete_object.delete()
            return redirect('home')  # wherever to go after deleting

    else:
        form = DeleteForm(instance=delete_object)

    return redirect('home')
