from pathlib import Path
import json

from parsers.extractor import ResumeExtractor
from parsers.education_extractor import EducationExtractor
from parsers.education_scorer import EducationScorer


class EducationProcessor:
    """
    Main Education & Certification Parsing Engine.
    """

    def __init__(self):
        self.extractor = ResumeExtractor()
        self.education_extractor = EducationExtractor()
        self.education_scorer = EducationScorer()

    def process(self, resume_path, target_role):
        """
        Process resume and evaluate education relevance.

        Args:
            resume_path (str)
            target_role (str)

        Returns:
            dict
        """

        resume_path = Path(resume_path)

        # Extract cleaned resume text
        cleaned_text = self.extractor.extract_resume(resume_path)

        # Extract education details
        education = self.education_extractor.extract(cleaned_text)

        # Evaluate education relevance
        relevance = self.education_scorer.score(
            education,
            target_role
        )

        result = {
            "education": education,
            "relevance": relevance
        }

        return result

    def save_output(self, result, output_path):
        """
        Save structured academic profile as JSON.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"Education report saved to: {output_path}")