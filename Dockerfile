FROM python:3.11
WORKDIR /
COPY foo.py /
CMD ["python", "./foo.py"]