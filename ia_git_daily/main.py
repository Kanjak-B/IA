import sys
from git_reader import get_all_commits, get_today_commits, run_git_command
from behavior_learner import learn_behavior
from daily_analyzer import analyze_today
from report_generator import generate_report
from commit_intelligence import suggest_commit_message, detect_commit_type

if len(sys.argv) != 2:
    print("Usage: python main.py /chemin/vers/repo_git")
    exit(1)

repo_path = sys.argv[1]

# -------------------------
# Lecture des commits
# -------------------------
all_commits = get_all_commits(repo_path)
today_commits = get_today_commits(repo_path)

# -------------------------
# Apprentissage du comportement
# -------------------------
behavior = learn_behavior(all_commits)

# -------------------------
# Analyse du jour
# -------------------------
today_analysis = analyze_today(today_commits, behavior)

# -------------------------
# Affichage rapport
# -------------------------
report = generate_report(repo_path, behavior, today_analysis)
print("\n" + report)

# -------------------------
# Proposer un message de commit intelligent
# -------------------------
# On récupère les fichiers modifiés aujourd'hui via git status
status_output = run_git_command(repo_path, ["status", "--porcelain"])
files_changed = [line[3:] for line in status_output.splitlines() if line]

if files_changed:
    # Déterminer le type le plus fréquent aujourd'hui ou None
    types_today = [detect_commit_type(c["message"]) for c in today_commits]
    main_type = max(set(types_today), key=types_today.count) if types_today else None

    suggested_commit = suggest_commit_message(files_changed, commit_type=main_type)
    print("\n💡 Suggestion de commit pour aujourd'hui :")
    print(suggested_commit)
else:
    print("\n💡 Aucun fichier modifié aujourd'hui pour proposer un commit")
