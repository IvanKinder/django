from django.shortcuts import render
import json

from mainapp.models import Product, ProductCategory

# CONTACTS = []
# NAMES = []

# for i in range(3):
#     with open(f'mainapp/templates/mainapp/contacts_data/{i + 1}.json', 'r') as contact_file:
#         CONTACTS.append(json.load(contact_file))

# with open('mainapp/templates/mainapp/static_db/new_product.json', 'r') as product:
#     new_product = json.load(product)
#     for value in ProductCategory.objects.values():
#         if new_product['category'] == value['name']:
#             for cat in ProductCategory.objects.all():
#                 if cat.name == value['name']:
#                     category = cat
#             my_product = Product(category=category, name=new_product['name'],
#                                   image=new_product['image'], short_desc=new_product['short_desc'],
#                                   discription=new_product['discription'], price=new_product['price'],
#                                   quantity=new_product['quantity'])
#             for value in Product.objects.values():
#                 NAMES.append(value['name'])
#             if my_product.name not in NAMES:
#                 my_product.save()


def main(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'Главная', 'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    print(links_menu[0].id)
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    content = {
        'title': 'Контакты',
        # 'contacts': CONTACTS
    }
    return render(request, 'mainapp/contact.html', content)


def products_all(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_home(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_office(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_modern(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_classic(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)
