import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"cm_timer_1: {self.elapsed_time:.3f} seconds")
        
    def get_time(self):
        
        return self.elapsed_time

@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"cm_timer_2: {elapsed_time:.3f} seconds")


if __name__ == "__main__":
    print("=== Testing cm_timer_1 ===")
    with cm_timer_1():
        time.sleep(1.5)
    
    print("\n=== Testing cm_timer_2 ===")
    with cm_timer_2():
        time.sleep(0.7)
    
    print("\n=== Testing with calculations ===")
    with cm_timer_1():
        
        result = sum(i**2 for i in range(1000000))
        print(f"Result: {result}")