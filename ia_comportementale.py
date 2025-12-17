# =========================================
# IA COMPORTEMENTALE - VERSION BASIQUE
# @author : Kanjak
# @date : 17/12/2025
# @file : ia_comportementale.py
# =========================================

# -------------------------
# 1. Données d'apprentissage
# -------------------------
# (temps_reponse, regards_evites, stress, resultat)
donnees = [
    (2, 0, 1, "normal"),
    (3, 1, 2, "normal"),
    (5, 2, 3, "normal"),
    (8, 4, 7, "suspect"),
    (10, 5, 8, "suspect"),
    (12, 6, 9, "suspect"),
]

# -------------------------
# 2. Fonction de score
# -------------------------
def score_comportement(temps, regards, stress):
    """
    Transforme un comportement humain en score numérique
    """
    return (temps * 0.4) + (regards * 1.5) + (stress * 2)


# -------------------------
# 3. Entraînement (apprendre le seuil)
# -------------------------
def entrainer(donnees):
    scores_normaux = []
    scores_suspects = []

    for temps, regards, stress, resultat in donnees:
        score = score_comportement(temps, regards, stress)

        if resultat == "normal":
            scores_normaux.append(score)
        else:
            scores_suspects.append(score)

    # Le seuil est entre normal et suspect
    seuil = (max(scores_normaux) + min(scores_suspects)) / 2
    return seuil


# -------------------------
# 4. Décision IA
# -------------------------
def ia_comportementale(temps, regards, stress, seuil):
    score = score_comportement(temps, regards, stress)

    if score > seuil:
        return "suspect", score
    else:
        return "normal", score


# -------------------------
# 5. Programme principal
# -------------------------
if __name__ == "__main__":
    seuil = entrainer(donnees)

    print("=== IA COMPORTEMENTALE ===")
    print(f"Seuil appris : {seuil:.2f}\n")

    # Tests
    tests = [
        (4, 1, 2),
        (6, 3, 4),
        (9, 5, 8),
    ]

    for temps, regards, stress in tests:
        decision, score = ia_comportementale(temps, regards, stress, seuil)
        print(
            f"Temps: {temps}s | Regards: {regards} | Stress: {stress} "
            f"=> Score: {score:.2f} => {decision.upper()}"
        )
