from django.urls import path
from.views import *
from django.conf import settings


urlpatterns=[
    path('contact/',ContactView,name='contact'),
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('gallery/',gallery,name='gallery'),
    path('blog/',blog,name='blog'),
    path('service/',service,name='service'),
    path('single/',single,name='single'),
    path('ap/',appointment),
    # path('handlerequest',handlerequest,name='handlerequest')
]
