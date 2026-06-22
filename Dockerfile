# base image
FROM python:3.9
#workdir
WORKDIR /app
#copy
COPY requirements.txt /app
COPY app.py /app
#run 
RUN pip install -r requirements.txt
#expose port
EXPOSE 5000

#command
CMD ["python", "./app.py"]