"""Automated Quality Gate Script"""

def check_quality_gate(score: float, threshold: float = 0.85) -> bool:
    return score >= threshold
