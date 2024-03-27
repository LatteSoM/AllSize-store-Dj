# from django.template.context_processors import static
from django.conf.urls.static import static as djstat
from django.urls import path, include
import MainApp.views as v
from AllSize import settings

from rest_framework import routers
from .views import BrandsViewSet, CategoryViewSet, ColorViewSet, GoodssViewSet, SizesViewSet, SizesToGoodViewSet

router = routers.DefaultRouter()
router.register(r'brands/', BrandsViewSet)
router.register(r'category/', CategoryViewSet)
router.register(r'colors/', ColorViewSet)
router.register(r'goods/', GoodssViewSet)
router.register(r'sizes/', SizesViewSet)
router.register(r'sizes_to_good/', SizesToGoodViewSet)


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
    path('add_to_fav/<int:product_id>/', v.add_fav, name='add_to_favorites'),
    path('is_fav/<int:product_id>/', v.is_fav, name='is_in_favorites'),
    path('search/', v.search),
    path('search/<str:search_term>', v.goods),
    path('info/', v.info_page, name='info'),
    path('api/', include(router.urls)),
    # path('add/<int:good_id>/', v.add_to_fav, name='add_fav'),
] + djstat(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
