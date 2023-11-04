# 부모 이미지로 공식 Python 실행 환경 사용
FROM python:3.11.6
LABEL maintainer="Lee Ji Chan"

ENV APP_HOME=/home/service/assignment

WORKDIR ${APP_HOME}

# System packages
RUN apt-get update && apt-get install -y \
    build-essential \
    systemctl \
    nginx \
    vim \
    supervisor


# 의존성 관리를 위한 pyproject.toml, poetry.lock 파일 복사
COPY ./server/poetry.lock ${APP_HOME}/
COPY ./server/pyproject.toml ${APP_HOME}/

# Poetry 설치 및 Python 가상 환경 생성하지 않음
RUN pip install "poetry==1.7.0"
RUN poetry config virtualenvs.create false
RUN poetry install --only main

# supervisor
COPY ./server/supervisor.conf /etc/supervisor/conf.d/sideproject.conf

# nginx
COPY ./server/nginx.conf /etc/nginx/nginx.conf

# app copy
COPY ./server/assignment_project ${APP_HOME}/assignment_project
COPY ./server/job_description ${APP_HOME}/job_description
COPY ./server/todo_app ${APP_HOME}/todo_app
COPY ./server/account ${APP_HOME}/account
COPY ./server/manage.py ${APP_HOME}/manage.py

# client
COPY ./client/dist /home/client/dist/

# runserver.sh 파일 복사
COPY ./server/runserver.sh ${APP_HOME}/runserver.sh
RUN chmod 755 ${APP_HOME}/runserver.sh  # 실행 권한 및 RUN


# Django 애플리케이션 실행
ENTRYPOINT ["/bin/sh", "runserver.sh"]