FROM python:3.6.9
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1 

#Create directory
RUN mkdir /docker_EGL/
#Open the directory created
WORKDIR /docker_EGL/
COPY ./requirements.txt /docker_EGL/

#Install programs (In this case Django)
RUN pip install --upgrade pip
RUN pip install -r /docker_EGL/requirements.txt

#Run container in the port 8000
EXPOSE 8000
#CD directory
WORKDIR /docker_EGL/
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
