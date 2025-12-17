from commit_intelligence import detect_commit_type

def analyze_today(commits_today, behavior):
    analysis = {
        "count": len(commits_today),
        "types": {},
        "alerts": [],
        "quality_score": 100
    }

    if not commits_today:
        analysis["alerts"].append("Aucun commit aujourd’hui")
        analysis["quality_score"] = 0
        return analysis

    for c in commits_today:
        ctype = detect_commit_type(c["message"])
        analysis["types"][ctype] = analysis["types"].get(ctype, 0) + 1

        if ":" not in c["message"]:
            analysis["alerts"].append(
                f"Message non structuré : '{c['message']}'"
            )
            analysis["quality_score"] -= 10

        if len(c["message"]) < behavior["avg_message_length"] * 0.6:
            analysis["quality_score"] -= 5

    if analysis["count"] > behavior["avg_commits_per_day"] * 2:
        analysis["alerts"].append("Beaucoup de commits → possible fragmentation")
        analysis["quality_score"] -= 10

    return analysis
