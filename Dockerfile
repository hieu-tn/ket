FROM python:3.9.5 as server

WORKDIR /usr/src/app

ENV PYTHONBURRED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
ADD server/requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy source code
ADD ./wait-for-it.sh /wait-for-it.sh
#ADD server /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0:8000", "--settings=ket.settings.development"]


FROM node:16 as app

WORKDIR /app

