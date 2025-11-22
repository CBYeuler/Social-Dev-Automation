def clean_commit_message(msg: str) -> str:
    prefixes = ["fix:", "feat:", "chore:", "refactor:", "docs:", "test:"]
    for p in prefixes:
        if msg.lower().startswith(p):
            return msg[len(p):].strip()
    return msg
def format_commit_message(msg: str) -> str:
    cleaned_msg = clean_commit_message(msg)
    if not cleaned_msg.endswith('.'):
        cleaned_msg += '.'
    return cleaned_msg.capitalize()
