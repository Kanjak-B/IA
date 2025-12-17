KEYWORDS = {
    "feat": ["add", "ajout", "create", "implement"],
    "fix": ["fix", "bug", "corrige", "resolve"],
    "refactor": ["refactor", "clean", "amelioration", "improve"],
    "perf": ["optimize", "performance", "speed"],
    "docs": ["doc", "readme"],
}

def detect_commit_type(message):
    msg = message.lower()
    for ctype, words in KEYWORDS.items():
        if any(w in msg for w in words):
            return ctype
    return "unknown"
