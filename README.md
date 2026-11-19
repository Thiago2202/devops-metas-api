# devops-metas-api

API Flask simples de metas de estudo, com pipeline CI/CD no GitHub Actions.

**Pipeline (`.github/workflows/ci-cd.yml`):**

1. `test` — instala dependências e roda o Pytest a cada push/PR na `main`
2. `publish` — só roda se os testes passarem: build da imagem Docker, push para o GHCR e smoke test do `/health`
3. `deploy` — gera a versão estática da aplicação e publica no GitHub Pages

## Endpoints

| Rota | Resposta |
|---|---|
| `GET /` | página com as metas e o progresso |
| `GET /health` | `{"status": "ok"}` |
| `GET /metas` | lista de metas |
| `GET /progresso` | percentual concluído |

## Rodar localmente

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python app.py
```

## Deploy local com Docker

```bash
docker compose up --build -d   # http://localhost:5000/health
docker compose down
```

Ou usando a imagem publicada: `docker run --rm -p 5000:5000 ghcr.io/thiago2202/devops-metas-api:latest`
