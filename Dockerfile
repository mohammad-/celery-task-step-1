# This comes with python installed
FROM python:2-alpine

    # Install celery
RUN pip install celery==4.1 && \ 
    # Add user as running celery with root user is not a good idea
    adduser -S hardworker && \
    # Create directory to hold code
    mkdir -p /home/hardworker/celery-handson

# Change working directory
WORKDIR /home/hardworker/celery-handson

#Change user 
USER hardworker

# Define command
CMD ["celery", "-A", "start", "worker", "--workdir", "src", "--loglevel=info"]