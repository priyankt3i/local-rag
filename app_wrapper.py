import subprocess
import threading
import webview

def run_streamlit():
    # Run the Streamlit app
    subprocess.Popen(
        ["streamlit", "run", "main.py", "--server.headless=true"],
        shell=True,
    )

if __name__ == "__main__":
    # Start the Streamlit app in a separate thread
    threading.Thread(target=run_streamlit, daemon=True).start()

    # Wait a moment for the app to start
    import time
    time.sleep(2)

    # Open the app in a pywebview window
    webview.create_window("LOCAL-RAG", "http://localhost:8501", width=1024, height=768)
    webview.start()

