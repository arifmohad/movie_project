
from django.urls import path

from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('movie/<int:id>', views.movdetails, name='movdetails'),
    path('addimg/', views.add_details, name='add_details'),
    path('edit/<int:id>', views.update, name='editdetails'),
    path('delete/<int:id>', views.delete, name='delete'),
]
