from  django.conf.urls import url

from . import views

app_name = 'mauridb'
urlpatterns = [

    # homepage
    url(r'^$', views.homepage, name='homepage'),

    # description of the web site
    url(r'^description/', views.description, name='description'),

    # details of the developer
    url(r'^developer/details/', views.mauri, name='mauri')
]