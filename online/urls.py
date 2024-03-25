

from django.urls import path
from online import views

urlpatterns = [
   
    path('', views.index , name='index'),
    path('add_author',views.add_author, name='add_author'),
    path('show_author',views.show_author,name='show_author'),
    # path('manage_category',views.manage_category, name='manage_category'),
]
