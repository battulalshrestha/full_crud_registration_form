from django.urls import path
from .views import home,show_data,delete_data,edit_data
urlpatterns = [
    path('',home,name = "home"),
    path('show_data/',show_data,name = "show_data"),
    path('delete_data/<int:id>/',delete_data,name = "delete_data"),
    path('edit/<int:id>/', edit_data, name='edit_data'),

]