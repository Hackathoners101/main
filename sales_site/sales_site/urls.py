from django.contrib import admin
from django.urls import path, include
from main_page import views

admin.site.site_header = 'CLS Global'
admin.site.index_title = 'Наша Админка'

urlpatterns = [
    path('', views.main_page),
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls'))
]
