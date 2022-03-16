# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # The help page
    path('help/', views.help, name = 'help'),
    path('about-depression/', views.about_depression, name='about_depression'),
    path('assessment/', views.assessment, name='assessment'),
<<<<<<< HEAD
    path('senseit/', views.senseit, name='senseit'),
=======

>>>>>>> f8379736d5bc7d3d6e32a4aadb1a9e0d2ca45d44
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
