"""
02 - Direct & Indirect Prompt Injection — Multi-Layered Defense & Sanitization
==================================================
Defensive filters, delimiter boundaries, and validation guards
"""


def sanitize_input(user_input: str) -> str:
    # Delimiter framing and injection pattern detection
    return f"<user_message>\n{user_input.strip()}\n</user_message>"


def validate_defense(user_input: str) -> bool:
    blocked_keywords = ["ignore previous instructions", "system override", "reveal secret"]
    return not any(kw in user_input.lower() for kw in blocked_keywords)


if __name__ == "__main__":
    sample = "Hello, can you help me write Python?"
    print(f"Safe: {validate_defense(sample)}, Sanitized:\n{sanitize_input(sample)}")
