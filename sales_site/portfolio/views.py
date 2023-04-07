from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from typing import Union
from dataclasses import dataclass
from main_page.models import Portfolio, Member


@dataclass
class Project:
    title: str
    hours: int
    url: str
    
    def __str__(self) -> str:
        return f"На проект под названием {self.title} я потратил {self.hours}"


projects = {
    "web": Project('website', 40, 'https://google.com'),
    "AI": Project('ML', 22, 'https://openai.com'),
}


def get_main_profile_page(request):
    return HttpResponse(f"Все ваше портфолио")


def get_projects_by_title(request, title: str) -> Union[HttpResponse, HttpResponseNotFound]:
    print(title)
    queryset = Portfolio.objects.all()
    my_column_values = list(queryset.values_list('title', flat=True))
    if title in my_column_values:
        data = {'project': Portfolio.objects.get(title=title)}
        return render(request, "portfolio/portfolio.html", context=data)
    else:
        data = {'title': title}
        return render(request, "error_page.html", context=data)


def get_projects_by_number(request, number: int) -> Union[HttpResponse, HttpResponseNotFound]:
    title = list(projects)[number-1]
    if number < len(projects) and number > 0:
        return HttpResponse(f"Ваш проект содержит: {projects[title]}")
    else:
        return HttpResponseNotFound(f"Проект под названием '{title}' не найден(")
