import re
from collections import defaultdict
from utils import tokenize_text

def build_positional_index(docs, field):
    """Construit un index inversé avec positions pour un champ donné.
    
    Args:
        docs (list): Liste des documents.
        field (str): Nom du champ à indexer ("Title" ou "Description").
    
    Returns:
        dict: Index inversé {mot: {URL: [positions]}}
    """
    positional_index = defaultdict(lambda: defaultdict(list))

    for doc in docs:
        url = doc.get("URL")
        if not url or field not in doc:
            continue  # Ignore les documents mal formés
        
        tokens = tokenize_text(doc[field])  # Tokenisation et nettoyage
        for pos, token in enumerate(tokens):
            positional_index[token][url].append(pos)  # Ajoute la position du mot dans l'URL

    return positional_index
