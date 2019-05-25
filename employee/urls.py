
from django.urls import path,include
from .views import EmployeeView,GetSalView,EmployeeAddView,LeaveAddView

urlpatterns = [

    path('',EmployeeView.as_view()),
     path('addemp/',EmployeeAddView.as_view()),
    path('getsal/',GetSalView.as_view()),
    path('addleave/',LeaveAddView.as_view())
]