FROM python:3

RUN mkdir /opt/pycourse

WORKDIR /opt/pycourse

RUN pip install -U pip pipenv

ADD Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

ENTRYPOINT ["ipython"]
