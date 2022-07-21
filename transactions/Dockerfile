FROM python:3
COPY /src ./

RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers

EXPOSE 8802
CMD python3 manage.py runserver 0.0.0.0:8802

