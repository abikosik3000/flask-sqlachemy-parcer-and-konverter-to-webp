FROM ubuntu:latest
MAINTAINER Nikolay Tsygankov 'abikosik2018@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
#ENTRYPOINT ['python3']python3
#CMD ["export", "FLASK_APP=myapp"]
CMD [ "flask", "--app" , "myapp", "run", "--host=0.0.0.0"]