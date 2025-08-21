from pydub import AudioSegment

# 手動指定 ffmpeg 路徑（請依你實際路徑修改）
AudioSegment.converter = r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"

try:
    # 建立 1 秒靜音 mp3 檔案測試輸出
    silent = AudioSegment.silent(duration=1000)  # 1000 毫秒 = 1 秒
    silent.export("ffmpeg_test_output.mp3", format="mp3")
    print("✅ ffmpeg 測試成功，已輸出 mp3 檔案！")

except Exception as e:
    print("❌ ffmpeg 測試失敗：", e)
