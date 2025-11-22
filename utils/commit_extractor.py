import subprocess

def get_latest_commit_message():
    result = subprocess.check_output(
        ["git", "log", "-1", "--pretty=format:%s"]
    )
    return result.decode("utf-8")


