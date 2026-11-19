from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

METAS = [
    {"id": 1, "titulo": "Aprender Docker", "concluida": True},
    {"id": 2, "titulo": "Criar pipeline no GitHub Actions", "concluida": True},
    {"id": 3, "titulo": "Publicar imagem no GHCR", "concluida": True},
    {"id": 4, "titulo": "Fazer deploy em produção", "concluida": False},
]


def progresso(metas):
    """Percentual de metas concluídas (0 a 100)."""
    if not metas:
        return 0
    feitas = sum(1 for m in metas if m["concluida"])
    return round(feitas * 100 / len(metas))


PAGINA = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Metas DevOps</title>
  <style>
    body { font-family: system-ui, sans-serif; background: #0d1117; color: #e6edf3;
           max-width: 640px; margin: 40px auto; padding: 0 16px; }
    h1 { margin-bottom: 4px; }
    .barra { background: #21262d; border-radius: 8px; height: 14px; overflow: hidden; }
    .barra div { background: #2ea043; height: 100%; }
    li { padding: 8px 0; border-bottom: 1px solid #21262d; list-style: none; }
    ul { padding: 0; }
    small { color: #8b949e; }
  </style>
</head>
<body>
  <h1>Metas DevOps</h1>
  <small>Flask · Pytest · Docker · GitHub Actions</small>
  <p>Progresso: <strong>{{ pct }}%</strong></p>
  <div class="barra"><div style="width: {{ pct }}%"></div></div>
  <ul>
  {% for m in metas %}
    <li>{{ "✅" if m.concluida else "⬜" }} {{ m.titulo }}</li>
  {% endfor %}
  </ul>
  <small>status: online</small>
</body>
</html>"""


@app.get("/")
def index():
    return render_template_string(PAGINA, metas=METAS, pct=progresso(METAS))


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/metas")
def metas():
    return jsonify(METAS)


@app.get("/progresso")
def progresso_endpoint():
    return jsonify(progresso=progresso(METAS))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
