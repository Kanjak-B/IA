# commit_generator.py

def generate_commit_message(files, types):
    main_type = max(types, key=types.get)

    if main_type == "code":
        prefix = "feat" if len(files) > 3 else "fix"
    elif main_type == "docs":
        prefix = "docs"
    else:
        prefix = "chore"

    scope = files[0].split("/")[0] if "/" in files[0] else "core"

    message = f"{prefix}({scope}): update {len(files)} files"

    return message
