import time

from utils import class_decorator


@class_decorator
class Waiting:
    def two(self):
        time.sleep(2)

    def three(self):
        time.sleep(3)
