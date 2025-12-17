# git_reader.py
import subprocess

def get_git_status():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().splitlines()


def get_git_diff():
    result = subprocess.run(
        ["git", "diff", "--stat"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
