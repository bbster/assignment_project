from rest_framework import serializers

from employment.models import JobDescription, Company, User, ResumeHistory


class JobDescriptionListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ['company', 'position', 'content', 'job_refund_pay', 'skils', 'start_date', 'end_date']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError('채용시작일이 채용마감일보다 늦습니다.')

        return data


class JobDescriptionRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.id', read_only=True)

    class Meta:
        model = JobDescription
        fields = ['company', 'position', 'content', 'job_refund_pay', 'skils', 'start_date', 'end_date']

    def to_representation(self, instance):
        data = super(JobDescriptionRetrieveUpdateDestroySerializer, self).to_representation(instance)

        filtered_job_descriptions = JobDescription.objects.filter(company=data["company"])
        data["job_descriptions"] = [job_description.id for job_description in filtered_job_descriptions]

        return data


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'country', 'city']


class CompanyRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'country', 'city']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'age']


class UserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'age']


class ResumeHistoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeHistory
        fields = ['job_description', 'user']


class ResumeHistoryRetrieveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeHistory
        fields = ['job_description', 'user']
