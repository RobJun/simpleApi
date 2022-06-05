from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('publish', views.modifyPost.as_view()),
    path('search',views.findPost)
]
