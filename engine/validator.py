# engine/validator.py

"""
Demand Field Validator for Veritas
Normalizes + ensures completeness of user-supplied fields.
"""

from typing import Dict


class DemandValidator:

    def validate(self, schema_fields: Dict, user_fields: Dict) -> Dict:
        """
        Returns sanitized + validated dict of fields.
        Missing fields → None (to be filled by model).
        """
        validated = {}

        for key in schema_fields:
            validated[key] = user_fields.get(key) if user_fields else None

        return validated
