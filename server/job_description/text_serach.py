from django.contrib.postgres.search import SearchQuery, SearchVector
from job_description.models import JobDescription


# 전체 데이터
for object in JobDescription.objects.all():
    print(object.position)


# Full text Search
query = SearchQuery('백엔드')  # 검색어 설정
result = JobDescription.objects.annotate(search=SearchVector('position')).filter(search=query)

# Explitcit Search
result2 = JobDescription.objects.filter(position__icontains='백엔드')
