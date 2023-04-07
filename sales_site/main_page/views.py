from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from portfolio.views import projects
from dataclasses import dataclass
from .models import Portfolio, Member

def main_page(request):
    count = len(projects)
    data = {
        'Member': Member.objects.all(),
        'Portfolio': Portfolio.objects.all(),
        'count': count,
        'projects': projects,
    }
    return render(request, 'main_page/main_page.html', context=data)
