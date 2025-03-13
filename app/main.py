from flask import Flask, request, jsonify, render_template
from asgiref.wsgi import WsgiToAsgi
import sqlite3
import uuid

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

# Initialize SQLite Database
DB_FILE = "pastes.db"

def init_db():
    """Create the database table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS pastes (
                id TEXT PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )"""
        )
        conn.commit()

init_db()  # Ensure the table is created

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paste", methods=["POST"])
def create_paste():
    """Handles pasting text and storing it in SQLite."""
    data = request.form.get("text")
    if not data:
        return jsonify({"error": "No text provided"}), 400

    paste_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pastes (id, content) VALUES (?, ?)", (paste_id, data))
        conn.commit()

    return jsonify({"message": "Snippet saved", "url": f"/paste/{paste_id}"}), 201

@app.route("/paste/<paste_id>", methods=["GET"])
def get_paste(paste_id):
    """Retrieves a paste from SQLite."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM pastes WHERE id = ?", (paste_id,))
        result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Paste not found"}), 404

    return jsonify({"paste_id": paste_id, "content": result[0]})

if __name__ == "__main__":
    app.run(debug=True)
