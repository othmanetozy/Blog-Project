from django.views.generic import RedirectView

from . import views
from django.urls import path

app_name='blog'
urlpatterns=[
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('redirection_url',views.redirection_fct,
         name='redir_fct'),
    path('redirect_perm',views.redirect_perm,
         name='permanent redirection'),
    path('redirection_m3',views.redirect_m3,
         name='redirection_methode3'),
    path('redirect_m4',RedirectView.as_view(url='http://127.0.0.1:8000/blog/redirection_url'),name='redirection_methode4')

]
