FROM python:3.9.5 as server

WORKDIR /usr/src/app

ENV PYTHONBURRED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
ADD backend-v1/requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy source code
ADD backend-v1 /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0:8000", "--settings=ket.settings.development"]


FROM node:16 as app

WORKDIR /app
