import json
import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def tokenize_text(text):
    """
    Tokenize the input text, remove stopwords and punctuation, but keep words intact (no stemming).
    """
    text = text.lower()  # Convertir en minuscule
    tokens = word_tokenize(text)  # Tokeniser le texte
    stop_words = set(stopwords.words('english'))  # Stopwords en anglais
    filtered_tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    return filtered_tokens

def parse_jsonl(file_path):
    """Parse le fichier JSONL et retourne une liste de documents."""
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]

def extract_url_info(url):
    """
    Extraire l'ID produit et la variante (si présente) depuis l'URL.
    """
    parts = url.split('/')
    product_id = None
    variant = None
    for part in parts:
        if part.isdigit():
            product_id = int(part)
        elif part.startswith("variant"):
            variant = part
    return product_id, variant

def save_index(index, file_path):
    """Sauvegarder un index dans un fichier JSON."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=4)



