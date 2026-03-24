from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/app_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/health')
def health():
    return jsonify({"status": "OK.", "message": "Aplikacja działa prawidłowo!"}), 200

@app.route('/')
def index():
    return jsonify({"info": "Wiadomość testowa"}), 200


@app.route('/tasks')
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([{"id": u.id, "name": u.name} for u in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)