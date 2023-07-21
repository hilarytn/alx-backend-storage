#!/usr/bin/env python3
"""
This script provides a class that illustrates how strings
can be stored in Redis.

Happy Coding!
"""
from uuid import uuid4


class Cache():
    """This class will cache data as parsed from the store method"""
    def __init__(self):
        import redis
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        id = str(uuid4())
        self._redis.set(id, data)
        return id
