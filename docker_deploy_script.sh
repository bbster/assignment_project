#!/bin/bash

# git pull origin main
git pull origin main

# Remove the Dockerfile container
docker rm -f sideproject_server

# Build the Dockerfile image
docker build -t sideproject_server .

# Run the Dockerfile container
docker run -d -it -p 8000:80 --link sideproject_postgres:latest --name sideproject_server sideproject_server
