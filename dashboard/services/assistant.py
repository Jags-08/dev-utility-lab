import re
from typing import Dict, Any, List

def suggest_utilities(query: str) -> List[Dict[str, str]]:
    """Smart heuristic tool recommendation based on natural language queries."""
    query = query.lower()
    suggestions = []
    
    if re.search(r"password|random|secret|string", query):
        suggestions.append({"id": "random/pwd", "reason": "Generates secure random strings."})
        
    if re.search(r"math|fib|prime|calc", query):
        suggestions.append({"id": "math/fib", "reason": "Calculates Fibonacci sequence fast."})
        suggestions.append({"id": "math/is_prime", "reason": "Determines primality."})
        
    if re.search(r"data|sort|filter|list", query):
        suggestions.append({"id": "data/sort", "reason": "Sorts arrays or objects."})
        
    return suggestions

def contextual_help(tool_id: str) -> str:
    """Provide generative-like hints based on requested tools."""
    hints = {
        "random/pwd": "Tip: Use lengths between 16 and 64 for production secrets. Disable special characters if using for basic API tokens.",
        "math/fib": "Warning: Fibonacci above n=1000 can be computationally expensive; the backend uses LRU caching to optimize repeat runs.",
        "math/is_prime": "Useful for cryptography prototyping and key-generation simulations."
    }
    return hints.get(tool_id, "Explore the parameters panel below to configure this utility.")

def explain_error(error_msg: str) -> str:
    """Local intelligent error explanation."""
    if "too large" in error_msg.lower():
        return "Assistant: It looks like you're trying to process a payload larger than 1MB. Try splitting your data into distinct chunks."
    if "format" in error_msg.lower():
        return "Assistant: The JSON structure is malformed. Ensure keys are quoted and commas correctly placed."
    return f"Assistant suggests reviewing the error trace: {error_msg}"
