import argparse
import sys
import json
from typing import Optional, List
from .math_ops import add, factorial, gcd, lcm, fibonacci, is_prime
from .string_ops import reverse_string, is_palindrome
from .random_ops import generate_password, random_int, shuffle_list
from .data_ops import read_json, read_file

def main(args: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="dev-utility-lab CLI Toolkit\nA professional Swiss-army knife for terminal environments.",
        epilog="Examples:\n  dev-utils add 5 7\n  dev-utils factorial 5\n  dev-utils reverse-string hello\n",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    subparsers.required = True

    # --- Math ---
    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("a", type=float, help="First number")
    parser_add.add_argument("b", type=float, help="Second number")

    parser_fact = subparsers.add_parser("factorial", help="Calculate factorial of a number")
    parser_fact.add_argument("n", type=int, help="Non-negative integer")

    parser_gcd = subparsers.add_parser("gcd", help="Calculate Greatest Common Divisor")
    parser_gcd.add_argument("a", type=int, help="First integer")
    parser_gcd.add_argument("b", type=int, help="Second integer")

    parser_lcm = subparsers.add_parser("lcm", help="Calculate Least Common Multiple")
    parser_lcm.add_argument("a", type=int, help="First integer")
    parser_lcm.add_argument("b", type=int, help="Second integer")

    parser_fib = subparsers.add_parser("fibonacci", help="Get the n-th Fibonacci number")
    parser_fib.add_argument("n", type=int, help="Integer position")

    parser_prime = subparsers.add_parser("is-prime", help="Check if a number is prime")
    parser_prime.add_argument("n", type=int, help="Integer to check")

    # --- Strings ---
    parser_rev = subparsers.add_parser("reverse-string", help="Reverse a string")
    parser_rev.add_argument("s", type=str, help="String to reverse")

    parser_pal = subparsers.add_parser("palindrome-check", help="Check if a string is a palindrome")
    parser_pal.add_argument("s", type=str, help="String to check")

    # --- Random ---
    parser_pass = subparsers.add_parser("generate-password", help="Generate a random password")
    parser_pass.add_argument("--length", type=int, default=12, help="Length of the password (default: 12)")

    parser_rint = subparsers.add_parser("random-int", help="Generate a random integer between a and b")
    parser_rint.add_argument("a", type=int, help="Lower bound")
    parser_rint.add_argument("b", type=int, help="Upper bound")

    parser_shuffle = subparsers.add_parser("shuffle-list", help="Shuffle a comma-separated list of items")
    parser_shuffle.add_argument("items", type=str, help="Comma-separated items (e.g. 1,2,3)")

    # --- Data ---
    parser_rjson = subparsers.add_parser("read-json", help="Read and print a JSON file")
    parser_rjson.add_argument("filepath", type=str, help="Path to the JSON file")

    parser_rfile = subparsers.add_parser("read-file", help="Read and print a text file")
    parser_rfile.add_argument("filepath", type=str, help="Path to the text file")

    parsed_args = parser.parse_args(args)

    try:
        # Math
        if parsed_args.command == "add":
            res = add(parsed_args.a, parsed_args.b)
            print(int(res) if res.is_integer() else res)
        elif parsed_args.command == "factorial":
            print(factorial(parsed_args.n))
        elif parsed_args.command == "gcd":
            print(gcd(parsed_args.a, parsed_args.b))
        elif parsed_args.command == "lcm":
            print(lcm(parsed_args.a, parsed_args.b))
        elif parsed_args.command == "fibonacci":
            print(fibonacci(parsed_args.n))
        elif parsed_args.command == "is-prime":
            print(is_prime(parsed_args.n))
        # Strings
        elif parsed_args.command == "reverse-string":
            print(reverse_string(parsed_args.s))
        elif parsed_args.command == "palindrome-check":
            print(is_palindrome(parsed_args.s))
        # Random
        elif parsed_args.command == "generate-password":
            print(generate_password(parsed_args.length))
        elif parsed_args.command == "random-int":
            print(random_int(parsed_args.a, parsed_args.b))
        elif parsed_args.command == "shuffle-list":
            lst = [item.strip() for item in parsed_args.items.split(",")]
            print(", ".join(shuffle_list(lst)))
        # Data
        elif parsed_args.command == "read-json":
            print(json.dumps(read_json(parsed_args.filepath), indent=2))
        elif parsed_args.command == "read-file":
            print(read_file(parsed_args.filepath))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
