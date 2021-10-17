FROM python:3.6-alpine
WORKDIR /home
COPY . .
CMD ["python", "extraction.py"]