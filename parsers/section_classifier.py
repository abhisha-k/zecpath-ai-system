import logging

from parsers.section_detector import SectionDetector


class SectionClassifier:
    """
    Classifies resume content into structured sections.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.detector = SectionDetector()

    def classify(self, text):
        """
        Classify resume into sections.

        Args:
            text (str)

        Returns:
            dict
        """

        detected = self.detector.detect_sections(text)

        sections = {
            "skills": "",
            "experience": "",
            "education": "",
            "projects": "",
            "certifications": ""
        }

        current_section = None

        lines = text.split("\n")

        for line in lines:

            heading = line.strip().lower()

            found = False

            for section, patterns in self.detector.section_patterns.items():

                if heading in patterns:

                    current_section = section
                    found = True
                    break

            if found:
                continue

            if current_section:

                sections[current_section] += line + "\n"

        self.logger.info("Resume classified into sections successfully.")

        return sections