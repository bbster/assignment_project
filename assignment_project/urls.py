from django.contrib import admin
from django.urls import path

from employment.views import (
    JobDescriptionListCreateView,
    JobDescriptionRetrieveUpdateDestroyAPIView,
    CompanyCreateView,
    UserCreateView,
    UserRetrieveUpdateDestroyView,
    ResumeHistoryListCreateView,
    ResumeHistoryRetrieveDestroyView,
    CompanyRetrieveDestroyView,

)
from todo_app.views import TodoRetrieveAPIView, TodoListCreateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),

    # job description
    path('api/v1/job-descriptions', JobDescriptionListCreateView.as_view()),
    path('api/v1/job-descriptions/<int:pk>', JobDescriptionRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/companys', CompanyCreateView.as_view()),
    path('api/v1/companys/<int:pk>', CompanyRetrieveDestroyView.as_view()),
    path('api/v1/users', UserCreateView.as_view()),
    path('api/v1/users/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('api/v1/resume-histories', ResumeHistoryListCreateView.as_view()),
    path('api/v1/resume-histories/<int:pk>', ResumeHistoryRetrieveDestroyView.as_view()),

    # todo_app
    path('api/v1/todos', TodoListCreateAPIView.as_view()),
    path('api/v1/todos/<int:pk>', TodoRetrieveAPIView.as_view()),
]

