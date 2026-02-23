import os

class Config:
    # настрока посгри
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://maymay:maymay@db:5432/flaskdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Настройки редиски
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379