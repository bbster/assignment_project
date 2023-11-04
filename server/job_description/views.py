import os

from django.conf import settings
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import filters, serializers
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)

from job_description.models import Company, JobDescription, ResumeHistory, User
from job_description.serializers import (
    CompanyListCreateSerializer,
    CompanyRetrieveUpdateDestroySerializer,
    JobDescriptionListCreateSerializer,
    JobDescriptionRetrieveUpdateDestroySerializer,
    ResumeHistoryListCreateSerializer,
    ResumeHistoryRetrieveDestroySerializer,
    UserCreateSerializer,
    UserRetrieveUpdateDestroySerializer,
)


class JobDescriptionListCreateView(ListCreateAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionListCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "company",
        "position",
        "content",
        "job_refund_pay",
        "skils",
        "start_date",
        "end_date",
    ]


class JobDescriptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionRetrieveUpdateDestroySerializer


class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "company_name", "country", "city"]

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_parameters = {
            "id": self.request.query_params.get("company_id"),
            "company_name": self.request.query_params.get("company_name"),
            "country": self.request.query_params.get("country"),
            "city": self.request.query_params.get("city"),
        }

        for field, value in filter_parameters.items():
            if value:
                queryset = queryset.filter(**{field: value})

        return queryset


class CompanyRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyRetrieveUpdateDestroySerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroySerializer


class ResumeHistoryListCreateView(ListCreateAPIView):
    queryset = ResumeHistory.objects.all()
    serializer_class = ResumeHistoryListCreateSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise serializers.ValidationError(
                "하나의 지원공고에는 한번만 지원 할 수 있습니다.",
            )


class ResumeHistoryRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = ResumeHistory.objects.all()
    serializer_class = ResumeHistoryRetrieveDestroySerializer


def index(request):
    template_path = os.path.join(
        settings.BASE_DIR,
        "templates",
        "assignment_templates",
        "index.html",
    )
    return render(request, template_path)
