from .models import Goods, Brands
from django.http import HttpResponseRedirect
from .form import *


def ord_param(param='price', sale=False):
    if param == 'default':
        goods = Goods.objects.all()
    else:
        if sale:
            goods = Goods.objects.filter(sale_confirmed=True)
        else:
            goods = Goods.objects.order_by(param)

    brand = Brands.objects.get(id=1)
    # cats = Category.objects.all()
    context = {
        'Brand_name': brand.brand_name,
        # 'i': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        'goods': goods,
        # 'cats': cats.count()
        # 'pic': Images.objects.filter(good_id=1)
    }
    return context


def submit_all_forms(request):
    if request.method == 'POST':
        form1 = SortingForm(request.POST)
        form2 = SizeForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect('/success-page/')  # Перенаправление на страницу успеха
    else:
        form1 = SortingForm()
        form2 = SizeForm()
    return render(request, 'submit_all_forms.html', {'form1': form1, 'form2': form2})
