import os

from django.conf import settings
from django.db import IntegrityError
from django.shortcuts import render

from rest_framework import serializers, filters
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveDestroyAPIView
)

from job_description.models import (
    JobDescription,
    Company,
    User,
    ResumeHistory
)
from job_description.serializers import (
    JobDescriptionRetrieveUpdateDestroySerializer,
    JobDescriptionListCreateSerializer,
    CompanyRetrieveUpdateDestroySerializer,
    UserCreateSerializer,
    UserRetrieveUpdateDestroySerializer,
    ResumeHistoryListCreateSerializer,
    ResumeHistoryRetrieveDestroySerializer, CompanyListCreateSerializer,
)


class JobDescriptionListCreateView(ListCreateAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionListCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["position", "content", "job_refund_pay", "skils", "start_date", "end_date"]


class JobDescriptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionRetrieveUpdateDestroySerializer


class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListCreateSerializer


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
            raise serializers.ValidationError('하나의 지원공고에는 한번만 지원 할 수 있습니다.')


class ResumeHistoryRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = ResumeHistory.objects.all()
    serializer_class = ResumeHistoryRetrieveDestroySerializer


def index(request):
    template_path = os.path.join(settings.BASE_DIR.parent, 'client', 'dist', 'index.html')
    return render(request, template_path)
