# Onlysubs

This is project template with implementation of Clean Architecture in Python, FastAPI for REST API, SQLAlchemy with Postgres for DB actions. 

# What is this project about?

This project is template with authentication, Docker, poetry and pre-commit for new projects.

# Run project

Make sure that you run this project on version 3.10+.

```sh
poetry install
poetry run python -m onlysubs
```

```sh
docker build --tag 'onlysubs' .
docker run -p 8000:8000 'onlysubs'
```

# TODO:
 - [x] Add pre-commit config with isort, ruff, black etc.
 - [ ] Add JSON logs.
 - [ ] Add unit and integration tests.
 - [ ] Add docker support.
 - [ ] Add SQLAlchemy support.
 - [ ] Realize MVP.
 - [ ] Add CI/CD.
 - [ ] Add Grafana Loki.
 - [ ] Add message broker for background tasks.
