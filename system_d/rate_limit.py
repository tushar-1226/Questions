print("Rate limitter implementation with token bucket algorithms.")

import time 
import threading

class TokenBucket:
    def __init__(self, capacity, rate):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_check = time.time()
        self.lock = threading.Lock()

    def allow_request(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_check
            self.last_check = now

            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.rate
            )

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

bucket = TokenBucket(rate=1, capacity=5)

if bucket.allow_request():
    print("Request Allowed")
else:
    print("Too Many Requests.")