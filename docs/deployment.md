# Deployment

## Run as a Service
```bash
uvicorn dashboard.app:app --host 0.0.0.0 --port 8000
```

## Dockerization
```dockerfile
FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["uvicorn", "dashboard.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## GitHub Pages (MkDocs)
```bash
mkdocs gh-deploy
```