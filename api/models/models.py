"""
Ce module gère le chargement et l'exécution du modèle d'IA.
"""

class FakeIAModel:
    """
    Simulateur de modèle d'intelligence artificielle pour la promo 2026.

    Attributes:
        model_name (str): Nom du modèle chargé.
        is_ready (bool): État du modèle (prêt ou non).
    """

    def __init__(self, model_name: str = "Promo-GPT-v1"):
        """
        Initialise le simulateur.

        Args:
            model_name (str): Le nom à donner au modèle.
        """
        self.model_name = model_name
        self.is_ready = True

    def predict(self, text: str) -> str:
        """
        Effectue une prédiction basée sur le texte fourni.

        Args:
            text (str): La donnée d'entrée pour l'inférence.

        Returns:
            str: Le résultat de l'inférence (formaté).
        """
        return f"[{self.model_name}] Résultat pour : {text}"