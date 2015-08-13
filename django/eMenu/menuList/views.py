from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

from .models import Menu


def home(request):
    order = request.GET.get('order')

    if order == 'name':
        menu_list = Menu.objects.exclude(meals=None) \
                        .annotate(Count('meals')).order_by('name')
    elif order == 'meals':
        menu_list = Menu.objects.exclude(meals=None) \
                        .annotate(Count('meals')).order_by('meals__count')
    else:
        order = 'id'
        menu_list = Menu.objects.exclude(meals=None).annotate(Count('meals'))

    paginator = Paginator(menu_list, 3)

    page = request.GET.get('page')
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        menus = paginator.page(1)
    except EmptyPage:
        menus = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {'menus': menus, 'order': order})


def menu(request):
    pass
