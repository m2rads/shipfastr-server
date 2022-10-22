# 1 
FROM python:3.9



# 3
COPY src/ /app
WORKDIR /app

# 2
RUN pip3 install -r requirements.txt

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app