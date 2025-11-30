# logger.py

"""
Veritas Engine - Audit Logger
Stores immutable JSON audit packets in SQLite.
"""

import uuid
import json
import sqlite3
import datetime
from config import AUDIT_DB_PATH


def init_audit_db():
    """Initialize the SQLite audit table if missing."""
    conn = sqlite3.connect(AUDIT_DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            run_id TEXT,
            timestamp TEXT,
            component TEXT,
            payload TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_event(component: str, payload: dict, run_id: str = None):
    """
    Write one audit packet (immutable).

    Parameters:
        component (str): subsystem name ("classifier", "planner", etc.)
        payload (dict): JSON-serializable audit data
        run_id (str): persistent ID linking all steps of one execution
    """
    if run_id is None:
        run_id = str(uuid.uuid4())

    timestamp = datetime.datetime.utcnow().isoformat()

    conn = sqlite3.connect(AUDIT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO audit_logs (run_id, timestamp, component, payload)
        VALUES (?, ?, ?, ?)
    """, (run_id, timestamp, component, json.dumps(payload)))

    conn.commit()
    conn.close()

    return run_id


def fetch_logs(run_id: str):
    """Retrieve all audit packets for a given run_id."""
    conn = sqlite3.connect(AUDIT_DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT component, payload
        FROM audit_logs
        WHERE run_id = ?
    """, (run_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"component": comp, "payload": json.loads(pay)}
        for comp, pay in rows
    ]
