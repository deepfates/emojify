FROM python:3.7
RUN pip install poetry

# Copy over just the requirements
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code
CMD [ "poetry", "run", "python", "server.py" ]