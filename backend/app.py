from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from analyzer import analyze_logs
import os

app = Flask(__name__, static_folder="../frontend")

CORS(app)


# -------- FRONTEND --------

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")


# -------- API --------

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    logs = data.get("logs")

    if not logs:
        return jsonify({"error": "No logs provided"}), 400

    result = analyze_logs(logs)

    return jsonify(result)


@app.route("/analyze-file", methods=["POST"])
def analyze_file():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    content = file.read().decode("utf-8")

    result = analyze_logs(content)

    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)