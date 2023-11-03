from drf_spectacular.views import SpectacularAPIView

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from account.views import SessionAPIView, TokenAPIView
from job_description.views import (
    JobDescriptionListCreateView,
    JobDescriptionRetrieveUpdateDestroyAPIView,
    UserCreateView,
    UserRetrieveUpdateDestroyView,
    ResumeHistoryListCreateView,
    ResumeHistoryRetrieveDestroyView,
    CompanyRetrieveDestroyView,
    CompanyListCreateView,
    index,
)
from todo_app.views import TodoRetrieveAPIView, TodoListCreateAPIView

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
    path("", index, name="index"),
    # swagger
    path(
        "api/doc/swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/doc/redoc",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
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
        "api/v1/resume-histories/<int:pk>", ResumeHistoryRetrieveDestroyView.as_view()
    ),
    # todo_app
    path("api/v1/todos", TodoListCreateAPIView.as_view()),
    path("api/v1/todos/<int:pk>", TodoRetrieveAPIView.as_view()),
    # account
    path("api/v1/session", SessionAPIView.as_view()),
    path("api/v1/token", TokenAPIView.as_view()),
]
