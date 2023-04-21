FROM python:3
WORKDIR /
COPY foo.py /
CMD ["python", "./foo.py"]