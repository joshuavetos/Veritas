# engine/classifier.py

"""
MVP Classifier for Veritas Engine
Lightweight rules → category + subtype + confidence score.
"""

import re
from typing import Dict


class Classifier:
    """
    Rule-based classifier for MVP Veritas.
    Later versions can swap in ML or hybrid models.
    """

    def __init__(self):
        # simple keyword maps for MVP categories
        self.rules = {
            "CODE_DEBUG": [
                r"error", r"traceback", r"bug", r"debug", r"exception",
                r"crash", r"fix this code"
            ],
            "WEBSITE_DEV": [
                r"website", r"html", r"css", r"react", r"frontend",
                r"landing page", r"build me a site"
            ],
            "STORY": [
                r"story", r"plot", r"write", r"novel", r"scene",
                r"character", r"fantasy", r"fiction"
            ],
            "DATA_TASK": [
                r"csv", r"data", r"analyze", r"pandas", r"table",
                r"visualize", r"chart", r"graph"
            ]
        }

    def classify(self, text: str) -> Dict:
        text_lower = text.lower()

        best_category = "GENERAL"
        best_match_count = 0

        # count matches per category
        for category, patterns in self.rules.items():
            score = sum(1 for p in patterns if re.search(p, text_lower))
            if score > best_match_count:
                best_match_count = score
                best_category = category

        # compute a simple confidence estimate
        confidence = min(1.0, best_match_count / 3) if best_match_count > 0 else 0.15

        return {
            "category": best_category,
            "subtype": f"{best_category}_GENERIC",
            "confidence": confidence
        }


# convenience function
def classify_text(text: str) -> Dict:
    return Classifier().classify(text)
