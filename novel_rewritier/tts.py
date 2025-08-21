# tts.py
import os
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv

# 載入 ElevenLabs 金鑰
load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

# 語音合成函式
def generate_audio(text: str, filename: str = "chapter.mp3", voice: str = "George"):
    try:
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2",  # 支援中英文
             voice_settings={
                "stability": 0.7,
                "similarity_boost": 0.9,
                "style": 1,   # 情緒（0~1）
                "speed": 1.25   # 語速（0.5 = 慢速, 1.0 = 正常, 1.5 = 快速）
            }
        )
        save(audio, filename)
        print(f"✅ 語音儲存完成：{filename}")
    except Exception as e:
        print(f"❌ 語音合成失敗：{e}")
