# config.py

"""
Global configuration for Veritas Engine (MVP).
"""

import os

# ---------------------------------------------------------
# VERSIONING
# ---------------------------------------------------------
VERITAS_VERSION = "0.1.0-mvp"

# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------
# SQLite for MVP; can become Postgres via environment variable
DATABASE_URL = os.getenv("VERITAS_DB_URL", "sqlite:///./veritas.db")

# ---------------------------------------------------------
# LOGGING
# ---------------------------------------------------------
AUDIT_DB_PATH = os.getenv("VERITAS_AUDIT_DB", "veritas_audit.db")
ENABLE_LOGGING = True

# ---------------------------------------------------------
# DEMAND ENGINE SETTINGS
# ---------------------------------------------------------
MAX_FIELDS = 12
