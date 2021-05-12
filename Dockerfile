FROM python:slim-buster

COPY mcs_health_check.py mcs_health_check.py

RUN pip3 install mcstatus

CMD ["python3", "mcs_health_check.py"]
