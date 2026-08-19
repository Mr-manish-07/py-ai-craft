# Threat Model — 01 - AI Security Fundamentals & OWASP Top 10 for LLMs

## 🛡️ Assets to Protect
1. System prompts & proprietary instructions
2. Tenant & user private data (PII, credentials)
3. Backend execution environment (Tools, DB, Servers)
4. API credits & token budgets

---

## ⚠️ Threats & Attack Vectors (STRIDE / OWASP)
| Threat ID | Threat Category | Description | Severity | Mitigation |
|---|---|---|---|---|
| T-01 | Prompt Injection | User overrides system instructions | High | Delimiter encapsulation, pre-flight guardrails |
| T-02 | Data Exfiltration | Attacker leaks system prompts or user context | High | Output validation, regex PII filter |
| T-03 | Excessive Agency | LLM executes unauthorized destructive actions | Critical | Least privilege, human approval gates |

