from dotenv import load_dotenv
load_dotenv()

from services.openai_client import generate_tweet

print(generate_tweet("Added new authentication module"))

