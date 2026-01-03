import subprocess
import sys

def run_doc():
    """Génère la doc Sphinx"""
    subprocess.run(["sphinx-build", "-b", "html", "docs/source", "public"])

