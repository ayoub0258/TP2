# TP2
pour le tp3 :  https://github.com/ayoub0258/TP3.git
## 📌 Description
Ce projet construit plusieurs index à partir d’un fichier JSONL contenant des informations produits pour préparer un moteur de recherche.

## 📂 Structure des index
### **1. Index inversé pour le titre et la description**
- Tokenisation simple (séparation par espace)
- Suppression des stopwords et de la ponctuation
- Associe chaque mot aux URLs des produits où il apparaît

### **2. Index inversé avec positions**
- Ajoute les positions des mots dans les titres et descriptions

### **3. Index des reviews**
- Nombre total de reviews
- Note moyenne
- Dernière note enregistrée

### **4. Index des features (marque, origine, etc.)**
- Associe chaque valeur de feature aux URLs des produits correspondants

## 🚀 Exécution du script
### **Installation des dépendances**
Assurez-vous d’avoir Python 3.7+ installé.  
Clonez le repo et installez les dépendances :
```bash
git clone https://github.com/ayoub0258/TP2.git
pip install nltk