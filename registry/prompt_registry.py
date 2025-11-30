# registry/prompt_registry.py

"""
Prompt Template Registry
Stores templates and renders them with demand list data.
"""

from typing import Dict


class PromptRegistry:

    def __init__(self):
        # MVP templates
        self.templates = {
            "CODE_DEBUG": """\
Task: Debugging task for category {category}

User Input:
{original_input}

Specifications:
{specs}

Instructions:
Analyze the error, identify root cause, provide corrected code AND explanation.
""",

            "WEBSITE_DEV": """\
Task: Website Development

User Input:
{original_input}

Requirements:
{specs}

Instructions:
Provide structure, components, technologies, and file layout.
""",

            "STORY": """\
Task: Creative Writing

Prompt:
{original_input}

Story Requirements:
{specs}

Instructions:
Generate a coherent narrative that fits tone, theme, and character details.
""",

            "GENERAL": """\
Task:

{original_input}

Details:
{specs}
"""
        }

    def render_template(self, category: str, demand_list: Dict) -> str:
        template = self.templates.get(category, self.templates["GENERAL"])

        specs = "\n".join(
            f"- {k}: {v if v is not None else '[missing]'}"
            for k, v in demand_list["demand_fields"].items()
        )

        return template.format(
            category=category,
            original_input=demand_list["original_input"],
            specs=specs
        )
