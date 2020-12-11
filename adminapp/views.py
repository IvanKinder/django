from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser


# Users

def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'update_form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users_list = ShopUser.objects.all().order_by('is_active')
    content = {
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass

# Categories

def category_create(request):
    pass


def categories(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass

# Products

def product_create(request, pk):
    pass


def products(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
