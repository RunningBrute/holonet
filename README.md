# Holonet

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run app

```bash
uvicorn app.main:app --reload
```

and go to `http://127.0.0.1:8000`

## Unit tests

`pytest -v`