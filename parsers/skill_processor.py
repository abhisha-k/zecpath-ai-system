from pathlib import Path
import json

from parsers.extractor import ResumeExtractor
from parsers.skill_extractor import SkillExtractor
from parsers.skill_scorer import SkillScorer


class SkillProcessor:
    """
    Main Skill Extraction Engine.
    """

    def __init__(self):
        self.extractor = ResumeExtractor()
        self.skill_extractor = SkillExtractor()
        self.skill_scorer = SkillScorer()

    def process(self, resume_path):
        """
        Extract and score skills from a resume.

        Args:
            resume_path (str)

        Returns:
            dict
        """

        resume_path = Path(resume_path)

        # Extract cleaned resume text
        cleaned_text = self.extractor.extract_resume(resume_path)

        # Extract skills
        extracted_skills = self.skill_extractor.extract(cleaned_text)

        # Assign confidence scores
        scored_skills = self.skill_scorer.score(extracted_skills)

        return scored_skills

    def save_output(self, skills, output_path):
        """
        Save structured skills as JSON.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(skills, file, indent=4)

        print(f"Skill report saved to: {output_path}")