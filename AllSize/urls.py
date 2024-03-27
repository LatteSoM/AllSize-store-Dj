"""
URL configuration for AllSize project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import AllSizeSitemap
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from AllSize import settings
from django.conf.urls.static import static
from django.views.static import serve as mediaserve


# sitemaps = {'goods': AllSizeSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.routing')),
    path('card/', include('busket.routing')),
    path('wish/', include('wishlist.routings'), name='wish'),
    # re_path(r'^robots\.txt$', TemplateView.as_view(template_name="AllSize/robots.txt", content_type='text/plain')),
    # re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
]

if settings.DEBUG:
    pass
else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
                mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]

