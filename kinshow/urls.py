from django.urls import path

from . import views

app_name = 'kinshow'
urlpatterns = [
    path('', views.index, name='index'),
    # path('test/', views.test, name='test'),
    # path('<int:pk>/', views.NewsView.as_view(), name='NewsView'),
    path('news/<int:pk>', views.news, name="news")
]
