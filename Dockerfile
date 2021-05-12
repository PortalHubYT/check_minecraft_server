FROM python:slim-buster

RUN pip3 install mcstatus

CMD ["python3 check_minecraft_server.py"]
