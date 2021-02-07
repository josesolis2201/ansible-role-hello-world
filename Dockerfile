FROM python:3
ADD helloworld.py /
RUN pip install flask flask_restful
EXPOSE 3333
CMD [ "python", "./helloworld.py"]