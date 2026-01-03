# Installer **uv**:

**Sur macOS ou Linux**

Ouvre ton terminal et colle cette commande :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

```

**Sur Windows**

Ouvre un terminal (PowerShell) et colle cette commande :

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

```

# Initialisation

```
uv init
```
ou
```
uv init PATH
```

# Environnement virtuel
```
uv venv
```

# Architecture
```
mon-api-ia/
├── pyproject.toml
├── app.py              # Point d'entrée FastAPI
├── modules/
│   └── modules.py      # Logique métier
├── models/
│   └── models.py       # Modèle IA
├── tests/
│   └── my_pytests.py   # Tes tests
└── docs/               # Dossier pour la doc 
```

# Installation des librairies et uv.lock
```
uv add fastapi uvicorn
uv add --dev pytest sphinx sphinx-rtd-theme
```

# Initialisation de la doc
On va dans le dossier `docs` puis 
```
uv run sphinx-quickstart
```

# github actions et github pages

créer les dossiers 
```
.github
└──workflows/
   └── docs.yml
```
copier coller dans docs.yml le code

Aller dans github pages (setting-->pages)
Dans Build and deployment, choisir `github actions`
