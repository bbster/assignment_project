# 부모 이미지로 공식 Python 실행 환경 사용
FROM python:3.11.6

ENV APP_HOME=/home/service/assignment

WORKDIR ${APP_HOME}

# System packages
RUN apt-get update && apt-get install -y

# 의존성 관리를 위한 pyproject.toml, poetry.lock 파일 복사
COPY poetry.lock ${APP_HOME}/
COPY pyproject.toml ${APP_HOME}/

# Poetry 설치 및 Python 가상 환경 생성하지 않음
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# app copy
COPY assignment_project ${APP_HOME}/assignment_project
COPY job_description ${APP_HOME}/job_description
COPY todo_app ${APP_HOME}/todo_app
COPY account ${APP_HOME}/account
COPY manage.py ${APP_HOME}/manage.py

# client
COPY staticfiles ${APP_HOME}/staticfiles
COPY templates ${APP_HOME}/templates

# runserver.sh 파일 복사
COPY runserver.sh ${APP_HOME}/runserver.sh
RUN chmod 755 ${APP_HOME}/runserver.sh  # 실행 권한 및 RUN

# 8000 포트를 외부로 공개
EXPOSE 8000

# Django 애플리케이션 실행
CMD ["nohup", "/bin/sh", "runserver.sh", "192.168.64.1:8000", "&"]
