from Devlittlegirls_app import views
from django.urls import path
from .views import *

app_name = 'Devlittlegirls_app'

urlpatterns = [
    path('', views.SiteList.as_view(), name='Home'),
    path('Create/', views.SiteCreate.as_view(), name='Create') #nome da pagina na barra no internet
    # path('', include('Devlittlegirls_app.urls', namespace='Devlittlegirls_app'))
]