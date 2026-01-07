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
│   ├── app.py              # Point d'entrée FastAPI
│   ├── modules/
│   │   └── modules.py      # Logique métier
│   ├── models/
│   │   └── models.py       # Modèle IA
│   └── docs/               # Dossier pour la doc + autres truc
└── tests/
    └── my_pytests.py   # Tes tests

```

# Installation des librairies et uv.lock
```bash
uv add fastapi uvicorn
uv add --dev pytest sphinx sphinx-rtd-theme
```
si le package est distribué les utilisateurs n'auront pas les outils de dev comme le test ou la génération de la doc, ca rend le package plus léger

# Initialisation de la doc
On va dans le dossier `docs` puis 
```bash
uv run sphinx-quickstart
```

# Mise à jour du thème
```bash
uv add --dev "sphinx-rtd-theme>=3.0.0rc1"
```
il y a d'autre thème comme `furo` c'est une question de choix

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

# pont entre les modules pour sphinx
Le fichier api.rst fait le pont pour la doc

et dans le fichier index.rst il faut ajouter '___api' à la fin et avec 3 ('\_') espaces (api.rst)

# exemple d'un index.rst
```rst
PACKAGING INITIATION
=============================

.. image:: _static/logo.png
  :width: 400
  :alt: mon logo

Sommaire
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

.. include:: ../../README.md
   :parser: myst_parser.sphinx_
   ```
# extension utiles
```
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',  # Pour extraire la doc de ton code
    'sphinx.ext.napoleon', # Pour supporter les docstrings style Google/NumPy
    'sphinx.ext.mathjax', # Pour latex 
    "sphinx.ext.viewcode", # Pour afficher le code source
    "sphinx_gallery.gen_gallery", # Pour les galleries d'images
    "myst_parser",    # Pour le markdown
]
```

# synchro UV + package
`uv sync`
`uv add myst-parser`
`uv add sphinx_gallery`

# Build de la doc
`uv run sphinx-build -b html docs/source public`

# en tête de conf.py
```python
import os
import sys

# pour arriver à la racine du projet C:\GITHUB\Dev-App-uv-sphinx/api
# On remonte à la racine, puis on descend dans 'api'
sys.path.insert(0, os.path.abspath('../../api'))
print(f"DEBUG: Sphinx cherche dans : {os.path.abspath('../../api')}")
```