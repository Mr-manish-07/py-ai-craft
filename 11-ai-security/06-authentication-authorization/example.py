"""
06 - AI Authentication & Tenant Authorization — Authentication & Tenant Authorization Example
==================================================
Overview: Securing AI endpoints with JWT/OAuth2, per-tenant vector filtering, and fine-grained role-based access control (RBAC).
"""


def check_tenant_access(user_tenant_id: str, document_tenant_id: str) -> bool:
    return user_tenant_id == document_tenant_id


if __name__ == "__main__":
    print(f"Tenant match: {check_tenant_access('tenant_a', 'tenant_a')}")
