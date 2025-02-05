import json

def build_review_index(documents):
    """
    Build a review index containing total reviews, average rating, and last rating.
    """
    review_index = {}

    for doc in documents:
        url = doc.get("url", "")
        reviews = doc.get("product_reviews", [])  # Reviews should be a list of dictionaries
        
        # Extraire les notes (rating) qui sont des nombres
        ratings = [review.get("rating", 0) for review in reviews if isinstance(review.get("rating"), (int, float))]
        total_reviews = len(ratings)  # Compter uniquement les critiques ayant des ratings valides
        
        # Calculer la moyenne et récupérer la dernière note
        avg_rating = sum(ratings) / total_reviews if total_reviews > 0 else 0
        last_rating = ratings[-1] if ratings else 0

        # Construire l'index
        review_index[url] = {
            "total_reviews": total_reviews,
            "average_rating": avg_rating,
            "last_rating": last_rating,
        }

    return review_index
