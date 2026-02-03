<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TikTok Downloader</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;
}

.card {
    background: white;
    padding: 25px;
    width: 100%;
    max-width: 420px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,.2);
}

input {
    width: 100%;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

button {
    width: 100%;
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: #2563eb;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:disabled {
    background: #999;
}

#loader {
    display: none;
    margin-top: 20px;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #ddd;
    border-top: 4px solid #2563eb;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: auto;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.progress {
    height: 8px;
    background: #eee;
    border-radius: 5px;
    overflow: hidden;
    margin-top: 10px;
}

.bar {
    width: 0%;
    height: 100%;
    background: #2563eb;
    transition: width 0.4s;
}
</style>
</head>

<body>
<div class="card">
    <h2>🎵 TikTok Downloader</h2>

    <form id="downloadForm" method="POST">
        <input type="text" name="url" placeholder="Paste URL TikTok" required>
        <button type="submit">Download</button>
    </form>

    <div id="loader">
        <div class="spinner"></div>
        <div class="progress">
            <div class="bar" id="bar"></div>
        </div>
        <p>Sedang memproses...</p>
    </div>
</div>

<script>
const form = document.getElementById("downloadForm");
const loader = document.getElementById("loader");
const bar = document.getElementById("bar");
const btn = form.querySelector("button");

form.addEventListener("submit", () => {
    loader.style.display = "block";
    btn.disabled = true;

    let progress = 0;
    const interval = setInterval(() => {
        if (progress < 90) {
            progress += 10;
            bar.style.width = progress + "%";
        }
    }, 500);
});
</script>

</body>
</html>

