FROM python:3.8-alpine

WORKDIR /app

COPY setup.py README.md ./
RUN pip3 install .

COPY . .

CMD ["python3", "main.py"]
