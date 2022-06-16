from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from Devlittlegirls_app.models import Site

class SiteList(ListView): #aqui é o nome da pagina html
    model = Site
    queryset = Site.objects.all()

class SiteCreate(CreateView):
    model = Site
    fields = "__all__"
    success_url = reverse_lazy('Devlittlegirls_app:Home')
