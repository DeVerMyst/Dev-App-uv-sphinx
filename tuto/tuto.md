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
ou si ca ne marche pas 

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# Initialisation

```bash
uv init
```
ou
```bash
uv init PATH
```

# Environnement virtuel
```bash
uv venv
```
Puis syntaxe habituel pour lancer l'environnement virtuel

# Architecture
```bash
projet/
├── pyproject.toml
├── api
│   ├── app.py             # Point d'entrée FastAPI
│   ├── modules/
│   │   └── modules.py     # Logique métier
│   ├── models/
│   │   └── models.py      # Modèle IA
│   └── docs/              # Dossier pour la doc + autres truc
└── test/
    └── test_valid.py      # Tests

```

# Installation des librairies et uv.lock
```bash
uv add fastapi uvicorn
uv add --dev pytest sphinx==8.2.3 
uv add --dev myst-parser
uv add --dev sphinx_gallery
```

si le package est distribué les utilisateurs n'auront pas les outils de dev comme le test ou la génération de la doc, ca rend le package plus léger

# Installation du thème
```bash
uv add --dev "sphinx-rtd-theme>=3.0.0rc1"
```
il y a d'autre thème comme `furo` c'est une question de choix

# Initialisation de la doc
On va dans le dossier `docs` puis 
```bash
uv run sphinx-quickstart
```

# github actions et github pages

créer les dossiers 
```bash
.github
└──workflows/
   └── docs.yml
```
copier coller dans docs.yml le code que je vous passe

Aller dans github pages (setting-->pages)
Dans Build and deployment, choisir `github actions`

# pont entre les modules pour sphinx (docs/)
Le fichier api.rst, modules.rst et models.rst font le pont pour la doc

et dans le fichier index.rst il faut ajouter '___api' à la fin et avec 3 ('\_') espaces (api.rst)
idem pour models et modules

# exemple d'un index.rst
voir le code dans `docs/index.rst`

# extension utiles
voir le code dans `docs/conf.py`

# synchro UV + package
`uv sync`

# Build de la doc
`uv run sphinx-build -b html docs/source public`

# en tête de conf.py
```python
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../api'))
print(f"DEBUG: Sphinx cherche dans : {os.path.abspath('../..')}")
```

# Faire tourner les tests
`uv run pytest`