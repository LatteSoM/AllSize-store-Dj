from django.shortcuts import render, redirect
from MainApp.models import Goods, SizesToGoodTable, MainProducts
from MainApp.form import DeleteForm, SizeForm
from busket.form import ContactForm
from busket.AllSizeBot import saaaaaad
# import telegram_send
# from MainApp.form import AddToCartForm
# Create your views here.


def remove_from_cart(request, good_id, size):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        uniq_key = str(good_id)+'_'+str(size)
        if str(uniq_key) in cart:
            del cart[str(uniq_key)]
            request.session['cart'] = cart
    return redirect('busket_page')


def get_cart_goods(request):
    cart = request.session.get('cart', {})
    goods_ids = [int(key.split('_')[0]) for key in cart.keys()]  # Получаем список id товаров из ключей словаря cart
    goods = Goods.objects.filter(id__in=goods_ids)  # Получаем товары из базы данных по списку id
    goods_in_cart = []
    for key in cart:
        good = goods.get(id=key[:1])
        good.quantity = cart[key][0]
        good.size = cart[key][1]
        goods_in_cart.append(good)

    return goods_in_cart


def group_message(request, client, number):
    a = f'Новый заказ: \n' \
        f'Имя клиента: {client} \n' \
        f'Номер телефона: {number}\n' \
        f'----------------------------- \n'

    # message = [a, ]
    goods_in_cart = get_cart_goods(request)
    for good in goods_in_cart:
        a += f'Модель: {good.model_name} \n' \
            f'Размер: {good.size} \n' \
            f'Количество: {good.quantity} \n' \
            f'------------------------------- \n'
    #     message[0] += a
    # return message[0]
    return a


def order_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            # send_order()
            # telegram_send.send(messages=['успех'])
            # tok = '6334529129:AAH5JseCYY8l4eEIPUilwTA3BjPDtmo6zAc'
            # u_id = '420309682'
            # url = f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={u_id}&parse_mode=MarkDown&text=xuy'
            # request.get(url)
            saaaaaad(group_message(request, name, phone_number))
            return redirect('/card/')
    else:
        form = ContactForm()

    goods = get_cart_goods(request)
    total = 0
    for good in goods:
        total += good.price

    context = {'goods': goods,
               'form': form,
               'total': total}
    return render(request, 'busket/order.html', context)


def main_goods_ids():
    main_cards_ids = []
    ids_in_db = MainProducts.objects.all()
    for idd in ids_in_db:
        main_cards_ids.append(idd.id)
    return main_cards_ids


def home(request):
    goods = get_cart_goods(request)

    form_delete = DeleteForm(request.GET)
    form = SizeForm(request.GET)

    favourite = request.session.get('favorites', {})
    fav_ids = list(favourite.keys())
    fav_goods = Goods.objects.filter(id__in=fav_ids)

    if 'goods_id' in request.GET and 'size' in request.GET:
        goods_id = request.GET['goods_id']
        selected_size = request.GET['size']
        add_to_cart(request, goods_id, selected_size)
        return redirect('/card/')

    total = 0
    for good in goods:
        total += good.price

    main_cards = Goods.objects.filter(id__in=main_goods_ids())

    context = {
        'goods': goods,
        'form': form_delete,
        'total': total,
        'fav': fav_goods,
        'add_form': form,
        'mian_cards': main_cards,

    }
    return render(request, 'busket/bag.html', context)


def add_to_cart(request, goods_id, selected_size):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    uniq_id = str(goods_id)+'_'+str(selected_size)
    print(type(uniq_id))
    if uniq_id in cart:
        print('s')
        if cart[uniq_id][1] == selected_size:
            print('f')
            cart[uniq_id][0] += 1
        else:
            cart[uniq_id] += [1, selected_size]
    else:
        print('e')
        cart[uniq_id] = [1, selected_size]
        # print('неправильное услоыие')
    request.session['cart'] = cart
    request.session.modified = True

