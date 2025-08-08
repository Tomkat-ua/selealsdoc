FROM tomkat/python-base:latest
ENV TZ=Europe/Kiev

WORKDIR /app
EXPOSE 3001

COPY requirements.txt /app/
COPY templates/* /app/templates/
COPY *.py /app/

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
