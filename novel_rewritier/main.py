import os
import re
from pathlib import Path
from openai import OpenAI
from pydub import AudioSegment
from pydub.utils import which
from dotenv import load_dotenv 

load_dotenv()

# 設定 ffmpeg 路徑（適用 Windows 安裝 Chocolatey 的情況）
AudioSegment.converter = which("ffmpeg") or "C:\\ProgramData\\chocolatey\\bin\\ffmpeg.exe"

client = OpenAI()

# 輸入檔案：只需提供 novel_user.txt
user_input_path = "examples/novel_user.txt"

# 讀取範本小說內容
with open(user_input_path, "r", encoding="utf-8") as f:
    user_story = f.read()

# 自動建立風格提示（不需再提供 novel_assistant.txt）
def extract_style_prompt(user):
    return f"以下是使用者提供的小說片段：\n{user}\n\n請模仿這段的語氣與風格，創作新的章節內容。"

style_prompt = extract_style_prompt(user_story)

# 儲存用
chapters = []
merged_audio = None

# 開始分章生成
for i in range(1, 11):
    chapter_prompt = f"請根據上述風格，生成第 {i} 章，長度約 1000–1200 字，請用 ### Chapter{i} 開頭。不要重複前面章節內容。"

    messages = [
        {"role": "system", "content": style_prompt},
        {"role": "user", "content": user_story},
        {"role": "user", "content": chapter_prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.95,
        max_tokens=2048
    )

    chapter_text = response.choices[0].message.content
    print(f"✅ 第 {i} 章完成，字數：{len(chapter_text)}")
    chapters.append(chapter_text)

    # 儲存章節文字
    txt_path = f"outputs/chapter_{i}.txt"
    Path(txt_path).write_text(chapter_text, encoding="utf-8")

    # 產生 mp3（僅用前 400 字）
    from tts import generate_audio
    mp3_path = f"outputs/chapter_{i}.mp3"
    tts_preview = re.sub(r"^#+\s*Chapter\s*\d+", "", chapter_text).strip()[:400]
    generate_audio(tts_preview, mp3_path)

    # 合併音訊
    if os.path.exists(mp3_path):
        segment = AudioSegment.from_mp3(mp3_path)
        merged_audio = segment if merged_audio is None else merged_audio + segment

# 合併音訊檔案輸出
if merged_audio:
    merged_audio.export("outputs/full_novel_merged.mp3", format="mp3")
    print("🎧 成功輸出合併語音檔 outputs/full_novel_merged.mp3")

# 合併文字輸出
full_text = "\n\n".join(chapters)
Path("outputs/full_novel.txt").write_text(full_text, encoding="utf-8")
print("📖 全部章節文字與語音生成完成！")
