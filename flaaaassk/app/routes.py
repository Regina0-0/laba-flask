from flask import current_app as app, jsonify, request
from .extensions import db, cache
from .models import Task
import json

@app.route('/tasks', methods=['GET'])
def get_tasks():

    data = cache.get("all_tasks")
    if data:
        return jsonify({"tasks": json.loads(data), "source": "redis_cache"})

    tasks = [{"id": t.id, "title": t.title} for t in Task.query.all()]
    
    cache.setex("all_tasks", 60, json.dumps(tasks))
    return jsonify({"tasks": tasks, "source": "database"})

@app.route('/tasks', methods=['POST'])
def create_task():
    task = Task(title=request.json.get('title', 'No Title'))
    db.session.add(task)
    db.session.commit()
    cache.delete("all_tasks")
    return jsonify({"status": "ok"}), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    cache.delete("all_tasks")
    return jsonify({"status": "deleted"}), 200

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    task.title = request.json.get('title', task.title)
    db.session.commit()
    cache.delete("all_tasks")
    return jsonify({"status": "updated"}), 200