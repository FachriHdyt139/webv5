from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            return "URL kosong!"

        filename = str(uuid.uuid4())

        ydl_opts = {
            'outtmpl': f'{DOWNLOAD_DIR}/{filename}.%(ext)s',
            'format': 'mp4/bestaudio/best',
            'merge_output_format': 'mp4',
            'quiet': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                ext = info.get("ext", "mp4")

            filepath = f"{DOWNLOAD_DIR}/{filename}.{ext}"
            return send_file(filepath, as_attachment=True)

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run()