import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'Главная', 'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []

def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]

def get_same_products(hot_product):
    return Product.objects.filter(category__pk=hot_product.category.pk).exclude(pk=hot_product.pk)[:3]


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    # quantity_and_price = []
    # if request.user.is_authenticated:
    #     all_products = 0
    #     all_price = 0
    #     for basket in Basket.objects.filter(user=request.user):
    #         all_products += basket.count()
    #         all_price += basket.count() * basket.product.price
    #     quantity_and_price.append(all_products)
    #     quantity_and_price.append(all_price)

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            # category = ProductCategory.objects.get(pk=pk)
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        content = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'products': products_list,
            'category': category,
            # 'basket': quantity_and_price
            'basket': get_basket(request.user),
            'hot_product': get_hot_product(),
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'basket': get_basket(request.user),
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    pass

def contacts(request):
    content = {
        'title': 'Контакты',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)

def not_found(request, exception):
    return render(request, '404.html', {'item': 'item'}, status=404)
