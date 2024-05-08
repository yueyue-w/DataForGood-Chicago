from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import Context, loader

from .models import Georeference, EconomicMain, EconomicSub
from django.template.defaulttags import register
from .utils import create_table
from .forms import SearchForm

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.

# Main Page - /main/
def index(request):
    return render(request, 'index.html')

# About Us Page - /main/about_us/
def aboutus(request):
    return render(request, 'aboutus.html')

# Data and Visualize Page - /main/data&visualize/
def dataandvisualize(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            geograpahic_level = form.cleaned_data['geographic_level']
            geographic_unit = form.cleaned_data['tract']
            year = form.cleaned_data['year']
            indicator = form.cleaned_data['indicator']
            
            print(geograpahic_level, geographic_unit, year, indicator)        
            field = create_table(EconomicMain, geograpahic_level, geographic_unit,
                                 indicator, year)
    
            return render(request, "dataandvisualize.html", {'field':field})
        
    return render(request, "dataandvisualize.html", {'form':form})

# Resources Page - /main/resources/
def resources(request):
    return render(request, "resources.html")