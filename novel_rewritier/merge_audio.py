# merge_audio.py
from pydub import AudioSegment
AudioSegment.converter = "C:\\ProgramData\\chocolatey\\bin\\ffmpeg.exe"  # ✅ 直接指定 ffmpeg 路徑

import os

# 設定資料夾路徑
folder_path = "outputs"
output_file = "outputs/merged_audio.mp3"

# 取得所有 mp3 檔案並排序（確保按 chapter_1.mp3 ~ 順序）
mp3_files = sorted([
    f for f in os.listdir(folder_path)
    if f.endswith(".mp3") and f.startswith("chapter_")
], key=lambda x: int(x.split("_")[1].split(".")[0]))

# 合併音訊
merged = AudioSegment.empty()
for mp3_file in mp3_files:
    print(f"🔊 正在加入：{mp3_file}")
    audio = AudioSegment.from_mp3(os.path.join(folder_path, mp3_file))
    merged += audio

# 輸出
merged.export(output_file, format="mp3")
print(f"✅ 合併完成！輸出檔案：{output_file}")
