
# Novel Rewriter 

本project是一個用於「小說仿寫與風格轉換」的自動化工具，能夠透過 OpenAI 的 GPT 模型，依據使用者提供的原始小說與範本風格，自動生成幾篇風格相似的仿寫小說。本工具特別設計給創作者、語音劇腳本製作者，或是需要進行大量小說風格實驗的使用者。

---

## 📁 專案資料夾結構說明
novel_rewriter/
│
├── main.py
├── .env # 儲存 OpenAI API 
├── requirements.txt # Python 套件依賴
│
├── examples/ # 儲存對照組的原始小說
│ ├── novel1_user.txt # 使用者提供的原文小說
│ └── novel1_assistant.txt # 模仿生成的小說（仿寫範本）
│
├── styles/ # 風格描述檔（用來指導模型模仿語氣/敘事方式）
│ └── 狗血優化.txt # 風格提示詞（Style Prompt），例如戲劇化、狗血風格等
│
├── outputs/ # 生成後的小說結果輸出
│ └── novel1_generated.txt # GPT 模型重新仿寫生成的小說
