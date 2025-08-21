# style_generator.py
import difflib

def extract_style_prompt(user_text: str, assistant_text: str) -> str:
    """
    根據 user 原文 和 assistant 仿作，自動生成風格 system prompt
    只取各 300 字內內容，以節省 token 使用
    """
    # 只取前 300 字
    user_sample = user_text[:300].strip()
    assistant_sample = assistant_text[:300].strip()

    # 差異比對（可選擇性使用）
    matcher = difflib.SequenceMatcher(None, user_sample, assistant_sample)
    similarity = matcher.ratio()

    prompt = f"""
請根據以下仿寫範本的語氣、敘事風格與敘述節奏，
模仿其小說風格進行創作：

- 範本風格相似度（僅供參考）：{similarity:.2%}
- 使用者原文片段：
「{user_sample}」

- 助手仿寫風格片段：
「{assistant_sample}」

請延續上述仿寫片段的敘事語氣，強調誇張情緒、情節轉折、
狗血衝突、情感虐戀、戲劇化對話等要素。
請模仿並持續創作風格一致的長篇小說。
"""
    return prompt.strip()
