FROM python:3-slim

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

COPY index.py .

CMD ["pipenv", "run", "python", "index.py"]
