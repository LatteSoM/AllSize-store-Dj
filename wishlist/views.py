from django.shortcuts import render, redirect
from MainApp.models import *
from MainApp.form import DeleteForm, SizeForm
from busket.views import add_to_cart
# from MainApp.views import main_goods_ids
# Create your views here.


def main_goods_ids():
    main_cards_ids = []
    ids_in_db = MainProducts.objects.all()
    for idd in ids_in_db:
        main_cards_ids.append(idd.id)
    return main_cards_ids


def home(request):
    fav_list = request.session.get('favorites', {})
    goods_ids = list(fav_list.keys())
    goods = Goods.objects.filter(id__in=goods_ids)

    form_delete = DeleteForm(request.GET)
    form = SizeForm(request.GET)

    total = 0
    for good in goods:
        total += good.price

    if 'goods_id' in request.GET and 'size' in request.GET:
        goods_id = request.GET['goods_id']
        selected_size = request.GET['size']
        add_to_cart(request, goods_id, selected_size)
        return redirect('/card/')

    main_cards = Goods.objects.filter(id__in=main_goods_ids())

    context = {
        'goods': goods,
        'form': form_delete,
        'total': total,
        'add_form': form,
        'mian_cards': main_cards,
    }

    return render(request, 'wishlist/wishlist.html', context)

    # cards_count = {
    #     'crd_count': [1, 2, 3, 4],
    #     'i': [1, 2, 3, 4, 5],
    #     'positions': [1, 2]
    # }

    # return render(request, 'wishlist/wishlist.html', context)


def add_to_favorites(request, goods_id):
    # del request.session['favorites']
    if 'favorites' not in request.session:
        request.session['favorites'] = {}
    fav = request.session['favorites']
    if goods_id in fav:
        if fav[goods_id]:
            fav[goods_id] += 1
        else:
            fav[goods_id] += 1,
    else:
        # cart[goods_id] = 1
        fav[goods_id] = 1
        # print('неправильное услоыие')
    request.session['favorites'] = fav
    request.session.modified = True
    # if request.method == 'POST':
    #     if not request.session.get('favorites'):
    #         request.session['favorites'] = list()
    #     else:
    #         request.session['favorites'] = list(request.session['favorites'])
    #
    #     favorites_ids_list = list()
    #     for item in request.session['favorites']:
    #         favorites_ids_list.append(item['id'])
    #
    #     # item_exists = next((item for item in request.session['favorites'] if item["type"] == request.POST.get('type') and item["id"] == id), False)
    #
    #     add_data = {
    #         'type': request.POST.get('type'),
    #         'id': goods_id,
    #     }
    #
    #     if goods_id not in favorites_ids_list:
    #         request.session['favorites'].append(add_data)
    #         request.session.modified = True


def remove_from_favorites(request, good_id):
    if request.method == 'POST':
        fav = request.session.get('favorites', {})
        if str(good_id) in fav:
            del fav[str(good_id)]
            request.session['favorites'] = fav
            # messages.success(request, 'The item has been removed from your shopping bag.')
        # else:
        # messages.error(request, 'The item does not exist in your shopping bag.')

    return redirect('wishlist_page')
    # if request.method == 'POST':
    #     for item in request.session['favorites']:
    #         if item['id'] == goods_id:
    #             item.caler()
    #
    #     while {} in request.session['favorites']:
    #         request.session['favorites'].remove({})
    #
    #     if not request.session['favorites']:
    #         del request.session['favorites']