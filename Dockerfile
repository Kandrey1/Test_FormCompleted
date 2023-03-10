FROM python:3.9-alpine3.16
WORKDIR ./app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]