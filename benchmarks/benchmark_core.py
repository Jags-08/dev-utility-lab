import timeit
from typing import Dict, Any

def run_benchmarks() -> Dict[str, Any]:
    print("Running Benchmarks...")
    
    fib_time = timeit.timeit("fibonacci(15)", setup="from dev_utils.math_ops import fibonacci", number=1000)
    print(f"Fibonacci(15) 1000x: {fib_time:.4f}s")
    
    pal_time = timeit.timeit("is_palindrome('A man a plan a canal Panama')", setup="from dev_utils.string_ops import is_palindrome", number=10000)
    print(f"Palindrome check 10000x: {pal_time:.4f}s")
    
    pwd_time = timeit.timeit("generate_password(16)", setup="from dev_utils.random_ops import generate_password", number=10000)
    print(f"Generate Password 10000x: {pwd_time:.4f}s")

    return {
        "fibonacci_15_1000x": round(fib_time, 4),
        "palindrome_10000x": round(pal_time, 4),
        "generate_password_10000x": round(pwd_time, 4),
    }

if __name__ == "__main__":
    run_benchmarks()
