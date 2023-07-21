#!/usr/bin/env python3
"""
This script provides a class that illustrates how strings
can be stored in Redis.

Happy Coding!
"""
from uuid import uuid4


class Cache():
    """store an instance of the Redis client
    as a private variable named _redis (using
    redis.Redis()) and flush the instance using
    flushdb"""
    def __init__(self):
        """Initialize the class"""
        import redis
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Create a store method that takes a
        data argument and returns a string."""
        id = str(uuid4())
        self._redis.set(id, data)
        return id
