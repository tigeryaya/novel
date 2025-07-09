import os
from openai import OpenAI
from dotenv import load_dotenv

# 載入 .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 建立 client（新版寫法）
client = OpenAI(api_key=api_key)

# 讀入原文與仿作
with open("novel_user.txt", "r", encoding="utf-8") as f:
    user_story = f.read()

with open("novel_assistant.txt", "r", encoding="utf-8") as f:
    assistant_story = f.read()

# 對話訊息
messages = [
    {"role": "system", "content": "你是一位擅長模仿狗血小說風格的 AI 作家，請根據下面的對話風格，創作一篇新短劇。"},
    {"role": "user", "content": user_story},
    {"role": "assistant", "content": assistant_story},
    {"role": "user", "content": "再寫一篇"}
]

# 呼叫 ChatGPT API（新版語法）
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # 或 gpt-3.5-turbo
    messages=messages,
    temperature=0.9,
    max_tokens=3000
)

# 取出文字
output = response.choices[0].message.content
print("\n📖 生成的新仿寫內容：\n")
print(output)

# 儲存成 txt
with open("novel_generated.txt", "w", encoding="utf-8") as f:
    f.write(output)