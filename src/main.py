from utils import parse_jsonl, save_index
from index_builder import build_inverted_index
from feature_index import build_brand_index, build_origin_index
from review_index import build_review_index
from positional_index import build_positional_index

# 📂 Chemins des fichiers
DATA_PATH = "data/products.jsonl"
INDEX_DIR = "index/"

# 🚀 Charger les données produits
print("🔍 Chargement des données...")
products = parse_jsonl(DATA_PATH)

# 📌 Création des index
print("📊 Création des index...")

# 1. Index inversé pour le titre
title_index = build_inverted_index(products, "Title")
save_index(title_index, f"{INDEX_DIR}title_index.json")

# 2. Index inversé pour la description
description_index = build_inverted_index(products, "Description")
save_index(description_index, f"{INDEX_DIR}description_index.json")

# 3. Index des features (marque, origine)
brand_index = build_brand_index(products)
save_index(brand_index, f"{INDEX_DIR}brand_index.json")

origin_index = build_origin_index(products)
save_index(origin_index, f"{INDEX_DIR}origin_index.json")

# 4. Index des reviews
review_index = build_review_index(products)
save_index(review_index, f"{INDEX_DIR}review_index.json")

# 5. Index de position pour le titre
title_pos_index = build_positional_index(products, "Title")
save_index(title_pos_index, f"{INDEX_DIR}title_pos_index.json")

# 6. Index de position pour la description
description_pos_index = build_positional_index(products, "Description")
save_index(description_pos_index, f"{INDEX_DIR}description_pos_index.json")

print("🎉 Tous les index ont été générés avec succès ! ✅")
