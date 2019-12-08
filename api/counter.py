from threading import Lock

from functools import wraps

counter_lock = Lock()


def atomic(lock: Lock):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class CounterHandler:
    counter = 0  # cheroot runs on multiple threads but not multiple processes,
    # which simplifies data sharing if memory allows

    @classmethod
    @atomic(counter_lock)
    def get_and_increment_counter(cls):
        result = cls.counter
        cls.counter += 1
        return result
