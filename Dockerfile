FROM python:3.9-buster

# Add source and install dependencies
RUN mkdir /Blockchain-3
WORKDIR /Blockchain-3
ADD . /Blockchain-3
RUN pip install -r requirements_new.txt
#RUN pip freeze > requirements_personal.txt

#Start Server
EXPOSE 8000
CMD python3.9 manage.py runserver 0:8000
