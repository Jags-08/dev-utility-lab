import time
from dev_utils.math_ops import fibonacci, is_prime
from dev_utils.random_ops import generate_password

def profile_startup() -> None:
    print("Profiling application execution paths...")
    t0 = time.time()
    
    # Simulate heavy workload
    fibonacci(30)
    is_prime(100003)
    generate_password(64)
    
    t1 = time.time()
    print(f"Core ops load simulated in {((t1-t0)*1000):.2f}ms")

if __name__ == "__main__":
    profile_startup()
