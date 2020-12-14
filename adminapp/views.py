from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser


# Users
from mainapp.models import ProductCategory


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
    title = 'Админка'
    users_list = ShopUser.objects.all().order_by('is_active')
    content = {
        'objects': users_list,
        'title': title
    }
    return render(request, 'adminapp/users.html', content)


def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'update_form': edit_form
    }

    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'user_to_delete': user_item
    }
    return render(request, 'adminapp/user_delete.html', content)

# Categories

def category_create(request):
    pass


def categories(request):
    categories_list = ProductCategory.objects.all().order_by('is_active')
    content = {
        'objects': categories_list
    }

    return render(request, '', content)


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
