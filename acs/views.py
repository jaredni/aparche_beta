from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'acs/index.html'

# Create your views here.
