from pathlib import Path
import json

from parsers.extractor import ResumeExtractor
from parsers.experience_extractor import ExperienceExtractor
from parsers.experience_scorer import ExperienceScorer


class ExperienceProcessor:
    """
    Main Experience Parsing & Relevance Engine.
    """

    def __init__(self):
        self.extractor = ResumeExtractor()
        self.experience_extractor = ExperienceExtractor()
        self.experience_scorer = ExperienceScorer()

    def process(self, resume_path, target_role):
        """
        Process resume and compute experience relevance.

        Args:
            resume_path (str)
            target_role (str)

        Returns:
            dict
        """

        resume_path = Path(resume_path)

        # Extract cleaned resume text
        cleaned_text = self.extractor.extract_resume(resume_path)

        # Extract experience details
        experience = self.experience_extractor.extract(cleaned_text)

        # Calculate relevance
        relevance = self.experience_scorer.score(
            experience,
            target_role
        )

        result = {
            "experience": experience,
            "relevance": relevance
        }

        return result

    def save_output(self, result, output_path):
        """
        Save structured experience JSON.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"Experience report saved to: {output_path}")