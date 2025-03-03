from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('<str:tags>/<int:article_id>/', views.IndexArticle.as_view(),name='article'),
]