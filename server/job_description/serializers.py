from rest_framework import serializers

from job_description.models import Company, JobDescription, ResumeHistory, User


class JobDescriptionListCreateSerializer(serializers.ModelSerializer):
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
    job_descriptions = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ["id", "company_name", "country", "city", "job_descriptions"]

    def get_job_descriptions(self, obj):
        job_descriptions = obj.job_descriptions.all()

        return [
            {
                "company": job_description.company_id,
                "position": job_description.position,
                "content": job_description.content,
                "reward": job_description.reward,
                "skill": job_description.skill,
                "start_date": job_description.start_date,
                "end_date": job_description.end_date,
            }
            for job_description in job_descriptions
        ]


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
