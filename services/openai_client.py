from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tweet(commit_msg: str) -> str:
    prompt = (
        f"Turn this commit message into a short, hype, dev-style tweet "
        f"with relevant hashtags. Add a placeholder for the repo URL.\n\n"
        f"Commit: {commit_msg}\n\nTweet:"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )

    return response.choices[0].message.content.strip()
def generate_linkedin_post(commit_msg: str) -> str:
    prompt = (
        f"Turn this commit message into a professional LinkedIn post "
        f"highlighting the technical achievement. Add a placeholder for the repo URL.\n\n"
        f"Commit: {commit_msg}\n\nLinkedIn Post:"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()
def generate_facebook_post(commit_msg: str) -> str:
    prompt = (
        f"Turn this commit message into an engaging Facebook post "
        f"that highlights the update in a casual tone. Add a placeholder for the repo URL.\n\n"
        f"Commit: {commit_msg}\n\nFacebook Post:"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
    )

    return response.choices[0].message.content.strip()

