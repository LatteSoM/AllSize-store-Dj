from django.shortcuts import render, redirect
from .models import *
from MainApp.form import SortingForm, SizeForm, SaleForm, PriceForm, AddToCartForm, FavoritesForm
from .utils import ord_param
from busket.views import add_to_cart
from wishlist.views import add_to_favorites
# from busket.views import goods_details

# Create your views here.


def main_goods_ids():
    main_cards_ids = []
    ids_in_db = MainProducts.objects.all()
    for idd in ids_in_db:
        main_cards_ids.append(idd.id)
    return main_cards_ids


def home(request):
    huge_card_id = HugeCard.objects.first().id
    huge_card_descr = HugeCard.objects.first().description
    good_in_huge_card = Goods.objects.get(id=huge_card_id)

    main_cards = Goods.objects.filter(id__in=main_goods_ids())

    good_on_sale = Goods.objects.filter(sale_confirmed=True)

    context = {
        'huge_card': good_in_huge_card,
        'descr': huge_card_descr,
        'mian_cards': main_cards,
        'sale': good_on_sale,
        'category': [1, 2, 3, 4],
        'brands': [1, 2, 3, 4, 5]
    }
    return render(request, 'MainApp/main.html', context)


def brands_only(request):
    brand_cards = Brands.objects.all()
    br_list = []
    for i in brand_cards:
        br_list.append(i.brand_name)
    category_cards = Category.objects.all()
    context = {
        'brands': br_list,
        # 'need_to_show_brand': 'True',
        # 'category': category_cards,
        # 'selected': sl

    }
    return render(request, 'MainApp/brands.html', context)


def cats_only(request, brand):
    # brand_cards = Brands.objects.all()
    category_cards = Category.objects.filter(brand__brand_name=brand)
    context = {
        # 'brands': brand_cards,
        # 'need_to_show_brand': 'False',
        'category': category_cards,
        # 'selected': sl

    }
    return render(request, 'MainApp/cats.html', context)


def button_view(request):
    if request.method == 'POST':
        if 'expensive' in request.POST:
            return render(request, 'MainApp/brandpage.html', ord_param('-price'))
        if 'cheaper' in request.POST:
            return render(request, 'MainApp/brandpage.html', ord_param('price'))
        if 'sale' in request.POST:
            return render(request, 'MainApp/brandpage.html', ord_param(sale=True))
        else:
            return render(request, 'MainApp/main.html')


def goods(request, brand=None, cat=None):
    if brand is None:
        goods = Goods.objects.all()
    else:
        goods = Goods.objects.filter(brand_id__brand_name=brand)

    if cat == 'sale':
        goods = Goods.objects.filter(sale_confirmed=True)

    # if not cat is None and not cat in 'sale':
    #     goods = Goods.objects.filter()

    o = {}
    for item in goods:
        key = item.model_name
        img = Images.objects.filter(good_id=item.id)
        o[key] = img



    form = SortingForm()
    size_form = SizeForm()
    sale_form = SaleForm(request.GET)
    price_form = PriceForm(request.GET)

    context = {'form': form, 'sizes': size_form, 'sale': sale_form, 'price': price_form,
               'goods': goods, }
    print(size_form.fields)
    if request.method == 'GET':
        form = SortingForm(request.GET)
        size_form = SizeForm(request.GET)
        sale_form = SaleForm(request.GET)
        price_form = PriceForm(request.GET)

        print(form.data)
        if form.is_valid() and size_form.is_valid() and sale_form.is_valid() and price_form.is_valid():

            con = []
            for field in form.cleaned_data:
                if form.cleaned_data[field]:
                    con.append(field)

            con_size = []
            for size in size_form.cleaned_data:
                if size_form.cleaned_data[size]:
                    con_size.append(size)

            con_sale = sale_form.cleaned_data['on_sale']
            print(con_sale)

            filtered_queryset = Goods.objects.all()
            if cat is not None:
                if cat == 'sale':
                    filtered_queryset = Goods.objects.filter(sale_confirmed=True)
                else:
                    filtered_queryset = Goods.objects.filter(category__category_name=cat)
            if con:
                filtered_queryset = filtered_queryset.filter(
                    category__category_name__in=con) if con else Goods.objects.all()

            if con_size:
                goods_for_size = SizesToGoodTable.objects.filter(
                    size__size__in=con_size).values_list('good_id', flat=True)
                filtered_queryset = filtered_queryset.filter(id__in=goods_for_size)

            if con_sale:
                filtered_queryset = filtered_queryset.filter(sale_confirmed=con_sale)

            if price_form.cleaned_data['cheaper']:
                filtered_queryset = filtered_queryset.filter(price__lte=7000)

            if price_form.cleaned_data['medium']:
                filtered_queryset = filtered_queryset.filter(price__gte=7000, price__lte=10000)

            if price_form.cleaned_data['prem']:
                filtered_queryset = filtered_queryset.filter(price__gte=10000)

            if brand is None:
                brand_as = 'всех товаров'
            else:
                brand_as = Brands.objects.get(brand_name=brand)
                brand_as = brand_as.brand_name

            context = {'form': form,
                       'sizes': size_form,
                       'sale': sale_form,
                       'price': price_form,
                       'goods': filtered_queryset,
                       'Brand_name': brand_as}

            return render(request, 'MainApp/brandpage.html', context)

    return render(request, 'MainApp/brandpage.html', context)


def item_view(request, brand, item_id):
        good = Goods.objects.get(id=item_id)
        form = SizeForm(request.GET)
        favorite_form = FavoritesForm(request.GET)

        context = {
            'good': good,
            'form': form,
            'imgages': Images.objects.filter(good_id=good.id),
            'favorite': favorite_form,
        }
        print(form.fields)
        if request.method == 'GET':
            form = SizeForm(request.GET)
            if form.is_valid():
                con = []
                size = ''
                for field in form.cleaned_data:
                    if form.cleaned_data[field]:
                        size = field
                        con.append(field)

                if con:
                    add_to_cart(request, good.id, size)
                    # return render(request, 'busket/bag.html')
                    return redirect('/card/')

        if request.method == 'POST':
            # favorite_form = FavoritesForm(request.GET)
            add_to_favorites(request, good.id)
            return redirect('/wish/')

            # if favorite_form.is_valid():
            #     con = []
            #     for field in favorite_form.cleaned_data:
            #         if favorite_form.cleaned_data[field]:
            #             con.append(con)
            #     print(con)
            #     print(favorite_form.cleaned_data)
            #     if con:
            #         add_to_favorites(request, good.id)

        return render(request, 'MainApp/item.html', context)


def add_to_fav(request, good_id):
    good = Goods.objects.get(id=good_id)
    form = SizeForm(request.GET)
    favorite_form = FavoritesForm(request.GET)

    context = {
        'good': good,
        'form': form,
        'imgages': Images.objects.filter(good_id=good.id),
        'favorite': favorite_form,
    }
    add_to_favorites(request, good_id)

    return render(request, 'MainApp/item.html', context)


    # good = Goods.objects.get(id=item_id)
    # sizes_to_good = SizesToGoodTable.objects.filter(good=good.pk)
    # available_sizes = [size_to_good.size for size_to_good in sizes_to_good if
    #                    size_to_good.count > 0]
    # if request.method == 'GET':
    #     form = AddToCartForm(request.GET, sizes_choices=available_sizes)
    #     context = {
    #         'good': good,
    #         'form': form,
    #         'imgages': Images.objects.filter(good_id=good.id)
    #     }
    #
    #     return render(request, 'MainApp/item.html', context)
    #
    # # if request.method == 'POST' and form.is_valid():
    # #     print(form.cleaned_data)
    # #     return render(request, 'busket/bag.html')
    #
    # if request.method == 'POST':
    #     form = AddToCartForm(request.POST, sizes_choices=available_sizes)
    #     if form.is_valid():
    #         selected_size = request.POST.get()
    #         if available_sizes in selected_size:
    #             # Обработка выбранного размера и добавление в корзину
    #             return render(request, 'busket/bag.html')  # перенаправление на страницу корзины
    #         else:
    #             context = {
    #                 'good': good,
    #                 'form': form,
    #                 'images': Images.objects.filter(good_id=good.id)
    #             }
    #             # Если размер не выбран или недоступен, возвращаем страницу с формой и ошибкой
    #             form.add_error(None, 'Пожалуйста, выберите доступный размер')
    #             return render(request, 'MainApp/item.html', context)
    #     else:
    #         # В случае невалидной формы, возвращаем страницу с формой и ошибками
    #         context = {
    #             'good': good,
    #             'form': form,
    #             'images': Images.objects.filter(good_id=good.id)
    #         }
    #         return render(request, 'MainApp/item.html', context)

    # else:
    #     good = Goods.objects.get(id=item_id)
    #     sizes_to_good = SizesToGoodTable.objects.filter(good=good.pk)
    #     available_sizes = [size_to_good.size for size_to_good in sizes_to_good if
    #                        size_to_good.count > 0]
    #
    #     form = AddToCartForm(sizes_choices=available_sizes)
    #     if form.is_valid():
    #         print('smdnfjns')
    #     return render(request, 'busket/bag.html')


    # brand_name = Brands.objects.get(id=1)
    # good = Goods.objects.get(id=item_id)
    # to_cart = AddToCartForm(request.GET)
    # # img_by_sep = Images.objects.get(good_id=good.id).split(',')
    # context = {
    #     'Brand_name': brand_name.brand_name,
    #     'item': item_id,
    #     'sizes_list': SizesToGoodTable.objects.filter(good=good.id),
    #     'good': good,
    #     'imgages': Images.objects.filter(good_id=good.id),
    #     'first_image': good.main_pic,
    #     'cart_form': to_cart
    # }
    # return render(request, 'MainApp/item.html', context)


# def select_size(request):



