import subprocess
from datetime import date

def run_git_command(repo_path, args):
    result = subprocess.run(
        ["git"] + args,
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def get_all_commits(repo_path):
    output = run_git_command(
        repo_path,
        ["log", "--pretty=%H|%s|%an|%ad", "--date=short"]
    )
    commits = []
    for line in output.splitlines():
        h, msg, author, d = line.split("|")
        commits.append({
            "hash": h,
            "message": msg,
            "author": author,
            "date": d
        })
    return commits

def get_today_commits(repo_path):
    today = date.today().isoformat()
    commits = get_all_commits(repo_path)
    return [c for c in commits if c["date"] == today]
