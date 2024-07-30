from threading import Thread
from multiprocessing import Process


def threadFunc():
    def decorator(func):
        def wrapper(*args, **kwargs):
            thread = Thread(target=func, args=args, kwargs=kwargs, daemon=True)
            thread.start()

        return wrapper

    return decorator


def processFunc():
    def decorator(func):
        def wrapper(*args, **kwargs):
            thread = Process(target=func, args=args, kwargs=kwargs, daemon=True)
            thread.start()

        return wrapper

    return decorator
