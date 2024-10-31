from django.urls import path
from .views import index,detail,Votes
urlpatterns = [
     path('', index,name = "home"),
    path('<int:question_id>',detail, name= "detail"),
    path('<int:question_id>/vote',Votes,name ="vote")
]