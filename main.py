from utils.commit_extractor import get_latest_commit_message
from utils.formatter import clean_commit_message
from services.openai_client import generate_tweet
from services.twitter_client import post_tweet

def main():
    raw_commit = get_latest_commit_message()
    cleaned_commit = clean_commit_message(raw_commit)
    tweet = generate_tweet(cleaned_commit)
    post_tweet(tweet)
    print("Tweet sent:", tweet)




if __name__ == "__main__":
    main()
