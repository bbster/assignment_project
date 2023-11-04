from rest_framework import serializers

from job_description.models import Company, JobDescription, ResumeHistory, User


class JobDescriptionListCreateSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    class Meta:
        model = JobDescription
        fields = [
            "id",
            "company",
            "position",
            "content",
            "reward",
            "skill",
            "start_date",
            "end_date",
        ]

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError(
                "채용시작일이 채용마감일보다 늦습니다.",
            )

        return data

    def get_company(self, obj):
        company = obj.company
        return {
            "id": company.id,
            "company_name": company.company_name,
            "country": company.country,
            "city": company.city,
        }


class JobDescriptionRetrieveUpdateDestroySerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = JobDescription
        fields = [
            "id",
            "company",
            "position",
            "content",
            "reward",
            "skill",
            "start_date",
            "end_date",
        ]

    def to_representation(self, instance):
        data = super(
            JobDescriptionRetrieveUpdateDestroySerializer,
            self,
        ).to_representation(instance)

        filtered_job_descriptions = JobDescription.objects.filter(
            company=data["company"],
        )
        data["job_description"] = [
            job_description.id for job_description in filtered_job_descriptions
        ]

        return data


class CompanyListCreateSerializer(serializers.ModelSerializer):
    job_description = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ["id", "company_name", "country", "city", "job_description"]

    def get_job_description(self, obj):
        job_description = obj.job_description

        return {
            "company": job_description.company_name,
            "position": job_description.country,
            "content": job_description.city,
            "reward": job_description.city,
            "skill": job_description.city,
            "start_date": job_description.city,
            "end_date": job_description.city,
        }


class CompanyRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "company_name", "country", "city"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "age"]


class UserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "age"]


class ResumeHistoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeHistory
        fields = ["id", "job_description", "user"]


class ResumeHistoryRetrieveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeHistory
        fields = ["id", "job_description", "user"]
