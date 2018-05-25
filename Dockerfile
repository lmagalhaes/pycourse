FROM python:3.6-alpine

WORKDIR /opt/pycourse

RUN pip install -U pip pipenv

ADD Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

ENTRYPOINT ["ipython"]
