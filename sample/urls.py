
from django.urls import path,include
from .views import UserView,UserAddView

urlpatterns = [

    path('',UserView.as_view()),
    path('adduser/',UserAddView.as_view())
]
