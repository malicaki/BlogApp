from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('articles/',views.articles,name = "articles"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('',views.articles,name = "articles"),
    path('article/<int:id>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateArticle,name = "update"),
    path('delete/<slug:slug>',views.deleteArticle,name = "delete"),
]