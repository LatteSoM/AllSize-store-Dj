from django import forms
from .models import Category, Sizes, SizesToGoodTable


class SortingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SortingForm, self).__init__(*args, **kwargs)
        sorting_fields = Category.objects.all()
        for field in sorting_fields:
            self.fields[field.category_name] = forms.BooleanField(required=False)


class SizeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)
        sorting_sizes = Sizes.objects.all()
        for field in sorting_sizes:
            self.fields[field.size] = forms.BooleanField(required=False)


class SaleForm(forms.Form):
    on_sale = forms.BooleanField(required=False)


class PriceForm(forms.Form):
    cheaper = forms.BooleanField(required=False)
    medium = forms.BooleanField(required=False)
    prem = forms.BooleanField(required=False)


class AddToCartForm(forms.Form):
    size = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        available_sizes = kwargs.pop('available_sizes')
        super(AddToCartForm, self).__init__(*args, **kwargs)
        sizes = SizesToGoodTable.objects.filter(good_id=available_sizes)
        self.fields['size'].queryset = sizes


class DeleteForm(forms.Form):
    delete = forms.BooleanField(required=False)


class FavoritesForm(forms.Form):
    add = forms.BooleanField(required=False)

# class AddToCartForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(AddToCartForm, self).__init__(*args, **kwargs)
#
#         for field in sizes_choices:
#             print(field.size)
#             self.fields[field.size] = forms.BooleanField(required=False)
        # self.fields['size'].choices = sizes_choices
# class AddToCartForm(forms.Form):
#     # put_to_cart = forms.BooleanField(required=False)
#     def __init__(self, *args, **kwargs,):
#         super(AddToCartForm, self).__init__(*args, **kwargs,)
#         sorting_sizes = SizesToGoodTable.objects.all()
#         for field in sorting_sizes:
#             self.fields[field.size] = forms.BooleanField(required=False)

