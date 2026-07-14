import redis
import os

AUTH_SESSION_REDIS_URL = os.getenv('AUTH_SESSION_REDIS_URL', 'redis://localhost:6379/0')

SESSION_REDIS_POOL = redis.ConnectionPool.from_url(AUTH_SESSION_REDIS_URL)

def _get_session_redis_client():
    return redis.Redis(connection_pool=SESSION_REDIS_POOL)

GET_SESSION_REDIS_CLIENT = _get_session_redis_client

APPEND_SLASH = False

