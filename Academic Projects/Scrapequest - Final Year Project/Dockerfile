# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the MongoDB URI 
ENV MONGO_URI mongodb+srv://sharams:Su9860797972@atlascluster.abktl4t.mongodb.net/

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the working directory in the container
COPY scrapequest /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the app. CMD is required to run on Heroku
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
