#MyBlog App Url
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns =[
    url(r'^$',views.PostApi.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$',views.PostDetailApi.as_view(),name='detail'),

]
