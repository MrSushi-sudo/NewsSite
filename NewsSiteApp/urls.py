from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewsList.as_view(), name='home'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
    path('create/', views.NewsCreateView.as_view(), name='news_create'),
]
