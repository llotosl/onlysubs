FROM python:3.11.5-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /onlysubs

COPY ./requirements/requirements.txt /onlysubs/requirements/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /onlysubs/requirements/requirements.txt

COPY . /onlysubs

CMD ["uvicorn", "--factory", "onlysubs.main:create_app", "--host", "0.0.0.0", "--port", "80"]
