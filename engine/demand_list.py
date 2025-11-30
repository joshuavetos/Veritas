# engine/demand_list.py

"""
Demand List Builder
Takes schema fields and produces structured demand packets.
"""

from typing import Dict, Any


class DemandListBuilder:

    def build(self, schema: Dict, user_input: str) -> Dict:
        """
        schema: {
            "version": "1.0.2",
            "fields": {"language": None, "error_message": None}
        }
        """
        demand_fields = schema.get("fields", {})

        return {
            "schema_version": schema.get("version"),
            "demand_fields": demand_fields,
            "original_input": user_input
        }
