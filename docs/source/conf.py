import os
import sys

# pour arriver à la racine du projet C:\GITHUB\Dev-App-uv-sphinx/api
# On remonte à la racine, puis on descend dans 'api'
sys.path.insert(0, os.path.abspath('../../api'))
print(f"DEBUG: Sphinx cherche dans : {os.path.abspath('../../api')}")

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DEV-APP-UV-SPHINX'
copyright = '2026, moi'
author = 'moi'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Importation du thème (optionnel selon les versions, mais recommandé)
import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',  # Pour extraire la doc de ton code
    'sphinx.ext.napoleon', # Pour supporter les docstrings style Google/NumPy
    'sphinx.ext.mathjax', # Pour latex 
    "sphinx.ext.viewcode",
    "myst_parser",    
]


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
