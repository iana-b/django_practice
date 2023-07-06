from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello1'),
    path('about/', views.about),
    path('item/<int:item_id>/', views.item_info),
    path('items/', views.items_list)
]
