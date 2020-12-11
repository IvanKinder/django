from django.shortcuts import render

from authapp.models import ShopUser


# Users

def user_create(request):
    pass


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
