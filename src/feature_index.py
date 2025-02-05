def build_brand_index(documents):
    """
    Construit un index des marques pour chaque document.
    """
    brand_index = {}
    for doc in documents:
        url = doc.get("url", "")
        brand = doc.get("product_features", {}).get("brand", "").strip()
        if brand:
            brand_index[url] = brand
    return brand_index

def build_origin_index(documents):
    """
    Construit un index des origines (par exemple, made_in) pour chaque document.
    """
    origin_index = {}
    for doc in documents:
        url = doc.get("url", "")
        origin = doc.get("product_features", {}).get("made in", "").strip()  # Change "origin" to match the actual key
        if origin:
            origin_index[url] = origin
    return origin_index
