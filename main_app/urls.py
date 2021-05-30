from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name='index'),
    path('add/', views.Create.as_view(), name='add'),
    path('<int:item_id>/', views.items_detail, name='index'),
    path('<int:pk>/delete/', views.Delete.as_view(), name='delete'),
]