FROM python:3.7

RUN pip install ipython
ADD requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /app
ADD api /app/api

CMD ["uvicorn", "--host", "0.0.0.0", "api.main:app"]
