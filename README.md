# Holonet

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .

cd frontend
npm install
npm run dev
```

## Run app

```bash
uvicorn app.main:app --reload
```

and go to `http://127.0.0.1:8000`

or if you want to share code with your friend 
`uvicorn app.main:app --host 0.0.0.0 --port 8000`
and use tunnel `cloudflared tunnel --url http://127.0.0.1:8000`

## Unit tests

`pytest -v`