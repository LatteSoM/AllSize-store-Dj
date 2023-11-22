from django.urls import path, re_path
import wishlist.views as v

urlpatterns = [
    path('', v.home, name='wishlist_page'),
    path('delete/<int:good_id>/', v.remove_from_favorites, name='delete_fav'),
]