from django.urls import path
from . import views

app_name = 'function_view'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/update_record/', views.update_record, name='update_record'),
    path('<int:id>/delete/', views.delete, name='delete'),
]