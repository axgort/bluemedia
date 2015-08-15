from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import Http404
from django.template.context_processors import csrf
from django.shortcuts import redirect

from .models import Menu, Meal
from .forms import ErrorForm


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


def menu(request, id):
    try:
        menu = Menu.objects.get(pk=id)
        meals = Meal.objects.filter(menu=menu)
    except:
        raise Http404()

    return render_to_response('details.html', {'menu': menu, 'meals': meals})


def error(request):
    if request.POST:
        form = ErrorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ErrorForm()

    context = {'form': form}
    context.update(csrf(request))

    return render_to_response('error.html', context)
