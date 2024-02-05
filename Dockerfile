<<<<<<< HEAD
#BASE IMAGE
=======
>>>>>>> a0676271efa1b02b3d4aad7de7f1a5647288a51c
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
<<<<<<< HEAD
ENTRYPOINT ["python","app1.py"]
=======
ENTRYPOINT ["python","app1.py"]
>>>>>>> a0676271efa1b02b3d4aad7de7f1a5647288a51c
