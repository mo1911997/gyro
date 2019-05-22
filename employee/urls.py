
from django.urls import path,include
from .views import EmployeeView,EmployeeAddView

urlpatterns = [

    path('',EmployeeView.as_view()),
    path('addemp/',EmployeeAddView.as_view())
]
