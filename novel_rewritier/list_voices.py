from elevenlabs import set_api_key, voices
import os
from dotenv import load_dotenv

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

for v in voices():
    print(f"✅ {v.name} - {v.voice_id}")
