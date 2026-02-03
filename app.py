from flask import Flask, render_template, request, send_file, after_this_request
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
        outtmpl = f"{DOWNLOAD_DIR}/{filename}.%(ext)s"

        ydl_opts = {
            "outtmpl": outtmpl,
            "format": "best",
            "noplaylist": True,
            "quiet": True,
            "cookies": "cookies.txt",
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filepath = ydl.prepare_filename(info)

            @after_this_request
            def remove_file(response):
                try:
                    os.remove(filepath)
                except Exception as e:
                    print("Gagal hapus:", e)
                return response

            return send_file(filepath, as_attachment=True)

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
