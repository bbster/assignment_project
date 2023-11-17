from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from account.views import AccountCreateView, AccountLoginView
from job_description.views import (
    CompanyListCreateView,
    CompanyRetrieveDestroyView,
    JobDescriptionListCreateView,
    JobDescriptionRetrieveUpdateDestroyAPIView,
    ResumeHistoryListCreateView,
    ResumeHistoryRetrieveDestroyView,
    UserCreateView,
    UserRetrieveUpdateDestroyView,
)
from todo_app.views import TodoListCreateAPIView, TodoRetrieveAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="API 문서",
        default_version="v1",
        description="API 문서",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # swagger
    # path(
    #     "api/doc/swagger",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path(
    #     "api/doc/redoc",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
    path("api/doc/spectacular", SpectacularAPIView.as_view(), name="schema"),
    # job description
    path("api/v1/job-descriptions", JobDescriptionListCreateView.as_view()),
    path(
        "api/v1/job-descriptions/<int:pk>",
        JobDescriptionRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path("api/v1/companies", CompanyListCreateView.as_view()),
    path("api/v1/companies/<int:pk>", CompanyRetrieveDestroyView.as_view()),
    path("api/v1/users", UserCreateView.as_view()),
    path("api/v1/users/<int:pk>", UserRetrieveUpdateDestroyView.as_view()),
    path("api/v1/resume-histories", ResumeHistoryListCreateView.as_view()),
    path(
        "api/v1/resume-histories/<int:pk>",
        ResumeHistoryRetrieveDestroyView.as_view(),
    ),
    # todo_app
    path("api/v1/todos", TodoListCreateAPIView.as_view()),
    path("api/v1/todos/<int:pk>", TodoRetrieveAPIView.as_view()),
    # account
    # path("api/v1/session", SessionAPIView.as_view()),
    # path("api/v1/token", TokenAPIView.as_view()),
    path("api/v1/account/login", AccountLoginView.as_view()),
    path("api/v1/account/create", AccountCreateView.as_view()),
]
