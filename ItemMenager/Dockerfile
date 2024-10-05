# Wybierz obraz bazowy
FROM python:3.12

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik pyproject.toml i poetry.lock
COPY pyproject.toml poetry.lock ./

# Zainstaluj Poetry
RUN pip install poetry

# Zainstaluj zależności
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Skopiuj cały kod źródłowy
COPY . .

# Ustaw zmienną środowiskową dla Django
ENV PYTHONUNBUFFERED 1

# Ustaw polecenie do uruchamiania serwera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
