FROM python:3.8

COPY . /app

WORKDIR /app
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python", "your_main_file.py"]