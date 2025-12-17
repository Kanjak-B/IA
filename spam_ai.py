# =========================================
# IA DE DETECTION DE SPAM - VERSION REELLE
# @author : Kanjak
# @date : 17/12/2025
# @file : spam_ai.py
# =========================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -------------------------
# 1. Données d'apprentissage
# -------------------------
messages = [
    "Gagnez de l'argent rapidement",
    "Cliquez ici pour un cadeau",
    "Offre limitée gagnez maintenant",
    "Urgent votre compte est bloqué",
    "Salut comment tu vas",
    "On se voit ce soir",
    "Le cours commence à 8h",
    "Merci pour ton aide",
]

labels = [
    "spam",
    "spam",
    "spam",
    "spam",
    "normal",
    "normal",
    "normal",
    "normal",
]

# -------------------------
# 2. Vectorisation (texte → nombres)
# -------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# -------------------------
# 3. Entraînement du modèle
# -------------------------
model = MultinomialNB()
model.fit(X, labels)

# -------------------------
# 4. Prédiction
# -------------------------
def detect_spam(message):
    vect = vectorizer.transform([message])
    prediction = model.predict(vect)[0]
    proba = model.predict_proba(vect).max()
    return prediction, proba


# -------------------------
# 5. Tests
# -------------------------
tests = [
    "Urgent gagnez un million maintenant",
    "Salut tu es où ?",
    "Clique pour récupérer ton argent",
]

for msg in tests:
    resultat, confiance = detect_spam(msg)
    print(f"Message: {msg}")
    print(f"➡️  {resultat.upper()} ({confiance*100:.1f}%)\n")
