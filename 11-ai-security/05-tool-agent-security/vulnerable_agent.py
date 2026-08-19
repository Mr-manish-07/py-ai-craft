"""
05 - Tool & Agent Security (Excessive Agency) — Vulnerable Agent (Excessive Agency Demo)
==================================================
DO NOT USE IN PRODUCTION — Illustrates unchecked tool execution
"""


def execute_tool_unchecked(tool_name: str, arguments: dict):
    print(f"=== [VULNERABLE AGENT] Blindly executing {tool_name} with {arguments} ===")


if __name__ == "__main__":
    execute_tool_unchecked("delete_database_table", {"table": "users"})
