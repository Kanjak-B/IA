def generate_report(repo_path, behavior, today):
    report = []

    report.append("🧠 RAPPORT IA GIT – ANALYSE QUOTIDIENNE\n")
    report.append(f"📂 Repo : {repo_path}\n")

    report.append("📊 Ton profil Git :")
    report.append(f"- Commits / jour (moyenne) : {behavior['avg_commits_per_day']}")
    report.append(f"- Longueur message moyenne : {behavior['avg_message_length']}")
    report.append(f"- Types dominants : {behavior['commit_types']}\n")

    report.append("📅 Aujourd’hui :")
    report.append(f"- Nombre de commits : {today['count']}")
    report.append(f"- Types détectés : {today['types']}")
    report.append(f"- Score qualité Git : {today['quality_score']} / 100\n")

    if today["alerts"]:
        report.append("⚠️ Alertes :")
        for a in today["alerts"]:
            report.append(f"- {a}")
    else:
        report.append("✅ Aucun problème détecté")

    if today["quality_score"] < 70:
        report.append("\n🛠 Recommandation :")
        report.append("- Structurer les messages (type: description)")
        report.append("- Regrouper les changements similaires")

    return "\n".join(report)
