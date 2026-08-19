"""
09 - Denial of Service & Abuse Protection — Resource Abuse & DoS Protection
==================================================
Overview: Mitigating Denial of Wallet / Token exhaustion attacks, quadratic expansion prompts, adaptive rate limiting, and CAPTCHA.
"""


def check_token_budget(prompt: str, max_allowed_tokens: int = 4000) -> bool:
    # Estimate tokens (~4 chars per token)
    est_tokens = len(prompt) // 4
    return est_tokens <= max_allowed_tokens


if __name__ == "__main__":
    print(f"Token budget valid: {check_token_budget('Sample query')}")
