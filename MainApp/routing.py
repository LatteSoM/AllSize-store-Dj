# from django.template.context_processors import static
from django.conf.urls.static import static as djstat
from django.urls import path
import MainApp.views as v
from AllSize import settings

urlpatterns = [
    path('', v.home, name='home_page'),
    path('<str:brand>/gds/', v.goods, name='goods_page'),
    path('gds/<str:cat>/', v.goods, name='sale_page'),
    path('gds/', v.goods, name='all_gds_page'),
    path('brands/<str:brand>/ctgs/', v.cats_only, name='cat_page'),
    # path('brands/<str:nts>/<str:sl_brand>/ctgs/', v.brands, name='cat_page'),
    # path('gds/<str:brand>/', v.goods, name='categ_det'),
    path('srt/', v.button_view, name='button'),
    # path('side', v.sorting_view, name='sorting_view'),
    path('brands/', v.brands_only, name='brands'),
    path('<str:brand>/gds/<int:item_id>/', v.item_view),
    # path('add/<int:good_id>/', v.add_to_fav, name='add_fav'),
] + djstat(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
