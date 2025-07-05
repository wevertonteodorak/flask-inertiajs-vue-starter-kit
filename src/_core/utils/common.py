import os

def env(key, default=None):
    if key in os.environ:
        return os.environ[key] or default
    else:
        return default