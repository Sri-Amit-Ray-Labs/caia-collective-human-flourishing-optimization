"""
Minimal Flask app stub for CDI (Collective Deliberation Interface).

Use to present CHFOA decisions and collect human feedback in a web UI.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>CHFOA CDI Stub</h2><p>Hook this up to core modules and templates.</p>"


@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "CHFOA web stub running"})


if __name__ == "__main__":
    app.run(debug=True)
