# main.py

from git_reader import get_git_status
from commit_analyzer import analyze_changes
from commit_generator import generate_commit_message
from report_generator import generate_report

status = get_git_status()

if not status:
    print("Aucun changement détecté.")
    exit()

files, types = analyze_changes(status)

print("\n--- MESSAGE DE COMMIT SUGGÉRÉ ---")
print(generate_commit_message(files, types))

print("\n--- RAPPORT IA ---")
print(generate_report(files, types))
