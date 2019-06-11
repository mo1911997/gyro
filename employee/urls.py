
from django.urls import path,include
from .views import EmployeeView,GetSalView,MainView,LeaveView,GetOneEmployeeView,LeaveApply

urlpatterns = [

    path('',EmployeeView.as_view()),
    path('leave/',LeaveView.as_view()),
    path('getemp/',GetOneEmployeeView.as_view()),
    path('getsal/',GetSalView.as_view()),
    path('main/',MainView.as_view()),
    path('getleaveconv/',LeaveApply.as_view())
]