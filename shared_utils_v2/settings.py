import redis
import os

SESSION_REDIS_HOST = os.getenv('SESSION_REDIS_HOST', 'localhost')
SESSION_REDIS_PORT = os.getenv('SESSION_REDIS_PORT', 6379)
SESSION_REDIS_DB = os.getenv('SESSION_REDIS_DB', 0)

SESSION_REDIS_POOL = redis.ConnectionPool(
    host=SESSION_REDIS_HOST, port=SESSION_REDIS_PORT, 
    db=SESSION_REDIS_DB, decode_responses=True
)

def _get_session_redis_client():
    return redis.Redis(connection_pool=SESSION_REDIS_POOL)

get_session_redis_client = _get_session_redis_client
