from django.urls import path, re_path
import busket.views as v

urlpatterns = [
    path('', v.home, name='busket_page',),
    path('delete/<int:good_id>/<int:size>/', v.remove_from_cart, name='delete_good'),
    path('order/', v.order_view, name='order'),
    path('end_order/', v.end_order_view, name='order_end')
]