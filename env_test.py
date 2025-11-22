
import os
from dotenv import load_dotenv

load_dotenv()

print("OPENAI:", os.getenv("OPENAI_API_KEY")[:5])
print("TWITTER:", os.getenv("TWITTER_API_KEY")[:5])
