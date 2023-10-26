# 부모 이미지로 공식 Python 실행 환경 사용
FROM python:3.11.6

ENV APP_HOME=/home/service/assignment

WORKDIR ${APP_HOME}

# System packages
RUN apt-get update && apt-get install -y

# 의존성 관리를 위한 pyproject.toml, poetry.lock 파일 복사
COPY poetry.lock ${APP_HOME}/
COPY pyproject.toml ${APP_HOME}/

# app copy
COPY assignment_project ${APP_HOME}/assignment_project
COPY employment ${APP_HOME}/employment
COPY todo_apps ${APP_HOME}/todo_apps
COPY manage.py ${APP_HOME}/manage.py

# runserver.sh 파일 복사
COPY runserver.sh ${APP_HOME}/runserver.sh

# Poetry 설치 및 Python 가상 환경 생성하지 않음
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN chmod 755 ${APP_HOME}/runserver.sh

# 8000 포트를 외부로 공개
EXPOSE 8000

# Django 애플리케이션 실행
CMD ["nohup", "/bin/sh", "runserver.sh", "0.0.0.0:8000", "&"]
