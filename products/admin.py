from django.contrib import admin
from django import forms
from .models import *
from django.db.models import Q


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.filter(~Q(id=self.instance.pk) & Q(level__lte=self.instance.level))


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['level']
    form = CategoryForm


admin.site.register(Section)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
