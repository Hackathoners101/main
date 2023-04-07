from django.contrib import admin
from .models import Portfolio, Member
from django.forms import ModelForm

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class MyModelForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'expirience']
    form = MyModelForm