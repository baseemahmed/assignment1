#base image
FROM python
COPY . /Docker
WORKDIR /Docker
CMD python mypyfile.py