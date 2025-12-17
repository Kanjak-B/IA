# commit_intelligence.py

KEYWORDS = {
    "feat": ["add", "ajout", "create", "implement", "new"],
    "fix": ["fix", "bug", "corrige", "resolve", "error"],
    "refactor": ["refactor", "clean", "amelioration", "improve", "update"],
    "perf": ["optimize", "performance", "speed", "efficient"],
    "docs": ["doc", "readme", "documentation"],
    "chore": ["chore", "cleanup", "config", "setup"]
}

def detect_commit_type(message):
    """
    Détecte automatiquement le type du commit
    """
    msg = message.lower()
    for ctype, words in KEYWORDS.items():
        if any(w in msg for w in words):
            return ctype
    return "unknown"

def suggest_commit_message(files_changed, commit_type=None):
    """
    Génère un message de commit suggéré basé sur les fichiers modifiés
    et le type de commit détecté ou choisi.
    """
    if not files_changed:
        return "chore: mise à jour"

    # Déterminer un type automatiquement si non fourni
    if not commit_type:
        commit_type = "feat" if any(f.endswith((".py", ".js", ".php")) for f in files_changed) else "chore"

    # Générer un scope (premier dossier modifié ou 'core')
    scope = files_changed[0].split("/")[0] if "/" in files_changed[0] else "core"

    # Générer un message descriptif simple
    description = ", ".join([f for f in files_changed[:3]])  # max 3 fichiers dans le résumé

    message = f"{commit_type}({scope}): {description}"
    if len(files_changed) > 3:
        message += " et d'autres fichiers"

    return message
