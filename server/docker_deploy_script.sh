#!/bin/bash

# Stop the Docker container
docker stop sideproject_server

# Remove the Docker container
docker rm sideproject_server
docker rmi sideproject_server

# Build the Docker image
docker build -t sideproject_server .

# Run the Docker container
docker run -d -it -p 8000:8000 --link sideproject_postgres:latest --name sideproject_server sideproject_server
