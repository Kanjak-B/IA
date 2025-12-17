from commit_intelligence import detect_commit_type

def learn_behavior(commits):
    stats = {
        "avg_message_length": 0,
        "commit_types": {},
        "avg_commits_per_day": 0
    }

    if not commits:
        return stats

    total_length = 0
    days = set()

    for c in commits:
        msg = c["message"]
        total_length += len(msg)
        days.add(c["date"])

        ctype = detect_commit_type(msg)
        stats["commit_types"][ctype] = stats["commit_types"].get(ctype, 0) + 1

    stats["avg_message_length"] = total_length // len(commits)
    stats["avg_commits_per_day"] = len(commits) // len(days)

    return stats
