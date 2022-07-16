from django.urls import path

from .views import *

urlpatterns = [
    path('',error_return),
    path('student/',student_list, name="student_list"),
    path('student/details/<str:studentId>',student_detail,name="student_detail"),
    path('notification/<str:studentunid>',notification_list,name='notification_list'),
    # path('transaction/details/<str:date>',transaction_detail,name='transaction_list'),

]
