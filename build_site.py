"""Gera a versão estática da aplicação (usada no deploy para o GitHub Pages)."""
from pathlib import Path

from app import app

SAIDA = Path("site")
ROTAS = {
    "/": "index.html",
    "/health": "health.json",
    "/metas": "metas.json",
    "/progresso": "progresso.json",
}

SAIDA.mkdir(exist_ok=True)
client = app.test_client()
for rota, arquivo in ROTAS.items():
    resposta = client.get(rota)
    assert resposta.status_code == 200, f"{rota} retornou {resposta.status_code}"
    (SAIDA / arquivo).write_bytes(resposta.data)
    print(f"{rota} -> site/{arquivo}")
