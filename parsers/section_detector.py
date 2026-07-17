import re
import logging


class SectionDetector:
    """
    Detects major sections within a resume.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.section_patterns = {
            "skills": [
                "skills",
                "technical skills",
                "core competencies"
            ],
            "experience": [
                "experience",
                "work experience",
                "professional experience",
                "employment"
            ],
            "education": [
                "education",
                "academic background",
                "qualification",
                "qualifications"
            ],
            "projects": [
                "projects",
                "academic projects",
                "personal projects"
            ],
            "certifications": [
                "certifications",
                "certificates",
                "licenses"
            ]
        }

    def detect_sections(self, text):
        """
        Detect resume section headings.

        Returns:
            dict
        """

        detected_sections = {}

        lines = text.split("\n")

        for line in lines:

            heading = line.strip().lower()

            for section, patterns in self.section_patterns.items():

                if heading in patterns:

                    detected_sections[section] = line.strip()

        self.logger.info("Resume sections detected successfully.")

        return detected_sections