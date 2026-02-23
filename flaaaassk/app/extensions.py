from flask_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()
cache = redis.Redis(host='redis', port=6379, decode_responses=True)