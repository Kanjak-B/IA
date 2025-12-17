# report_generator.py

def generate_report(files, types):
    report = []
    report.append("RAPPORT GIT IA")
    report.append(f"Fichiers modifiés : {len(files)}")

    for k, v in types.items():
        report.append(f"- {k} : {v}")

    if len(files) > 10:
        report.append("Commit trop volumineux recommandé à découper")

    return "\n".join(report)
