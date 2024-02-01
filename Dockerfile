FROM python:3.11.7-slim-bullseye 

#COPY OF THE SOURCE CODE
COPY app1.py app1.py

#COPY OF THE REQUIRMENTS FILE
COPY requirements.txt requirements.txt

# INSTALL THE DEPENDENCIES
RUN  pip install -r requirements.txt

#EXPOSE THE PORT
EXPOSE 1010

#ENTRY POINT / STARTING POINT OF THE APPLICATION
ENTRYPOINT ["python","app1.py"]
