# Use the official Python image as a base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . /app/

# Your Django settings and configurations (settings.py content)
# ...

# CMD to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
