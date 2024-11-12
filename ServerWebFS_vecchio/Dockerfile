FROM python:3.10-alpine
ADD server.py .
RUN pip install flask
RUN mkdir templates
ADD ./templates/index.html ./templates
CMD ["python","./server.py"]

