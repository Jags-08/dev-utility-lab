import time
from typing import Any, Dict

from dev_utils.math_ops import add, factorial, fibonacci, gcd, is_prime, lcm
from dev_utils.random_ops import generate_password, random_int
from dev_utils.string_ops import is_palindrome, reverse_string


def count_words(text: str) -> int:
    return len(text.split())


# Safe registry of allowed functions
TOOL_REGISTRY = {
    "math/add": {"func": add, "args": ["a", "b"], "types": [float, float]},
    "math/factorial": {"func": factorial, "args": ["n"], "types": [int]},
    "math/is_prime": {"func": is_prime, "args": ["n"], "types": [int]},
    "math/fibonacci": {"func": fibonacci, "args": ["n"], "types": [int]},
    "math/gcd": {"func": gcd, "args": ["a", "b"], "types": [int, int]},
    "math/lcm": {"func": lcm, "args": ["a", "b"], "types": [int, int]},
    "string/reverse": {"func": reverse_string, "args": ["text"], "types": [str]},
    "string/palindrome": {"func": is_palindrome, "args": ["text"], "types": [str]},
    "string/word_count": {"func": count_words, "args": ["text"], "types": [str]},
    "random/generate_password": {"func": generate_password, "args": ["length"], "types": [int]},
    "random/random_int": {"func": random_int, "args": ["min_val", "max_val"], "types": [int, int]},
}


def dispatch_tool(tool_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    if tool_id not in TOOL_REGISTRY:
        return {"success": False, "error": f"Unknown tool: {tool_id}"}

    spec = TOOL_REGISTRY[tool_id]
    func = spec["func"]
    arg_names = spec["args"]
    arg_types = spec["types"]

    # Extract and cast arguments safely
    safe_args = []
    for name, expected_type in zip(arg_names, arg_types):  # type: ignore
        val = payload.get(name)
        if val is None:
            return {"success": False, "error": f"Missing argument: {name}"}
        try:
            # Handle empty strings properly for numeric conversions
            if expected_type in (int, float) and str(val).strip() == "":
                return {"success": False, "error": f"Argument '{name}' cannot be empty."}
            safe_args.append(expected_type(val))
        except (ValueError, TypeError):
            err_msg = f"Invalid type for {name}. Expected {expected_type.__name__}."
            return {"success": False, "error": err_msg}

    # Apply security limits (e.g., limit factorial/fibonacci size to avoid hanging server)
    if "math/factorial" in tool_id and safe_args[0] > 1000:
        return {"success": False, "error": "Value too large for factorial limit (max 1000)"}
    if "math/fibonacci" in tool_id and safe_args[0] > 10000:
        return {"success": False, "error": "Value too large for fibonacci limit (max 10000)"}
    if "random/generate_password" in tool_id and safe_args[0] > 1000:
        return {"success": False, "error": "Password length limit exceeded (max 1000)"}

    start_time = time.time()
    try:
        # We need to ignore type issues here since we are unpacking dynamic args
        result = func(*safe_args)  # type: ignore
        exec_time = time.time() - start_time
        return {"success": True, "result": result, "execution_time_ms": round(exec_time * 1000, 4)}
    except Exception as e:
        return {"success": False, "error": str(e)}
