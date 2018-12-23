FROM python:3.7-alpine

RUN mkdir /src
WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src
RUN pip install .

EXPOSE 1337

CMD [ "python", "./rest/rest.py" ]
