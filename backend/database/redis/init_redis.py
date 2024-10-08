import redis
from flask import current_app

def get_redis_client():
    redis_client = redis.StrictRedis(
        host=current_app.config['REDIS_HOST'],
        port=current_app.config['REDIS_PORT'],
        db=current_app.config['REDIS_DB'],
        decode_response=True
    )

    return redis_client

