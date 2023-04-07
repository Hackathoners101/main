from django.db import models
from sales_site.settings import MEDIA_ROOT

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    

class Member(models.Model):
    name = models.CharField(max_length=64)
    expirience = models.TextField(default='Secret')
    photo = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)
    def __str__(self) -> str:
        return self.name


"""
# Добавление полей
a = Member(name='Egor', expirince='profi').save()
Member.objects.create(name='Avatar2', description='xxx')

# получение полей
Member.objects.all()
Member.objects.all()[:2]

x = Member.objects.all()[4]
x.name

# Изменение полей

x = Movie.objects.all()[2]
x.name = 'new_name'
x.save ()


# Удаление записей
x = Movie.objects.all()[3]
x.delete()


# Поиск по параметру
Movie.objects.get(id=5)

Movie.objects.get(name='Egor')

Movie.objects.filter(title='xxx')

Movie.objects.filter(age__lt=765456)

Movie.objects.filter(age__isnull)

Movie.objects.get(name='Egor').filter(age__isnull)
g
gte
lte

exclude

Movie.objects.filter(name__startwith='Eg')

Movie.objects.filter(id__in=[3, 4, 6])

"""
