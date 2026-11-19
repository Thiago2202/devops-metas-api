from app import app, progresso

client = app.test_client()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_metas():
    response = client.get("/metas")
    assert response.status_code == 200
    assert len(response.get_json()) == 4


def test_progresso():
    response = client.get("/progresso")
    assert response.status_code == 200
    assert response.get_json() == {"progresso": 75}


def test_progresso_lista_vazia():
    assert progresso([]) == 0


def test_pagina_inicial():
    response = client.get("/")
    assert response.status_code == 200
    assert "Metas DevOps" in response.get_data(as_text=True)
