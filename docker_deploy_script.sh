#!/bin/bash

# Stop the Docker container
docker stop sideproject_server

# Remove the Docker container
docker rm sideproject_server
docker rmi sideproject

# Build the Docker image
docker build -t sideproject .

# Run the Docker container
docker run -d -it -p 8000:8000 --link jc_postgres:latest --name sideproject_server sideproject
