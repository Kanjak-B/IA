import sys
from git_reader import get_all_commits, get_today_commits
from behavior_learner import learn_behavior
from daily_analyzer import analyze_today
from report_generator import generate_report

if len(sys.argv) != 2:
    print("Usage: python main.py /chemin/vers/repo_git")
    exit(1)

repo_path = sys.argv[1]

all_commits = get_all_commits(repo_path)
today_commits = get_today_commits(repo_path)

behavior = learn_behavior(all_commits)
today_analysis = analyze_today(today_commits, behavior)

report = generate_report(repo_path, behavior, today_analysis)

print("\n" + report)
