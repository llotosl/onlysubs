# Onlysubs

This is my pet project with implementation of Clean Architecture in Python, FastAPI for REST API, SQLAlchemy with Postgres for DB actions. 

# What this project about?

This project is analog of Onlyfans or Boosty. This is service with subscription management where authors can publish content for their subscribers.

# Run project

```sh
poetry install
poetry run uvicorn --factory onlysubs.main:create_app
```

# TODO:
 - [ ] Add pre-commit config with isort, ruff, black etc.
 - [ ] Add unit and integration tests.
 - [ ] Add docker support.
 - [ ] Add SQLAlchemy support.
 - [ ] Realize MVP.
 - [ ] Add CI/CD.
 - [ ] Add Grafana Loki.
 - [ ] Add message broker for background tasks.

