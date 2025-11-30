# engine/demand_engine.py

"""
Demand Engine - MVP Pipeline
1. Classify input
2. Fetch schema
3. Build demand list
4. Merge into prompt template
"""

from typing import Dict

from engine.classifier import classify_text
from engine.demand_list import DemandListBuilder
from engine.validator import DemandValidator

from registry.schema_registry import SchemaRegistry
from registry.prompt_registry import PromptRegistry


class DemandEngine:

    def __init__(self):
        self.schema_registry = SchemaRegistry()
        self.prompt_registry = PromptRegistry()
        self.builder = DemandListBuilder()
        self.validator = DemandValidator()

    def process(self, user_input: str) -> Dict:
        # Step 1: classify
        cls = classify_text(user_input)

        # Step 2: get schema
        schema = self.schema_registry.get_schema(cls["category"])

        # Step 3: build demand list
        demand_list = self.builder.build(schema, user_input)

        # Step 4: create optimized prompt
        optimized_prompt = self.prompt_registry.render_template(
            cls["category"],
            demand_list
        )

        return {
            "classifier": cls,
            "schema": schema,
            "demand_list": demand_list,
            "optimized_prompt": optimized_prompt
        }
