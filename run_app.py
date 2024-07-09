import subprocess
import os

# 確保在當前腳本的目錄中運行
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(current_dir, 'app.py')

try:
    # 使用 subprocess 運行 Streamlit 並捕獲輸出
    result = subprocess.run(['streamlit', 'run', app_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 將 stdout 和 stderr 寫入日誌文件
    with open('streamlit_output.log', 'w') as f:
        f.write(result.stdout)
    with open('error_log.txt', 'w') as f:
        f.write(result.stderr)
except Exception as e:
    # 捕獲可能的異常並寫入錯誤日誌
    with open('error_log.txt', 'w') as f:
        f.write(str(e))
