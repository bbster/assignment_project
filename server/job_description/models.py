from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True, help_text='생성일')
    updated_at = models.DateTimeField(auto_now=True, help_text='수정일')


class Company(BaseModel):
    company_name = models.CharField(max_length=50, help_text='회사이름')
    country = models.CharField(max_length=50, help_text='국가')
    city = models.CharField(max_length=50, help_text='도시')


class JobDescription(BaseModel):
    company = models.ForeignKey(to="job_description.Company",
                                on_delete=models.CASCADE,
                                related_name="job_descriptions",
                                db_comment="해당 채용공고를 등록한 회사입니다.")
    position = models.CharField(max_length=50, help_text='직무')
    content = models.TextField(help_text='채용내용')
    reward = models.PositiveIntegerField(help_text='채용보상금')
    skill = models.CharField(max_length=200, help_text='여러 기술')
    start_date = models.DateField(help_text='채용시작일')
    end_date = models.DateField(help_text='채용마감일')


class User(BaseModel):
    name = models.CharField(max_length=50, help_text='이름')
    age = models.PositiveIntegerField(help_text='나이')
    job_descriptions = models.ManyToManyField(to="job_description.JobDescription", through="job_description.ResumeHistory",
                                              related_name="users", through_fields=("user", "job_description"))


class ResumeHistory(BaseModel):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['job_description', 'user'],
                                    name='unique_in_application')
        ]

    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE, db_comment='해당 지원이력을 가지고 있는 채용공고입니다.')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_comment='해당 지원이력을 가지고 있는 유저 입니다.')
