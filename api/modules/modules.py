"""
Modules utilitaires pour la manipulation de fichiers.
"""

def read_config_file(file_path: str) -> str:
    """
    Lit un fichier texte et retourne son contenu.

    Args:
        file_path (str): Le chemin vers le fichier .txt à lire.

    Returns:
        str: Le contenu brut du fichier.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas au chemin indiqué.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()