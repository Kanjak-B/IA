# commit_analyzer.py

def analyze_changes(status_lines):
    files = []
    types = {"code": 0, "config": 0, "docs": 0}

    for line in status_lines:
        file = line[3:]
        files.append(file)

        if file.endswith((".py", ".js", ".php")):
            types["code"] += 1
        elif file.endswith((".md", ".txt")):
            types["docs"] += 1
        else:
            types["config"] += 1

    return files, types
