from pathlib import Path
import json

from parsers.extractor import ResumeExtractor
from parsers.section_classifier import SectionClassifier


class SectionProcessor:
    """
    Main Resume Section Segmentation Engine.
    """

    def __init__(self):
        self.extractor = ResumeExtractor()
        self.classifier = SectionClassifier()

    def process(self, resume_path):
        """
        Process a resume and classify its sections.

        Args:
            resume_path (str)

        Returns:
            dict
        """

        resume_path = Path(resume_path)

        # Extract cleaned resume text
        cleaned_text = self.extractor.extract_resume(resume_path)

        # Classify sections
        sections = self.classifier.classify(cleaned_text)

        return sections

    def save_output(self, sections, output_path):
        """
        Save structured resume sections as JSON.
        """

        output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(sections, file, indent=4)

        print(f"Segmented resume saved to: {output_path}")