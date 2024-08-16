from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits
import pathlib


def home_page(request, *args, **kwargs):
    # html_file_path = pathlib.Path(__file__).resolve().parent
    # print(html_file_path)
    # html_file = html_file_path/"home.html"
    # html_content = html_file.read_text()
    queryset = PageVisits.objects.all()
    
    page_qs = PageVisits.objects.filter(path = request.path)
    page_title = "My title"
    context = {
        "title" : page_title,
        'total_visit_count' : queryset.count(),
        'percentage' : page_qs.count() * (100/queryset.count()),
        'page_visit_count' : page_qs.count(),
    }
    PageVisits.objects.create(path  = request.path)
    return render(request, "home.html", context)


def about_page(request, *args, **kwargs):

    qs = PageVisits.objects.all()
    about_count = PageVisits.objects.filter(path = request.path)
    try:
        percentage = (about_count.count()*100)/qs.count()
    except:
        percentage = 0    
    context = {
        'Total_count': qs.count(),
        'about_count': about_count.count(),
        'percentage': percentage,
    }

    PageVisits.objects.create(path = request.path)
    return render(request, 'about.html', context=context)