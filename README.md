
# Novel Rewriter & TTS Pipeline  
# 小說風格仿寫與語音合成自動化流程

本project是一個用於「小說仿寫與風格轉換」的自動化工具，能夠透過 OpenAI 的 GPT 模型，依據使用者提供的原始小說與範本風格，自動生成幾篇風格相似的仿寫小說。本工具特別設計給創作者、語音劇腳本製作者，或是需要進行大量小說風格實驗的使用者。

This project is an automated tool for “novel imitation and style conversion” that uses OpenAI's GPT model to automatically generate several imitation novels with similar styles based on the original novel and template style provided by the user. This tool is specially designed for creators, voice drama script writers, or users who need to conduct large-scale novel style experiments.

---
## 專案目標 / Project Goals

- ✅ 自動仿寫指定小說風格（風格學習）
- ✅ 控制小說生成長度（如：10,000 字以上）
- ✅ 整合 ElevenLabs 語音合成並合併段落音訊
- ✅ 可套用多主題小說樣式，如狗血愛情、科幻、驚悚等

- Style learning from examples to rewrite novels in a similar tone  
- Control output length (e.g., minimum 10,000 characters or more)  
- Integrate ElevenLabs TTS with paragraph-based merging  
- Flexible for different genres: romance, sci-fi, thriller, etc.


## 📁 專案資料夾結構說明
├── examples/               # 範例對話片段（風格對照） / Example reference texts
│   ├── novel1_user.txt     # 使用者原始段落 / Original user input
│   └── novel1_assistant.txt# AI 改寫範本 / Assistant rewrite reference

├── outputs/                # 輸出結果 / Final outputs
│   ├── novel1_generated.txt# 最終生成小說 / Final generated novel
│   └── merged_audio.wav    # 合併音訊 / Final merged audio

├── styles/                 # 類型風格提煉檔 / Extracted style prompts
│   └── 狗血愛情風格.txt     # Example: dramatic romance style

├── main.py                 # 主程式：風格學習與內容生成 / Main pipeline
├── tts.py                  # TTS 語音合成腳本 / Text-to-speech
├── merge_audio.py          # 音訊合併腳本 / Audio merger
├── list_voices.py          # ElevenLabs 語音列舉 / List all available voices
├── style_generator.py      # 風格萃取器 / Extract style prompt from references

├── .env                    # API 金鑰環境設定檔 / API key config
├── requirements.txt        # Python 相依套件 / Required libraries

--------

Set up
建立虛擬環境（可選） / (Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate  # Windows 請改用 venv\Scripts\activate


安裝必要套件 / Install dependencies

pip install -r requirements.txt


建立 .env 並加入金鑰 / Set API keys

OPENAI_API_KEY=你的OpenAI金鑰/key
ELEVEN_API_KEY=你的ElevenLabs金鑰/key

---

##How to use
1. 放入風格範本 / Prepare Style Examples

將對照組小說片段放入 examples/ 中，例如：

novel1_user.txt → 原始段落

novel1_assistant.txt → AI 改寫版本

建議選用具有代表性的幾段片段，不需完整小說

Use representative sections only (not full novels) to teach the style.
You only need to include 3–5 representative pairs of text; full novels are not required


still working on it...
