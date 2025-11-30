# registry/schema_registry.py

"""
Schema Registry for Veritas Engine
Stores and retrieves versioned schemas.
MVP uses in-memory defaults, upgradeable to ORM-backed SQLite.
"""

from typing import Dict


class SchemaRegistry:

    def __init__(self):
        # MVP in-memory schemas
        # Later versions auto-load from DB (models/schema_orm.py)
        self.schemas = {
            "CODE_DEBUG": {
                "version": "1.0.0",
                "fields": {
                    "language": None,
                    "error_message": None,
                    "file_path": None
                }
            },
            "WEBSITE_DEV": {
                "version": "1.0.0",
                "fields": {
                    "purpose": None,
                    "pages": None,
                    "style": None,
                    "color_palette": None,
                    "examples": None,
                    "deadline": None
                }
            },
            "STORY": {
                "version": "1.0.0",
                "fields": {
                    "genre": None,
                    "tone": None,
                    "characters": None,
                    "setting": None,
                    "theme": None
                }
            },
            "GENERAL": {
                "version": "1.0.0",
                "fields": {
                    "details": None
                }
            }
        }

    def get_schema(self, category: str) -> Dict:
        """
        Return schema for category (fallback to GENERAL)
        """
        return self.schemas.get(category, self.schemas["GENERAL"])
