
from django.urls import path,include
from .views import EmployeeView,GetSalView,LeaveAddView,LeaveView,GetEmployeeLeaveView,LeaveApply

urlpatterns = [

    path('',EmployeeView.as_view()),
    path('getsal/',GetSalView.as_view()),
    path('addleave/',LeaveAddView.as_view()),
    path('getleave/',LeaveView.as_view()),
    path('getempleave/',GetEmployeeLeaveView.as_view()),
    path('getleaveconv/',LeaveApply.as_view())
]