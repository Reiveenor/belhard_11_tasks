import time

from utils import decorator


@decorator
def one():
    time.sleep(1)
