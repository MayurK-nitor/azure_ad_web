# Use the official Python image as the base image
FROM python:3-alpine3.15

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install Git
RUN apk update && apk add git

# Set your GitHub PAT as an environment variable
# ENV GITHUB_TOKEN=<your_github_pat_here>

# Install the Python packages from requirements.txt
RUN pip install -r requirements.txt

# Expose a port (if needed)
EXPOSE 3000

# Define the command to run your application
CMD python ./app.py

#Run below command in terminal
#docker build -t mayur2912/flask-appl:0.0.1.RELEASE .

#to run the container
# docker container run -d -p 3000:3000 mayur2912/flask-appl:0.0.1.RELEASE

#to check
# docker container ls

#to stop
# docker container stop imagenumber

#add this in requirements.txt
# git+https://github.com/MayurK-nitor/azure_ad_web/@feature/generic-azure-ad-web-library
