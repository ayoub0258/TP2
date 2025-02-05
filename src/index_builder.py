import re
from collections import defaultdict
from utils import tokenize_text


def build_inverted_index(documents, field):
    """Créer un index inversé pour un champ donné (titre ou description)."""
    inverted_index = defaultdict(list)
    for doc in documents:
        tokens = tokenize_text(doc.get(field, ""))
        for token in set(tokens):
            inverted_index[token].append(doc['url'])
    return inverted_index
