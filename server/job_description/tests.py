from rest_framework.test import APITestCase

from job_description.models import Company, JobDescription, User, ResumeHistory


class TestViews(APITestCase):
    def setUp(self):
        Company.objects.create(
            company_name="test_company", country="test_country", city="test_city"
        )
        JobDescription.objects.create(
            company=Company.objects.get(company_name="test_company"),
            position="test_position",
            content="test_content",
            job_refund_pay=100000,
            skils="test_skils",
            start_date="2021-01-01",
            end_date="2021-01-02",
        )
        User.objects.create(name="test_name", age=20)
        ResumeHistory.objects.create(
            job_description=JobDescription.objects.get(position="test_position"),
            user=User.objects.get(name="test_name"),
        )

    def test_create_job_description(self):
        response = self.client.post(
            "/api/v1/job-description",
            {
                "company": 1,
                "position": "test_position",
                "content": "test_content",
                "job_refund_pay": 100000,
                "skils": "test_skils",
                "start_date": "2021-01-01",
                "end_date": "2021-01-02",
            },
        )

        self.assertEquals(response.status_code, 201)
        self.assertEquals(
            response.json(),
            {
                "company": 1,
                "position": "test_position",
                "content": "test_content",
                "job_refund_pay": 100000,
                "skils": "test_skils",
                "start_date": "2021-01-01",
                "end_date": "2021-01-02",
            },
        )

    def test_get_job_description(self):
        response = self.client.get("/api/v1/job-description")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.json(),
            [
                {
                    "company": 1,
                    "position": "test_position",
                    "content": "test_content",
                    "job_refund_pay": 100000,
                    "skils": "test_skils",
                    "start_date": "2021-01-01",
                    "end_date": "2021-01-02",
                }
            ],
        )

    def test_retrieve_job_description(self):
        response = self.client.get("/api/v1/job-description/1")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.json(),
            {
                "company": "1",
                "position": "test_position",
                "content": "test_content",
                "job_refund_pay": 100000,
                "skils": "test_skils",
                "start_date": "2021-01-01",
                "end_date": "2021-01-02",
                "job_description": [1],
            },
        )
