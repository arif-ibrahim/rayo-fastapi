# rayo-fastapi
## python3 -m venv .venv
### pip install -r requirements.txt


## Setup

Make sure to create virtual environment and active it:

```bash
# python3 -m venv .venv
pip install -r requirements.txt
source .venv/bin/activate
```

## Development Server

Start the development server on `http://127.0.0.1:8000`:

```bash
uvicorn rayoo.main:app --reload
```

