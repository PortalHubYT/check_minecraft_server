FROM python:slim-buster

COPY check_minecraft_server.py check_minecraft_server.py

RUN pip3 install mcstatus

CMD ["python3", "check_minecraft_server.py"]
