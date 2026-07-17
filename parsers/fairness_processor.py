from pathlib import Path
import json

from parsers.normalizer import Normalizer
from parsers.bias_reducer import BiasReducer


class FairnessProcessor:
    """
    Main Fairness, Normalization & Bias Reduction Engine.
    """

    def __init__(self):
        self.normalizer = Normalizer()
        self.bias_reducer = BiasReducer()

    def process(self, resume_text, skills, ats_score):
        """
        Apply normalization and bias reduction.

        Args:
            resume_text (str)
            skills (list)
            ats_score (float)

        Returns:
            dict
        """

        normalized_text = self.normalizer.normalize_text(resume_text)
        normalized_skills = self.normalizer.normalize_skills(skills)
        normalized_score = self.normalizer.normalize_score(ats_score)

        masked_text = self.bias_reducer.mask_personal_info(
            normalized_text
        )

        bias_report = self.bias_reducer.evaluate_bias(masked_text)

        result = {
            "normalized_text": masked_text,
            "normalized_skills": normalized_skills,
            "normalized_score": normalized_score,
            "bias_report": bias_report
        }

        return result

    def save_output(self, result, output_path):
        """
        Save fairness report as JSON.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"Fairness report saved to: {output_path}")