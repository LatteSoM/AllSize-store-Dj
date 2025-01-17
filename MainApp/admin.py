from django.contrib import admin
from MainApp.models import *


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand_name', 'brands_pic')
    # list_display_links = ('brand_name',)
    list_editable = ('brand_name', 'brands_pic')
    search_fields = ('brand_name', 'brands_pic')
    # list_filter = ('pk', 'brand_name')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name', 'brand', 'cat_pic')
    # list_display_links = ('category_name',)
    list_editable = ('category_name', 'brand', 'cat_pic')
    search_fields = ('category_name', 'brand', 'cat_pic')
    # list_filter = ('pk', 'category_name')


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'color')
    # list_display_links = ('color',)
    list_editable = ('color',)
    search_fields = ('color',)
    # list_filter = ('pk', 'color')


@admin.register(Sizes)
class SizesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'size')
    # list_display_links = ('size',)
    list_editable = ('size',)
    search_fields = ('size',)
    # list_filter = ('pk', 'size')


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model_name', 'main_pic', 'category', 'brand_id', 'description', 'price', 'color_id', 'sale_confirmed', 'articul', 'price_with_sale')
    # list_display_links = ('model_name', 'category', 'brand_id', 'description', 'price', 'color_id', 'sale_confirmed')
    list_editable = ('model_name', 'main_pic','category', 'brand_id', 'description', 'price', 'color_id', 'sale_confirmed', 'articul', 'price_with_sale')
    search_fields = ('model_name', 'main_pic', 'category', 'brand_id', 'description', 'price', 'color_id', 'sale_confirmed', 'articul', 'price_with_sale')
    # list_filter = ('pk', 'model_name', 'category', 'brand_id', 'description', 'price', 'color_id', 'sale_confirmed')


@admin.register(SizesToGoodTable)
class SizesToGoodTableAdmin(admin.ModelAdmin):
    list_display = ('pk', 'good', 'size', 'count')
    # list_display_links = ('good', 'size', 'count')
    list_editable = ('good', 'size', 'count')
    search_fields = ('good', 'size', 'count')
    # list_filter = ('pk', 'good', 'size', 'count')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'imga', 'good_id')
    # list_display_links = ('imga', 'good_id')
    list_editable = ('imga', 'good_id')
    search_fields = ('imga', 'good_id')
    # list_filter = ('pk', 'imga', 'good_id')


@admin.register(HugeCard)
class HugeCardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'good_id', 'description',)
    # list_display_links = ('item_name', 'select_size', 'buyer')
    list_editable = ('good_id', 'description', )
    search_fields = ('good_id', 'description', )


@admin.register(MainProducts)
class MainProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'good_id',)
    list_editable = ('good_id', )
    search_fields = ('good_id', )


@admin.register(MainBrands)
class MainBrandsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brand_id',)
    list_editable = ('brand_id', )
    search_fields = ('brand_id', )


@admin.register(MainCats)
class MainCatsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cat_id',)
    list_editable = ('cat_id', )
    search_fields = ('cat_id', )

# Register your models here.


