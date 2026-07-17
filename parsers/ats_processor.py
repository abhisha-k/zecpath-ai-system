from pathlib import Path
import json

from parsers.weight_manager import WeightManager
from parsers.ats_scorer import ATSScorer


class ATSProcessor:
    """
    Main ATS Scoring Engine.
    """

    def __init__(self):
        self.weight_manager = WeightManager()

        if not self.weight_manager.validate_weights():
            raise ValueError("ATS weights must total 100.")

        self.scorer = ATSScorer(
            self.weight_manager.get_weights()
        )

    def process(
        self,
        skill_score,
        experience_score,
        education_score,
        semantic_score
    ):
        """
        Generate ATS score.
        """

        result = self.scorer.calculate(
            skill_score,
            experience_score,
            education_score,
            semantic_score
        )

        return result

    def save_output(self, result, output_path):
        """
        Save ATS report.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"ATS report saved to: {output_path}")