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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/job-description', JobDescriptionListCreateView.as_view()),
    path('api/v1/job-description/<int:pk>', JobDescriptionRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/company', CompanyCreateView.as_view()),
    path('api/v1/company/<int:pk>', CompanyRetrieveDestroyView.as_view()),
    path('api/v1/user', UserCreateView.as_view()),
    path('api/v1/user/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('api/v1/resume-history', ResumeHistoryListCreateView.as_view()),
    path('api/v1/resume-history/<int:pk>', ResumeHistoryRetrieveDestroyView.as_view()),
]
